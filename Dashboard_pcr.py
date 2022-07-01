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
from streamlit_option_menu import option_menu
import pickle

# Chargement de mes données
df = pd.read_csv("data_pcr_complet_csv.csv")
df = df[0:53]
# Titre de mon application 
st.title("Analyse du PCR de janvier 2018 au mai 2022 ")
# Menu bar horizontal
menu = option_menu(menu_title = "Menu",
                   options = ["Données PCR", "Graphes PCR","Matrice de corrélation","Machine Learning","Importation de données CSV"],
                   icons = ["clipboard-data","graph-down","file-spreadsheet","laptop","upload"],
                   menu_icon = "cast", default_index = 0, orientation = "horizontal")
if menu == "Données PCR":
    # Dataframe
    st.title("Tableau de données du PCR")
    st.table(df)
    st.title("Tableau simplifié")
    st.table(df.describe())
if menu == "Matrice de corrélation":
    # Matrice de corrélation avec seaborn
    st.title("Matrice de Corrélation")
    img = Image.open("Matrice_de_correlation.png")
    st.image(img)
if menu == "Graphes PCR":
    fig1 = plt.figure()
    A2018 = df[["Mois","Temps de réponse PCR en JO"]][0:12]
    A2019 = df[["Mois","Temps de réponse PCR en JO"]][12:24]
    A2020 = df[["Mois","Temps de réponse PCR en JO"]][24:36]
    A2021 = df[["Mois","Temps de réponse PCR en JO"]][36:48]
    A2022 = df[["Mois","Temps de réponse PCR en JO"]][48:53]
    # Graphes 2018
    fig1 = plt.figure()
    plt.title("Temps de réponse PCR en JO par Mois en 2018")
    plt.plot(A2018["Mois"],A2018["Temps de réponse PCR en JO"], "r:o", label="2018")
    plt.bar(A2018["Mois"],A2018["Temps de réponse PCR en JO"],color="blue")
    plt.xticks(rotation=70)
    st.pyplot(fig1)
    # Graphes 
    fig2 = plt.figure()
    plt.title("Temps de réponse PCR en JO par Mois en 2019")
    plt.plot(A2019["Mois"],A2019["Temps de réponse PCR en JO"], "r:o", label="2019")
    plt.bar(A2019["Mois"],A2019["Temps de réponse PCR en JO"],color="blue")
    plt.xticks(rotation=70)
    st.pyplot(fig2) 
    # Graphes 2020
    fig3 = plt.figure()
    plt.title("Temps de réponse PCR en JO par Mois en 2020")
    plt.plot(A2020["Mois"],A2020["Temps de réponse PCR en JO"], "r:o", label="2020")
    plt.bar(A2020["Mois"],A2020["Temps de réponse PCR en JO"],color="blue")
    plt.xticks(rotation=70)
    st.pyplot(fig3)
    # Graphes 2021
    fig4 = plt.figure()
    plt.title("Temps de réponse PCR en JO par Mois en 2021")
    plt.plot(A2021["Mois"],A2021["Temps de réponse PCR en JO"], "r:o", label="2021")
    plt.bar(A2021["Mois"],A2021["Temps de réponse PCR en JO"],color="blue")
    plt.xticks(rotation=70)
    st.pyplot(fig4)
    # Graphe 2018 et 2020
    fig5 = plt.figure()
    plt.title("Temps de réponse PCR en JO par Mois de 2018 et de 2020")
    plt.plot(A2018["Mois"],A2018["Temps de réponse PCR en JO"], "r:o", label="2018")
    plt.plot(A2020["Mois"],A2020["Temps de réponse PCR en JO"], "g:o", label="2020")
    plt.xticks(rotation=70)
    plt.legend()
    st.pyplot(fig5)
     # Graphe 2019 et 2021
    fig6 = plt.figure()
    plt.title("Temps de réponse PCR en JO par Mois de 2019 et 2021")
    plt.plot(A2019["Mois"],A2019["Temps de réponse PCR en JO"], "b:o", label="2019")
    plt.plot(A2021["Mois"],A2021["Temps de réponse PCR en JO"], "y:o", label="2021")
    plt.xticks(rotation=70)
    plt.legend()
    st.pyplot(fig6)

        
if menu == "Machine Learning":
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
        
if menu == "Importation de données CSV":
    # Importation d'un fichier CSV
    uploaded_files = st.file_uploader("Choisir un fichier CSV", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        dataFrame = pd.read_csv(uploaded_file)
        st.write(dataFrame)
        st.write(dataFrame.describe())
        # Sidebar
        st.sidebar.title("Analyse du PCR")
        graph_type = st.sidebar.selectbox("Type de graphes" , ["Scatter chart","Bar chart"])
        # Personalisation Graphes
        st.title("Visualisation Personnalisée")
        fig  = go.Figure()
        select_axe_abscisse = st.sidebar.selectbox("Axe des abscisses", list(dataFrame.columns.values))
        select_axe_ordonnee = st.sidebar.selectbox("Axe des ordonnées", list(dataFrame.columns.values))
        if graph_type == 'Scatter chart':
            if select_axe_abscisse and select_axe_ordonnee:
                fig.add_trace(go.Scatter(x = dataFrame[select_axe_abscisse] , y =  dataFrame[select_axe_ordonnee], mode="markers"))
        elif graph_type == 'Bar chart':
            if select_axe_abscisse and select_axe_ordonnee:
                fig.add_trace(go.Bar(x = dataFrame[select_axe_abscisse] , y =  dataFrame[select_axe_ordonnee]))
        st.plotly_chart(fig) 
        
    
 
    
    





    
    