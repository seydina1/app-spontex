# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 13:34:42 2022

@author: seydi
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# Traitement des données
pcr = pd.read_excel("pcr.xlsx",engine='openpyxl')
pcr = pcr[0:53]
X = pcr[["PCR Reçu"]]
y = pcr["PCR Complété"]

#Graphe et visualisation
print(pcr.describe())
plt.title("PCR Complété en fonction du PCR Reçu")
plt.xlabel("PCR Reçu")
plt.ylabel("PCR Complété")
plt.scatter(X,y)

# Regression linéaire
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Droite d'ajustement
plt.plot(X,y_pred, color='red')

# Détermination des coefficients
a0 = model.intercept_
a1 = model.coef_

# Metrics
r2_score = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
print("La précision du model est de:",100*r2_score, "%")

pickle_out = open("model_linear_pcr_complete_recu.pkl","wb")
pickle.dump(model,pickle_out)
pickle_out.close()


