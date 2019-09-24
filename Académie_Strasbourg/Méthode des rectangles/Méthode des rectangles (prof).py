import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import numpy as np
from math import e

def Aire_rect(l,L):
    return l*L

def f(x):
    return e**(-x**2)


# cette fonction utilise la fonction f et la fonction Aire_rect
def Methode_rectangle(n):
    
    # tracé de la courbe de f
    prec=0.05
    abs_fonc = np.arange(0,1+prec,prec)
    ord_fonc = f(abs_fonc)
    plt.plot(abs_fonc,ord_fonc,color='green')
    
    ax = plt.gca()
    
    #initialisation du compteur
    Aire_inf=0
    
    # tracé des rectangles et calcul de l'aire
    l=1/n
    for k in range(n):
        x=k*1/n
        L=f(x+1/n)
        #Rectangle défini par le point en bas à gauche,
        #sa largeur l et sa longueur L
        rect=ptc.Rectangle( (x,0) , l, L, fill=False)
        ax.add_patch(rect)  
        
        #incrément du compteur
        Aire_inf = Aire_inf + Aire_rect(l,L)

    # affichage de l'aire sous la figure
    plt.text(0,-0.1,'Aire='+str(Aire_inf)) 
    # reglage des bornes des axes du repere
    plt.axis([0,1,0,1]) 
    # affichage    
    plt.show() 
    # attente d'une action de clic sur la fenetre puis fermeture
    plt.waitforbuttonpress() 
    plt.close() 

    return Aire_inf

