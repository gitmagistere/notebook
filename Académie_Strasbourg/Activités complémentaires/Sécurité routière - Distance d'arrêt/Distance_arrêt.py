'''
Formation Python 
Lycee Français de Prague
2019 - Franck CHEVRIER

Securite routiere - Distance d'arrêt
'''  

'''
PARTIE I: Corrige standard
'''

# question 1

def R(v):
    "Calcul de la vitesse de reaction"
    return v/3.6

# question 2

def F(v):
    "Calcul de la distance de freinage (temps sec)"
    return v**2/200

# question 3

def A(v):
    "Calcul de la distance d'arret (temps sec)"
    return R(v)+F(v)

# question 4

def Crash(v,d):
    "Indique si un crash a lieu (temps sec)"
    if A(v)>=d:
        return True
    else:
        return False

# question 6

def F(v,M):
    "Calcul de la distance de freinage (temps sec ou humide)"
    if M==True:
        return v**2/200*2
    else:
        return v**2/200

def A(v,M):
    "Calcul de la distance d'arret (temps sec ou humide)"
    return R(v)+F(v,M)

def Crash(v,d,M):
    "Indique si un crash a lieu (temps sec ou humide)"
    if A(v,M)>=d:
        return True
    else:
        return False

# questions 8,9

def test(d,M):
    v=0
    while Crash(v,d,M)==False:
        v=v+5
    return v-5

'''
PARTIE II: Syntaxes expertes
'''

def F(v,M):
    return v**2/200*2 if M else v**2/200
    
def A(v,M):
    return R(v)+F(v,M)

def Crash(v,d,M):
    return A(v,M)>=d

def test(d,M):
    v=0
    while Crash(v,d,M)==False:
        v=v+5
    return v-5


    
    