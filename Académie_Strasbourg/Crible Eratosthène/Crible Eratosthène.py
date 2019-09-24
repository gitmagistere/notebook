'''
Formation Python 
Lycee Français de Prague
2019 - Franck CHEVRIER

Crible d'Eratosthene
'''

def Crible_Eratosthene(N=100):
    '''
    Fonction qui realise le crible d'Eratosthene
    '''
    #On dispose de la liste des nombres entiers de 0 a N
    L=[k for k in range(N+1)]
    
    #Barrer 0 (déjà fait) et 1
    L[1]=0
    
    #Parcourir dans l'ordre tous les entiers k de 2 a N
    for k in range(2,N+1):
        
        #Si le nombre k n'est pas barré:
        if L[k]!=0:
            
            #Barrer tous les multiples stricts de k dans la liste
            for j in range(2*k,N+1,k):
                L[j]=0
                
    #Renvoyer la liste des nombres qui ont ete entoures (cad premiers)
    return [ L[k] for k in range(N+1) if L[k]!=0 ]


from math import log #logarithme neperien

def Comparaison(N):
    '''
    Fonction qui renvoie la frequence d'apparition
    des nombres premier inferieurs à N et 1/ln(N)
    '''
    return len(Crible_Eratosthene(N))/N,1/log(N)




