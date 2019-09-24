'''
Formation Python 
Lycee Français de Prague
2019 - Franck CHEVRIER

Derivation, Newton et Dichotomie
'''  


''' 
Activité 1 : Fonctions élémentaires autour de la dérivation 
'''

from scipy import misc

def f(x):
    return 1/4*x**3+x-3

def coeff_dir(xA,yA,xB,yB):
    return (yB-yA)/(xB-xA)

def taux_variation(f,a,h):
    return coeff_dir(a,f(a),a+h,f(a+h))

def coeff_tang(f,a):
    m=misc.derivative(f,a)
    p=f(a)-m*a
    return m,p

def tab_val(f): #fonction donnée dans l'énoncé
    t=[]
    x=0
    for k in range(10):
        t.append(f(x))
        x=x+2
    return t

def tab_val_bis(f,x_0,p,n):
    t=[]
    x=x_0
    for k in range(n):
        t.append(f(x))
        x=x+p
    return t

def cdir_secantes(f,x_0,p,n):
    t=[]
    x=x_0
    for k in range(n):
        x=x+p #Attention: incrément préalable pour éviter une division par 0
        t.append(coeff_dir(x_0,f(x_0),x,f(x)))
    return t    
    
#ou    

def cdir_secantes2(f,x_0,p,n):
    t=[]
    for k in range(1,n+1):
        t.append(taux_variation(f,x_0,k*p))
    return t     
    
''' 
Activité 2 : Méthode de Newton 
'''

def etap_Newton(f,a):
    return a-f(a)/misc.derivative(f,a)
    
def appl_Newton(f,a,n): #fonction donnée dans l'énoncé 
    t=[a]
    for k in range(n): 
        a=etap_Newton(f,a)
        t.append(a)     
    return t

def g(x):
    return x**2-5

def h(x):
    return x**3-7

''' 
Activité 3 : Algorithme de dichotomie 
'''

def etap_dichoto(f,a,b):
    m=(a+b)/2
    if f(a)*f(m)<0:
        return a,m
    else:
        return m,b

def dichoto_iter(f,a,b,n):
    for k in range(n):
        a,b=etap_dichoto(f,a,b)
    return a,b

def dichoto_test(f,a,b,h):
    while b-a>h:
        a,b=etap_dichoto(f,a,b)
    return a,b

''' 
Compléments hors programme pour l'enseignant 
Ci dessous des versions expertes ou récursives des fonctions apparaissant dans les activités 
'''

def tab_val_2(f): 
    return [f(2*k) for k in range(10)]

def tab_val_bis_2(f,x_0,p,n):
    return [f(x_0+k*p) for k in range(n)]
    
def cdir_secantes_2(f,x_0,p,n):
    return [coeff_dir(x_0+k*p,f(x_0+k*p),x_0,f(x_0)) for k in range(1,n+1)]
    
#ou    

def cdir_secantes2_2(f,x_0,p,n):
    return [taux_variation(f,x_0,k*p) for k in range(1,n+1)]
    
def appl_Newton_2(f,a,n):  
    return [] if n<0 else [a]+appl_Newton_2(f,etap_Newton(f,a),n-1)

def etap_dichoto_2(f,a,b):
    m=(a+b)/2
    return (a,m) if f(a)*f(m)<0 else (m,b)
    
def dichoto_iter_2(f,a,b,n):
    return (a,b) if n==0 else dichoto_iter_2(f,*etap_dichoto_2(f,a,b),n-1)
    
def dichoto_test_2(f,a,b,h):
    return (a,b) if b-a<=h else dichoto_test_2(f,*etap_dichoto_2(f,a,b),h)
    
  
   
