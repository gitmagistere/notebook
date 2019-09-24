import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import numpy as np

# cette fonction utilise la fonction f
def Methode_rectangle():
    
    # tracé de la courbe de f
    prec=0.05
    abs_fonc = np.arange(0,1+prec,prec)
    ord_fonc = f(abs_fonc)
    plt.plot(abs_fonc,ord_fonc,color='green')
    
    ax = plt.gca()
    
    # tracé des rectangles
    l=1/4
    for k in range(4):
        x=k*1/4
        L=f(x+1/4)
        #Rectangle défini par le point en bas à gauche,
        #sa largeur l et sa longueur L
        rect=ptc.Rectangle( (x,0) , l, L, fill=False)
        ax.add_patch(rect)  

    # reglage des bornes des axes du repere
    plt.axis([0,1,0,1]) 
    # affichage    
    plt.show() 
    # attente d'une action de clic sur la fenetre puis fermeture
    plt.waitforbuttonpress() 
    plt.close() 

    return None

