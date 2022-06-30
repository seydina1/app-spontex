# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:11:58 2022

@author: seydi
"""

import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données et traitement des données
data_pcr = pd.read_excel("data_pcr.xlsx")
data_pcr = data_pcr[0:53]
print(data_pcr.describe())
X = data_pcr["PCR Complété"]
y = data_pcr[["Temps de réponse PCR en JO"]]


# Graphe
plt.title("Temps de réponse PCR en JO CDG en fonction du temps de réponse PCR en JO")
plt.xlabel("PCR Complété")
plt.ylabel("Temps de réponse PCR en JO ")
plt.scatter(X,y)