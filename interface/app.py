
import streamlit as st
import pandas as pd
import os
from src.load_data import load_data
from src.clean_data import clean_data
from src.preprocess import preprocess_data
from src.visualize import show_visualizations

st.set_page_config(page_title="Scoring Crédit", layout="wide")

st.title("📊 Scoring Crédit - Analyse des risques de défaut")

st.sidebar.header("📁 Données")
data_source = st.sidebar.radio("Choisir la source de données :", ["GitHub", "Charger un fichier CSV"])

if data_source == "GitHub":
    data_url = "https://raw.githubusercontent.com/balriccc/scoring-credit/main/data/cs-training.csv"
    df = load_data(data_url)
else:
    uploaded_file = st.sidebar.file_uploader("Charger un fichier CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, index_col=0)
    else:
        st.warning("Veuillez charger un fichier pour continuer.")
        st.stop()

if df is not None:
    st.success("✅ Données chargées avec succès !")
    st.write(df.head())

    df_clean = clean_data(df)
    st.success("✅ Données nettoyées.")

    df_preprocessed = preprocess_data(df_clean)
    st.success("✅ Données prétraitées.")

    show_visualizations(df_preprocessed)
