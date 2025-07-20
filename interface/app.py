
import streamlit as st
import random

st.set_page_config(page_title="Scoring Crédit", layout="centered")

st.title("💳 Application de Scoring Crédit")

st.markdown("Remplissez les informations du client pour simuler une prédiction de défaut de crédit.")

# Formulaire simplifié
age = st.slider("Âge", 18, 100, 35)
income = st.number_input("Revenu mensuel (€)", min_value=0, value=3000)
nb_credits = st.number_input("Nombre de crédits en cours", min_value=0, value=1)
dette_ratio = st.slider("Ratio d’endettement", 0.0, 1.0, 0.3)
nb_retards = st.slider("Nombre de retards de paiement", 0, 10, 0)

if st.button("🔍 Prédire le risque"):
    # Règle simple ou aléatoire
    if nb_retards > 2 or dette_ratio > 0.6:
        st.error("❌ Risque élevé de défaut !")
    else:
        st.success("✅ Faible risque de défaut.")
