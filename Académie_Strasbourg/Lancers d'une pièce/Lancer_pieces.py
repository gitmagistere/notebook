'''
Formation Python 
Lycee Français de Prague
2019 - Franck CHEVRIER

Lancers d'une piece (introduction aux variables aleatoires)
'''  

from random import*


def piece():
    '''
    fonction qui simule le lancer d'une pièce
    
    '''
    return randint(0,1)
    
    
def jeux(N):
    '''
    fonction qui simule N parties
    Le resultat est une liste contenant dans cet ordre:
    - le nombre de parties gagnees
    - le nombre de parties nulles
    - le nombre de parties perdues
    '''
    res=[0,0,0]
    
    for i in range(N):
        
        lancers=[piece() for k in range(3)]
        nb_piles=sum(lancers)
        
        if nb_piles==3:
            res[0]=res[0]+1
        elif nb_piles==2:
            res[1]=res[1]+1
        else:
            res[2]=res[2]+1
    
    return res


def gain_algebrique(L):
    '''
    fonction qui renvoie le gain algebrique du joueur
    '''
    return L[0]*3+L[1]*0+L[2]*(-1)


def gm(L):
    '''
    fonction qui renvoie le gain algebrique moyen par partie
    '''
    return gain_algebrique(L)/sum(L)


'''
liste des probabilites que
- le joueur gagne
- la partie soit nulle
- le joueur perde
'''
Proba=[1/8,3/8,1/2]


def ecart_gain(L):
    '''
    fonction qui renvoie l'ecart entre le gain moyen et l'esperance de gain
    '''
    return gm(L)-gm(Proba)
    