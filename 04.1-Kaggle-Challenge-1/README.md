# Hackathon séries temporelles

## Liens
- Compétition Kaggle, manche 1 : (voir vos emails)
- Formulaire de dépôt : (voir vos emails)

**Manche 1 : lundi 2 novembre 2026, ouverture à 14 h et clôture à 18 h 30, heure de Paris.** Le classement privé sera révélé le **vendredi 6 novembre 2026 à 7 h, heure de Paris**.

## La tâche
Une station météo mesure 14 variables toutes les heures. Pour chaque bloc du test, vous avez les 72 dernières heures. Prévoyez la température `temp_1_C` des 24 heures suivantes. Métrique : RMSE en °C (plus c'est petit, mieux c'est).

Comparez méthodes classiques (décomposition, SARIMA) et réseaux récurrents (reservoir computing, GRU, LSTM).

## Fichier de ce dépôt
- `notebook_demarrage.ipynb` : chargement des données, validation qui imite le test, baselines naïves, **SARIMA**, découpage des données en exemples `X` / `Y`, et écriture de la soumission.

Par défaut, le notebook soumet **SARIMA**, la référence classique. Pour faire mieux, c'est à vous d'écrire votre modèle (ESN, GRU, LSTM…) dans la fonction `predict_mon_modele` : vous pouvez reprendre et adapter le code de vos cours.

Les données ne sont pas dans ce dépôt : elles sont sur la page Kaggle de la compétition.

---

> **Conseil important : dans la première demi-heure, faites les étapes 1 à 6 et déposez tout de suite le notebook et le CSV SARIMA sur le formulaire (étape 9).** Vous avez ainsi une soumission valide qui vous assure la note minimale de SARIMA, même si votre modèle n'est pas prêt à l'échéance. Vous pourrez redéposer une meilleure version ensuite.

## Pas à pas (à faire par les deux membres du binôme, sauf mention contraire)

Les intitulés des boutons Kaggle peuvent varier légèrement. En cas de doute, demandez à l'enseignant.

### 1. Créer son compte Kaggle
1. Allez sur https://www.kaggle.com et cliquez sur **Register** (en haut à droite).
2. Inscrivez-vous avec votre adresse e-mail. **Un seul compte par étudiant.**
3. Vérifiez votre numéro de téléphone : cliquez sur votre photo de profil (en haut à droite), puis **Settings**, puis **Phone verification**. C'est nécessaire pour activer Internet dans les notebooks, par exemple pour installer `reservoirpy` avec `!pip install reservoirpy`.

### 2. Rejoindre la compétition
1. Ouvrez le **lien d'invitation** reçu par e-mail. Vous devez être connecté à Kaggle.
2. À partir de l'ouverture, sur la page de la compétition, cliquez sur **Join Competition**, puis acceptez les règles (**I Understand and Accept**). Si la compétition n'est pas encore ouverte, attendez l'heure annoncée.

### 3. Former l'équipe du binôme
Chacun des deux a maintenant sa propre équipe d'une personne. Il faut les réunir **avant toute soumission** si possible.
1. **Étudiant A** : onglet **Team** de la compétition. Dans le champ du nom d'équipe, tapez le nom choisi par le binôme (c'est ce nom que vous indiquerez dans le formulaire de dépôt), puis **Save**.
2. **Étudiant B** : onglet **Team**, section **Merge** (fusion). Cherchez le nom de l'équipe de A, puis cliquez sur **Request Merge**.
3. **Étudiant A** : onglet **Team**, acceptez la demande de fusion (**Accept**).
4. Vérifiez dans l'onglet **Team** que vos deux noms apparaissent, et que le nom d'équipe est le bon.

### 4. Ouvrir le notebook sur Kaggle (un membre du binôme)
1. Téléchargez `notebook_demarrage.ipynb` depuis ce dépôt GitHub (bouton **Download raw file** sur la page du fichier).
2. Sur la page de la compétition, onglet **Code**, cliquez sur **New Notebook**. Un notebook vide s'ouvre ; les données de la compétition sont déjà attachées (panneau de droite, rubrique **Input**).
3. Menu **File**, puis **Import Notebook**, et choisissez le fichier téléchargé.
4. Renommez le notebook en haut à gauche, par exemple `nom-equipe-manche-1`.
5. Si vous avez besoin d'installer une bibliothèque (par exemple `reservoirpy`) : panneau de droite, **Settings**, puis **Internet : On**.

