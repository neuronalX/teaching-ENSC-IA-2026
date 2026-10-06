"""Fonctions fournies pour les TP : données simulées, références et protocole.

L'écriture de ces utilitaires n'est pas l'objet des exercices. Aucune donnée
réelle ni performance garantie : les scores proviennent uniquement de la simulation.
"""
import numpy as np

def signal_long(n=480, seed=2026, rupture=False):
    t=np.arange(n)
    x=18+.008*t+2*np.sin(2*np.pi*t/24)+np.random.default_rng(seed).normal(0,.65,n)
    if rupture: x[t>=384]+=3
    return t,x

def acf_simple(x, maxlag=36):
    x=np.asarray(x,float); z=x-x.mean(); den=z@z
    if den==0: raise ValueError('ACF indéfinie pour une constante')
    return np.array([z[k:]@z[:len(z)-k]/den for k in range(maxlag+1)])

def mae(y,p): return float(np.mean(np.abs(np.asarray(y)-np.asarray(p))))
def rmse(y,p): return float(np.sqrt(np.mean((np.asarray(y)-np.asarray(p))**2)))

def reference(x, origins, H=1, method='naif', period=24, width=6):
    """Prévisions émises séparément à chaque origine : jamais de x[t+H]."""
    x=np.asarray(x); origins=np.asarray(origins,int)
    if method=='naif': return x[origins]
    if method=='moyenne': return np.array([x[t-width+1:t+1].mean() for t in origins])
    if method=='saisonnier':
        # Dernière observation de la phase cible connue à l'origine, même si H>period.
        indices=origins+H-period*int(np.ceil(H/period))
        if indices.min()<0: raise ValueError('Historique saisonnier insuffisant')
        return x[indices]
    raise ValueError(method)

def niveau_ses(x, alpha):
    levels=np.empty(len(x)); levels[0]=x[0]
    for i in range(1,len(x)): levels[i]=alpha*x[i]+(1-alpha)*levels[i-1]
    return levels

def design(x,H=6,lags=(0,1,23,24),calendar=True):
    """Entrées à l'origine t, cible t+H. Les lags sont relatifs à t."""
    origins=np.arange(max(lags),len(x)-H)
    X=np.column_stack([np.asarray(x)[origins-lag] for lag in lags])
    if calendar:
        q=origins+H
        X=np.column_stack([X,np.sin(2*np.pi*q/24),np.cos(2*np.pi*q/24),q/480])
    return X,np.asarray(x)[origins+H],origins

def fit_ridge(X,y,alpha=1):
    """Standardisation apprise sur X seulement ; intercept non pénalisé."""
    X=np.asarray(X,float); mu=X.mean(0); sd=X.std(0); sd=np.where(sd>1e-12,sd,1)
    Z=np.column_stack([np.ones(len(X)),(X-mu)/sd])
    penalty=np.eye(Z.shape[1])*alpha;penalty[0,0]=0
    beta=np.linalg.solve(Z.T@Z+penalty,Z.T@y)
    return {'mu':mu,'sd':sd,'beta':beta,'alpha':alpha}

def predict_ridge(model,X):
    return np.column_stack([np.ones(len(X)),(X-model['mu'])/model['sd']])@model['beta']

def optional_statsmodels():
    try:
        from statsmodels.tsa.arima.model import ARIMA
        from statsmodels.tsa.holtwinters import ExponentialSmoothing
        return ARIMA,ExponentialSmoothing
    except ImportError:
        return None,None
