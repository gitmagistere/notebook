'''
Formation Python 
Lycee Français de Prague
2019 - Franck CHEVRIER

Longueur d'une courbe
'''

from math import*
import matplotlib.pyplot as plt

def h(x):
    return x**2

def long_segment(xA,yA,xB,yB):
    '''
    fonction qui renvoie la longueur d'un segment
    '''
    return sqrt((xB-xA)**2+(yB-yA)**2)

def approx_long_courbe(n=4):
    '''
    fonction qui affiche une courbe 
    approchant une fonction par des segments
    et qui renvoie l'approximation de sa longueur
    '''
    # initialisaion de la variable pour la longueur totale
    Long=0
    
    for k in range(n):
        
        # calcul des abscisses de deux points consécutifs
        x1=k/n
        x2=(k+1)/n
        
        # affichage du segment reliant ces points
        plt.plot([x1,x2],[h(x1),h(x2)],color='blue')
    
        # incrémentation de la longueur totale
        Long=Long+long_segment(x1,h(x1),x2,h(x2))
        
    # ouverture de la fenetre graphique et affichage
    plt.show() 
    # attente d'une action de clic sur la fenetre puis fermeture
    plt.waitforbuttonpress() 
    plt.close() 
    
    return Long
        