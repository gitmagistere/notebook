import matplotlib.pyplot as plt

# (pour fonctionner, necessite que la fonction h soit creee au prealable)

def approx_long_courbe():
    
    for k in range(4):
        
        # calcul des abscisses de deux points consécutifs
        x1=k/4
        x2=(k+1)/4
        
        # affichage du segment reliant ces points
        plt.plot([x1,x2],[h(x1),h(x2)],color='blue')
    
    # ouverture de la fenetre graphique et affichage
    plt.show() 
    # attente d'une action de clic sur la fenetre puis fermeture
    plt.waitforbuttonpress() 
    plt.close() 
    
    return None


