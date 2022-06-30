# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 09:26:48 2022

@author: seydi
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.subplots as make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import pickle

# Chargement de mes données
df = pd.read_excel("data_pcr_complet.xlsx",engine='openpyxl')
df = df[0:53]

# Titre de mon application 
st.title("Analyse du PCR de janvier 2018 au mai 2022 ")
st.markdown("Cette application est un tableau de bord")

# Sidebar
st.sidebar.title("Analyse du PCR de janvier 2018 au mai 2022")
graph_type = st.sidebar.selectbox("Type de graphes" , ["Line chart","Bar chart"])
select_axe_abscisse = st.sidebar.selectbox("Axe des abscisses", list(df.columns.values))
select_axe_ordonnee = st.sidebar.selectbox("Axe des ordonnées", list(df.columns.values))
# Dataframe
st.title("Tableau de données du PCR")
st.table(df)
st.title("Tableau simplifié")
st.table(df.describe())

# Figure
st.title("Visualisation")
fig  = go.Figure()

if graph_type == 'Line chart':
    if select_axe_abscisse == 'PCR Reçu' and select_axe_ordonnee == 'PCR Complété':
        fig.add_trace(go.Scatter(x = df["PCR Reçu"], y = df["PCR Complété"], mode="markers"))
    if select_axe_abscisse == 'DO Reçu' and select_axe_ordonnee == 'DO Traité':
        fig.add_trace(go.Scatter(x = df["DO Reçu"], y = df["DO Traité"], mode="markers"))
elif graph_type == 'Bar chart':
    if select_axe_abscisse == 'Année' and select_axe_ordonnee == 'Temps de réponse PCR en JO':
        fig.add_trace(go.Bar(x = df["Année"], y = df["Temps de réponse PCR en JO"]))
    if select_axe_abscisse == 'Année' and select_axe_ordonnee == 'Temps de réponse PCR en JO CDG':
        fig.add_trace(go.Bar(x = df["Année"], y = df["Temps de réponse PCR en JO CDG"]))
    if select_axe_abscisse == 'Année' and select_axe_ordonnee == 'PCR Reçu':
        fig.add_trace(go.Bar(x = df["Année"], y = df["PCR Reçu"]))
    if select_axe_abscisse == 'Année' and select_axe_ordonnee == 'PCR Complété':
        fig.add_trace(go.Bar(x = df["Année"], y = df["PCR Complété"]))
    if select_axe_abscisse == 'Année' and select_axe_ordonnee == 'PCR Traité envoyé pour CDG':
        fig.add_trace(go.Bar(x = df["Année"], y = df["PCR Traité envoyé pour CDG"]))
    if select_axe_abscisse == 'Année' and select_axe_ordonnee == 'PCR Annulé':
        fig.add_trace(go.Bar(x = df["Année"], y = df["PCR Annulé"]))
    if select_axe_abscisse == 'Année' and select_axe_ordonnee == 'PCR Réponse faite au demandeur':
        fig.add_trace(go.Bar(x = df["Année"], y = df["PCR Réponse faite au demandeur"]))
    if select_axe_abscisse == 'Année' and select_axe_ordonnee == 'DO Reçu':
        fig.add_trace(go.Bar(x = df["Année"], y = df["DO Reçu"]))
    if select_axe_abscisse == 'Année' and select_axe_ordonnee == 'DO Traité':
        fig.add_trace(go.Bar(x = df["Année"], y = df["DO Traité"]))
st.plotly_chart(fig)


# Matrice de corrélation avec seaborn
st.title("Matrice de Corrélation")
img = Image.open("Matrice_de_correlation.png")
st.image(img)

# Machine learning
pickle_in = open('model_linear_pcr_complete_recu.pkl', 'rb')
model = pickle.load(pickle_in)

st.title("Prédiction du Nombre de PCR qui va etre complété par mois")
pcr_recu = st.text_input("PCR Reçu")
def prediction():
    prediction = int(pcr_recu)*model.coef_ + model.intercept_
    print(prediction)
    return prediction

def main():
    resultat = ""
    if st.button("Prédiction"):
        resultat = prediction()
    st.success("Le nombre de PCR qui sera complété est {}".format(resultat))
    
    
if __name__=='__main__':
    main()    
    