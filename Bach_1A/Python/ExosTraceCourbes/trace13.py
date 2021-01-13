# Exemples de tracés de courbes simples

import numpy as np # numpy Python numérique : tableaux, vecteurs
import matplotlib.pyplot as plt

# lecture des données du fichier data.txt avec la focntion moadtxt de
# numpy :
data = np.loadtxt("data.txt")
#type(data) - > ndarray : tableau n-dimensionnel numpy
# data.shape -> renvoie le tupe qui donne les dimensions du ndarray
temps = data[:, 0]  # 1ere colonne
T1    = data[:, 1]  # 2me colonne
T2    = data[:, 2]  # 3me colonne

T1 = T1 - 273.15  # conversion Kelnin -> ° C
T2 = T2 - 273.15

plt.figure()    # crée une fenêtre vide
plt.plot(temps, T1, "o-b")  # effectue le tracé : des ronds bleus reliés par
                            # des traits
plt.xlabel("Temps [s]")
plt.ylabel("Température [°C]")
plt.grid()
plt.show()      # fait apparaître la fenêtre surgissante