### 5. Partager le notebook (obligatoire)
1. Bouton **Share** (en haut à droite du notebook).
2. Laissez-le **Private**. **Ne le rendez jamais public.**
3. Ajoutez comme collaborateurs votre binôme (**Can edit**) et l'enseignant **neuronalX** (**Can view**), en tapant leur nom d'utilisateur Kaggle.

### 6. Lancer le notebook et faire une première soumission
1. Menu **Run**, puis **Run All** (ou le bouton ▶▶). Attendez la fin (1 à 3 minutes). Le notebook affiche les scores de validation des baselines et de SARIMA, puis écrit le fichier `submission.csv` (SARIMA).
2. En haut à droite, cliquez sur **Save Version**, choisissez **Save & Run All (Commit)**, puis **Save**. Attendez que la version soit terminée (quelques minutes).
3. Ouvrez la version enregistrée, onglet **Output**, et cliquez sur **Submit** à côté de `submission.csv`. Ajoutez une description courte (par exemple `SARIMA`).
4. Votre score public apparaît dans l'onglet **Submissions** de la compétition, et votre équipe dans le **Leaderboard**.
5. Déposez dès maintenant ce notebook et ce CSV sur le formulaire (étape 9) : c'est votre filet de sécurité.

### 7. Écrire votre modèle
1. Dans la section **Votre modèle**, écrivez la fonction `predict_mon_modele(block)` : elle reçoit les 72 dernières heures d'un bloc et renvoie les 24 températures prévues. Les tableaux `X_fit`, `Y_fit` (entraînement) et `X_val`, `val_y` (validation) sont déjà prêts.
2. Décommentez les deux lignes de validation sous la fonction et regardez la **RMSE de validation** : c'est elle qui vous dit si vous progressez. Elle calcule la même métrique que Kaggle.
3. Quand vous faites mieux que SARIMA en validation, remplacez `PREDICT = predict_sarima` par `PREDICT = predict_mon_modele` dans la dernière cellule, puis soumettez comme à l'étape 6.
4. Ne soumettez sur Kaggle que vos meilleurs essais (15 soumissions par jour au maximum).

### 8. Choisir la soumission finale
Onglet **Submissions** : cochez **Use for Final Score** sur vos 2 meilleures soumissions au maximum. Sinon, Kaggle choisit automatiquement celles qui ont le meilleur score public.

### 9. Déposer sur le formulaire (avant l'échéance, un membre du binôme)
1. Téléchargez le notebook de la version ayant produit le CSV final (fichier `.ipynb`, menu **File**, puis **Download Notebook**) et nommez-le avec votre nom d'équipe, par exemple `equipe_bleue.ipynb`.
2. Téléchargez le CSV de votre soumission finale (onglet **Output** de la version soumise) et **renommez-le avec votre nom d'équipe Kaggle**, par exemple `equipe_bleue.csv`.
3. Un membre du binôme ouvre le formulaire (lien reçu par e-mail) et dépose les deux fichiers avant **18 h 30, heure de Paris, le 2 novembre 2026** pour la manche 1. Vérifiez le nom d'équipe, les fichiers et le message de confirmation. En cas d'amélioration, mettez votre dépôt à jour avant cette échéance.

---

## Règles
- Une équipe Kaggle par binôme ; un seul compte Kaggle par étudiant.
- Travaillez et soumettez depuis un notebook Kaggle **privé**, partagé uniquement avec votre binôme et avec l'enseignant. Rendre son notebook public est interdit.
- Avant chaque échéance, déposez le notebook et le CSV de la soumission finale sur le formulaire.
- Données externes interdites. Partage de code ou de prédictions entre binômes interdit.
- Toute copie avérée entraîne 0 pour les binômes impliqués, après examen par l'enseignant. La vérification automatique signale des similarités ; elle ne prononce aucune sanction. Les éléments communs provenant des notebooks fournis ne constituent pas, à eux seuls, une preuve de copie.
- Le classement public (environ 30 % du test) permet de suivre vos résultats. La note utilise le classement privé (environ 70 %), révélé pour la manche 1 le **6 novembre 2026 à 7 h, heure de Paris**.
- Les soumissions et dépôts après l'échéance ne sont pas pris en compte pour la notation.
- Vérifiez le fuseau affiché par Kaggle : l'interface peut afficher les heures locales ou UTC. Pour la manche 1, l'échéance est **18 h 30 à Paris**, soit **17 h 30 UTC**, le 2 novembre 2026.
- Manches suivantes : J+2 à 23 h 59 (manche 2), J+14 (manche 3), J+60 (manche 4) ; les dates et heures précises seront confirmées par l'enseignant.
