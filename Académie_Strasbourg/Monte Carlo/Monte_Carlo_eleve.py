#import des bibliotheques
from random import*
import matplotlib.pyplot as plt


def MonteCarlo():
    
    # generation de coordonnees aleatoires entre 0 et 1 pour un point M dans C
    x,y=random(),random()    
    # placement du point M dans le repere (en bleu)
    plt.scatter(x,y,color='blue')     
    
    # reglage des bornes des axes du repere
    plt.axis([0,1,0,1]) 
    # ouverture de la fenetre graphique et affichage
    plt.show() 
    # attente d'une action de clic sur la fenetre puis fermeture
    plt.waitforbuttonpress() 
    plt.close() 
    
    return None

