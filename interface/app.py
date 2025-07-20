
import streamlit as st
import pandas as pd
from src.load_data import load_data
from src.clean_data import clean_data
from src.preprocess import preprocess_data
from src.visualize import show_visualizations

st.set_page_config(page_title="Scoring Crédit", layout="wide")

st.title("📊 Scoring Crédit - Analyse du risque de défaut")

# Choix de la source de données
st.sidebar.header("📁 Source de données")
data_choice = st.sidebar.radio("Choisissez la source :", ["Depuis GitHub", "Téléversement CSV"])

if data_choice == "Depuis GitHub":
    url = "https://raw.githubusercontent.com/balriccc/scoring-credit/main/data/cs-training.csv"
    df = load_data(url)
else:
    uploaded_file = st.sidebar.file_uploader("Charger un fichier .csv", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, index_col=0)
    else:
        st.stop()

# Affichage des premières lignes
st.subheader("Aperçu des données brutes")
st.dataframe(df.head())

# Nettoyage
df_clean = clean_data(df)
st.success("✅ Données nettoyées")

# Prétraitement
df_processed = preprocess_data(df_clean)
st.success("✅ Données prétraitées")

# Visualisations
show_visualizations(df_processed)
