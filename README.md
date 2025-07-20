# 💳 Credit Scoring App

## 🎯 Objectif du projet

Ce projet vise à prédire le risque de défaut de crédit pour des clients bancaires à partir de leurs informations personnelles et financières.  
L’objectif est d’aider les établissements financiers à mieux gérer le risque de crédit et à prendre des décisions éclairées d’octroi de prêts.

---

## 🧠 Problématique métier

- **Problème** : Comment évaluer le risque de défaut d’un client bancaire ?
- **Objectif** : Déterminer automatiquement si un client est “à risque” ou “non à risque”.
- **Valeur ajoutée** : Gain de temps pour les agents de crédit, réduction du risque de défaut, automatisation du processus d’analyse.

---

## 🗃️ Données utilisées

- **Source** : [Kaggle - Credit Risk Dataset](https://www.kaggle.com/datasets)
- **Fichier utilisé** : `credit_data.csv` (dans `/data`)
- **Structure** :
  - Variables numériques : `age`, `income`, `loan_amount`...
  - Variables catégorielles : `job_type`, `housing`, `loan_status`...
  - Cible : `default` (0 = bon client, 1 = client à risque)

---

## ⚙️ Pipeline de traitement

1. **Prétraitement** :
   - Nettoyage des valeurs manquantes
   - Normalisation des données numériques
   - Encodage des variables catégorielles

2. **Analyse exploratoire** :
   - Statistiques descriptives
   - Visualisations : distribution des défauts, revenus par statut, heatmap de corrélation

3. **Modélisation** :
   - Modèle de scoring simple (logique conditionnelle ou RandomForest)
   - Évaluation via `accuracy`, `recall`, `precision`, `f1-score`

4. **Interface utilisateur** :
   - Créée avec **Streamlit**
   - Permet à l'utilisateur d'entrer les infos d'un client
   - Affiche la prédiction de risque en temps réel

---

## 🖥️ Interface Streamlit

- Code : [`/interface/app.py`](interface/app.py)
- Lancement local :https://da39005d0745.ngrok-free.app/

```bash
streamlit run interface/app.py
<img width="971" height="870" alt="image" src="https://github.com/user-attachments/assets/92014c72-cff5-4503-ac03-2f238d507728" />
