
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Scoring Crédit", layout="wide")

st.title("📊 Scoring Crédit - Prédiction du risque de défaut")

# Chargement des données depuis GitHub
DATA_URL = "https://raw.githubusercontent.com/balriccc/scoring-credit/main/data/cs-training.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url, index_col=0)
    return df

@st.cache_resource
def load_model():
    # Charge le modèle entraîné — adapte le chemin si besoin
    # Ici on suppose que tu as mis ton model.joblib dans /interface (attention à la taille !)
    model_path = "interface/model.joblib"
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        st.error(f"Modèle non trouvé à l’emplacement {model_path}")
        return None

df = load_data(DATA_URL)
st.write("Aperçu des données :")
st.dataframe(df.head())

model = load_model()

if model:
    st.write("Entrez les caractéristiques pour prédire le risque de défaut :")
    # Exemple des champs (adapte en fonction de tes features)
    RevolvingUtilizationOfUnsecuredLines = st.number_input("RevolvingUtilizationOfUnsecuredLines", min_value=0.0, max_value=10.0, value=0.5)
    age = st.number_input("Age", min_value=18, max_value=100, value=40)
    DebtRatio = st.number_input("DebtRatio", min_value=0.0, max_value=10.0, value=0.3)
    MonthlyIncome = st.number_input("MonthlyIncome", min_value=0.0, max_value=100000.0, value=5000.0)
    NumberOfOpenCreditLinesAndLoans = st.number_input("NumberOfOpenCreditLinesAndLoans", min_value=0, max_value=50, value=5)
    NumberOfTimes90DaysLate = st.number_input("NumberOfTimes90DaysLate", min_value=0, max_value=50, value=0)
    NumberRealEstateLoansOrLines = st.number_input("NumberRealEstateLoansOrLines", min_value=0, max_value=50, value=0)
    NumberOfTime60_89DaysPastDueNotWorse = st.number_input("NumberOfTime60_89DaysPastDueNotWorse", min_value=0, max_value=50, value=0)
    NumberOfTime30_59DaysPastDueNotWorse = st.number_input("NumberOfTime30_59DaysPastDueNotWorse", min_value=0, max_value=50, value=0)
    NumberOfDependents = st.number_input("NumberOfDependents", min_value=0, max_value=20, value=0)

    input_data = [[
        RevolvingUtilizationOfUnsecuredLines,
        age,
        DebtRatio,
        MonthlyIncome,
        NumberOfOpenCreditLinesAndLoans,
        NumberOfTimes90DaysLate,
        NumberRealEstateLoansOrLines,
        NumberOfTime60_89DaysPastDueNotWorse,
        NumberOfTime30_59DaysPastDueNotWorse,
        NumberOfDependents
    ]]

    if st.button("Prédire le risque"):
        pred = model.predict(input_data)
        proba = model.predict_proba(input_data)[0][1]
        st.write(f"**Prédiction:** {'Défaillant' if pred[0] == 1 else 'Non défaillant'}")
        st.write(f"**Probabilité de défaut:** {proba:.2%}")

else:
    st.warning("Le modèle n'a pas pu être chargé. Vérifiez la présence du fichier model.joblib.")

