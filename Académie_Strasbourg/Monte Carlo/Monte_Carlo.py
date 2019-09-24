'''
Formation Python 
Lycee Français de Prague
2019 - Franck CHEVRIER

Methode de Monte-Carlo
'''

'''
Questions 1 à 6
'''

#import des bibliotheques
from random import*
import matplotlib.pyplot as plt


def dans_P(x,y):
    return y<=x**2

def MonteCarlo(n):
    
    # initialisation du compteur de points dans P
    compteur=0
    
    for k in range(n):
        # generation de coordonnees aleatoires entre 0 et 1 pour un point M dans C
        x,y=random(),random()    
        
        if dans_P(x,y):
            # placement du point M dans le repere (en rouge)
            plt.scatter(x,y,color='red')     
            # incrementation du compteur
            compteur = compteur+1
        else:
            # placement du point M dans le repere (en bleu)
            plt.scatter(x,y,color='blue') 
        
    # calcul de la fréquence de points dans P
    f=compteur/n
    # affichage de la frequence dans la fenetre       
    plt.text(0,-0.1,"Fréquence des points dans C: "+str(f))
    
    # reglage des bornes des axes du repere
    plt.axis([0,1,0,1]) 
    # ouverture de la fenetre graphique et affichage
    plt.show() 
    # attente d'une action de clic sur la fenetre puis fermeture
    plt.waitforbuttonpress() 
    plt.close() 
    
    return f

