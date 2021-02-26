# Tracé du diagramme de distribution des espèces conjuguées A/B
import numpy as np
from matplotlib import pyplot as plt

pKa= float(input("Entrer la valeur du pKa du couple acide-base : pKa = "))
Ci= float(input("Entrer la valeur de la concentration en quantité de matière de l'acide en mol/L: Ci ="))

pH=np.linspace(0,14,100)# 100 valeurs allant de 0 à 14
CA=Ci/(1+10**(pH-pKa))
CB=Ci-CA
pA=CA/Ci*100
pB=CB/Ci*100

plt.title("diagramme de distribution des espèces AH et A-")
plt.xlabel("pH")
plt.ylabel('Pourcentage des espèces(%)')
plt.grid(True)
plt.plot(pH,pA,c='red',label="Pourcentage de la forme acide AH")
plt.plot(pH,pB,c='green',label="Pourcentage de la forme basique A-")
plt.legend()
plt.show()
