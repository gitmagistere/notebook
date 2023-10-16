from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import numpy as np

fig = plt.figure("histogramme",figsize = (7,5)) # taille du graphe
#axes = fig.add_subplot(1,1,1)

xmax = 2.5


palette = ['blue', 'red', 'green','black'] #liste des couleur des histogrammes


def animation_fonction(i): # on définit une fonction qui va créer les images à afficher.
    x = i/50  # on divise par 50, car l'animation comporte 50 images
    R1 = 3 - x
    R2 = 5 - 2 * x
    P1 = 1 + x
    P2 = 0 + 2 * x

    #plt.clf()
    plt.xlabel("Espèces chimiques")
    plt.ylabel("Quantités de matière")
    plt.bar(["Réactif 1", "Réactif 2", "Produit 1","Produit 2"],[R1, R2, P1, P2], color = palette, linewidth = 3, edgecolor = 'white')
# je ruse en entourant l'histogramme d'un contour blanc (edgecolor) assez large (linewidth)
# pour effacer l'histogramme de l'image précédente.

plt.title("Evolution des quantités de matière")

animation = FuncAnimation(fig, animation_fonction,interval = 1, frames = int(xmax*50), repeat = False)
# on affiche dans la fenetre fig les image définies par la fonction animation_fonction. interval permet de ralentir l'animation,
# frame indique le nombre d'image de l'animation. repeat précicise si l'animation est jouée en boucle (défaut) ou non.


plt.show()