# Sources des données


## CO₂ de Mauna Loa — exemple réel de TP-06-R

`co2_mensuel.csv` : 144 valeurs, janvier 1987 à décembre 1998, concentration atmosphérique en ppmv (parties par million en volume). Source : jeu de mesures **hebdomadaires** `statsmodels.datasets.co2`, livré avec statsmodels, sans téléchargement à l’exécution. Le CSV calcule la moyenne arithmétique des valeurs hebdomadaires disponibles dans chaque mois ; il ne s’agit pas de la série mensuelle officielle NOAA/Scripps. Aucun mois n’est manquant sur l’extrait choisi et aucune interpolation n’est appliquée. Génération : `scripts/preparer_co2.py`.

[Documentation et provenance statsmodels](https://www.statsmodels.org/stable/datasets/generated/co2.html). Le jeu est indiqué comme domaine public. Citation fournie par ce distributeur : Keeling, C.D. et T.P. Whorf, 2004, Atmospheric CO2 concentrations derived from flask air samples at sites in the SIO network, dans Trends: A Compendium of Data on Global Change, CDIAC, Oak Ridge National Laboratory, U.S. Department of Energy. Les dates et traitements ci-dessus décrivent notre extrait local, pas une nouvelle mesure expérimentale.
