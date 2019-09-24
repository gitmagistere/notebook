'''
Formation Python 
Lycee Français de Prague
2019 - Franck CHEVRIER

Securite routiere - Test d'alcoolemie
''' 

'''
PARTIE I: Corrige standard
'''

#question 1

def A(n,v,d):
    "calcule la quantite d'alcool"
    return n*v*d/10

#question 2

def T(n,v,d,m):
    "calcule le taux d'alcoolemie pour un homme"
    return 0.8*A(n,v,d)/(0.7*m)

#question 3

def Alctest(n,v,d,m):
    if T(n,v,d,m)<=0.5:
        return True
    else:
        return False

#question 5

def T(n,v,d,m,S):
    "calcule le taux d'alcoolemie pour un homme ou une femme"
    if S==True:
        k=0.7
    else:
        k=0.6
    return 0.8*A(n,v,d)/(k*m)

def Alctest(n,v,d,m,S):
    "teste le taux d'alcoolemie"
    if T(n,v,d,m,S)<=0.5:
        return True
    else:
        return False    
    
#question 7

def tab(v=250,d=5,m=75,S=True):
    "dresse la liste des taux d'alcoolemie suivant le nombre de verres (0 a 4)"
    L=[]
    for n in range(5):
        L.append(T(n,v,d,m,S))
    return L

#questions 8,9

def cherche(v=125,d=3,m=75,S=True):
    "cherche le nombre de verres max pour avoir un test d'alcoolemie negatif"
    n=0
    while Alctest(n,v,d,m,S)==True:
        n=n+1
    return n-1

'''
PARTIE II: Syntaxes expertes
'''

def A(n,v,d): 
    return n*v*d/10

def T(n,v,d,m,S):
    k= 0.7 if S else 0.6
    return 0.8*A(n,v,d)/(k*m)

def Alctest(n,v,d,m,S): 
    return T(n,v,d,m,S)<=0.5

def tab(v,d,m,S,N=5):
    return [T(n,v,d,m,S) for n in range(N)]
    
def cherche(v,d,m,S):
    n=0
    while Alctest(n,v,d,m,S): n+=1
    return n-1    
    
    