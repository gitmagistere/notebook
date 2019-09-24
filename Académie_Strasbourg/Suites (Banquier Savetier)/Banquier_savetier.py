''' 
Formation Python 
Lycee Français de Prague
2019 - Franck CHEVRIER 

Un exemple d'etude de suites:
LE BANQUIER ET LE SAVETIER
'''

# Question 1

def C(n):
    '''
    Fonction qui renvoie la somme versee par M Circonspect le n eme jour
    '''
    a=20000
    for k in range(n):
        a = a+10000
    return a

def C2(n):
    '''
    Fonction qui renvoie la somme versee par M Circonspect
    '''
    return 20000+n*10000

def cherche():
    '''
    Fonction qui renvoie le rang du premier jour
    au bout duquel M Circonspect versera plus de 150000€
    '''
    n=0
    while C(n)<150000:
        n=n+1
    return n

# Question 2

def M(n):
    '''
    Fonction qui renvoie la somme versee par M Malin le n eme jour    
    '''
    a=1
    for k in range(n):
        a = a*2
    return a

def M(n):
    '''
    Fonction qui renvoie la somme versee par M Malin le n eme jour    
    '''
    return 2**n

# Question 3

def depasse():
    '''
    Fonction qui renvoie le jour a partir 
    duquel M Malin verse plus que M Circonspect
    '''
    n=0
    while M(n)<C(n):
        n = n+1
    return n

# Question 4

def somme_Circonspect(n):
    '''
    Fonction qui renvoie la somme versee en tout 
    par M Circonspect le n eme jour
    '''
    S=0
    for k in range(n+1):
        S = S+C(k)
    return S

# Questions 5 et 6 

def cherche(Personne,seuil):
    '''
    Fonction qui renvoie le jour a partir duquel
    un personnage verse un montant supérieur au seuil
    '''
    n=0
    while Personne(n)<seuil:
        n = n+1
    return n

# Question 7

def somme(Personne,n):
    '''
    Fonction qui renvoie la somme versee en tout 
    par un personnage le n eme jour 
    '''
    S=0
    for k in range(n+1):
        S = S+Personne(k)
    return S

# Remarque/Complement

def depasse(Pers1,Pers2):
    '''
    Fonction qui renvoie le jour a partir 
    duquel Pers1 verse plus que Pers2
    '''
    n=0
    while Pers1(n)<Pers2(n):
        n = n+1
    return n

# Question 8

def val(Pers):
    '''
    fonction qui renvoie la liste des sommes versees 
    par une personne, chaque jour, pendant les 31 jours du mois
    '''
    L=[]
    for n in range(31):
        L.append(Pers(n))
    return L
    
def val(Pers):
    '''
    fonction qui renvoie la liste des sommes versees 
    par une personne, chaque jour, pendant les 31 jours du mois
    '''
    return [Pers(n) for n in range(31)]

# Question 9

def somme(liste):
    '''
    fonction qui renvoie la somme des valeurs d'une liste
    '''
    S=0
    for k in range(len(liste)):
        S = S+liste[k]
    return S


