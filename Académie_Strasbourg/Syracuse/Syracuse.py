'''
Formation Python 
Lycee Français de Prague
2019 - Franck CHEVRIER 

Suites de Syracuse
'''

def suiv_Syracuse(p):
    "calcul du terme suivant d'une suite de Syracuse"
    if p%2==0:
        return p//2
    else:
        return 3*p+1

def Deb_Syracuse(a) :
    "établit la liste des 4 premiers termes d'une suite de Syracuse"
    L=[a]
    for k in range(3) :
        n=len(L)
        suiv=suiv_Syracuse(L[n-1])
        L.append(suiv)
    return L

def Tab_Syracuse(a,N):
    "établit la liste des N premiers termes d'une suite de Syracuse"
    L=[a]
    for k in range(N-1) :
        n=len(L)
        suiv=suiv_Syracuse(L[n-1])
        L.append(suiv)
    return L

def Vol_Syracuse(a):
    "établit la liste correspondant à un vol"
    L=[a]
    n=len(L)
    while L[n-1]!=1: #L[-1] donne le dernier élément de la liste L    
        suiv=suiv_Syracuse(L[n-1])
        L.append(suiv)
        n=len(L)
    return L
    
def altitude_150():
    "donne le plus petit a tel que le vol atteint l'altitude 150"
    a=1
    while max(Vol_Syracuse(a))<150:
        a=a+1
    return a
    
def duree_vol_40():
    "donne le plus petit a tel que le vol a une durée d'au moins 40"
    a=1
    while len(Vol_Syracuse(a))<40:
        a=a+1
    return a    
        
def altitude(M):
    "donne le plus petit a tel que le vol atteint l'altitude M"
    a=1
    while max(Vol_Syracuse(a))<M:
        a=a+1
    return a
    
def duree_vol(T):
    "donne le plus petit a tel que le vol a une durée d'au moins T"
    a=1
    while len(Vol_Syracuse(a))<T:
        a=a+1
    return a     

def vol_le_plus_long(N):
    "renvoie la valeur de a inférieure à N pour laquelle le vol est le plus long"
    candidat=1
    longueur_cand=1
    for a in range(2,N):
        long_a=len(Vol_Syracuse(a)) #pour ne pas effectuer 2x le calcul
        if long_a>longueur_cand:
            candidat=a
            longueur_cand=long_a
    return candidat #on peut compléter avec: ,longueur

def vol_le_plus_haut(N):
    "renvoie la valeur de a inférieure à N pour laquelle l'altitude atteinte est maximale"
    candidat=1
    altitude=1
    for a in range(2,N):
        alt_a=max(Vol_Syracuse(a)) #pour ne pas effectuer 2x le calcul
        if alt_a>altitude:
            candidat=a
            altitude=alt_a
    return candidat #on peut compléter avec: ,altitude



''' 
Compléments pour l'enseignant: Autres écritures des fonctions
'''


def suiv_Syracuse_2(p):
    return 3*p+1 if p%2 else p//2 #p%2 renvoie 0 ou 1 (booléen)
   
    
def Deb_Syracuse_2(a) :
    L=[a]
    for k in range(3) :
        L.append(suiv_Syracuse(L[len(L)-1]))
    return L


def Tab_Syracuse_2(a,N) :
    L=[a]
    for k in range(N-1) :
        L.append(suiv_Syracuse(L[len(L)-1]))
    return L


def Vol_Syracuse_2(a):
    L=[a]
    while L[-1]!=1: #L[-1] donne le dernier élément de la liste L
        L.append(suiv_Syracuse(L[-1]))
    return L
 
    
def altitude_2(M,a=1):
    return a if max(Vol_Syracuse(a))>=M else altitude_2(M,a+1)
   
    
def duree_vol_2(T,a=1):
    return a if len(Vol_Syracuse(a))>=T else duree_vol_2(T,a+1)

'''
Franck CHEVRIER - JAP 2019 - Académie de Strasbourg
''' 
