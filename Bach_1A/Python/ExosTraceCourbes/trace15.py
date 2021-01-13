# Exemples de tracés de courbes simples

import numpy as np # numpy Python numérique : tableaux, vecteurs
import matplotlib.pyplot as plt

# lecture des données du fichier data.txt avec la focntion moadtxt de
# numpy :
nom_fichier = "data.txt"
data = np.loadtxt(nom_fichier)
#type(data) - > ndarray : tableau n-dimensionnel numpy
# data.shape -> renvoie le tupe qui donne les dimensions du ndarray
temps = data[:, 0]  # 1ere colonne
T1    = data[:, 1]  # 2me colonne
T2    = data[:, 2]  # 3me colonne

T1 = T1 - 273.15  # conversion Kelnin -> ° C
T2 = T2 - 273.15

plt.figure()    # crée une fenêtre vide
plt.plot(temps, T1, "o-b", label="T1")  # effectue le tracé : des ronds bleus 
                                        # reliés par des traits
plt.plot(temps, T2, "o-m", label="T2")  # effectue le tracé : des ronds magenta
                                        # reliés par des traits
plt.xlabel("Temps [s]")
plt.ylabel("Température [°C]")
plt.grid()
plt.legend()
plt.title(f"Tracé des températures du fichier '{nom_fichier}'", size=16)
plt.savefig(nom_fichier.replace(".txt", ".png"))
plt.show()      # fait apparaître la fenêtre surgissante
