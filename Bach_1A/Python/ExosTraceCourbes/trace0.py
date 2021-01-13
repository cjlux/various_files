# Exemples de tracés de courbes simples

import numpy as np # numpy Python numérique : tableaux, vecteurs
import matplotlib.pyplot as plt

def fonction1(x):
    return x**2

X = np.linspace(0,10,50) # 50 pts réguliérement espacés entre 0 et 10
Y = fonction1(X)

plt.figure()    # crée une fenêtre vide
plt.plot(X, Y)  # effectue le tracé... X : abscisses et Y:ordonnées
plt.show()      # fait apparaître la fenêtre surgissante
