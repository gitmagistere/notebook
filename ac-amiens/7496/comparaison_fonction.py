from lycee import *

#création de la fonction f(x)=2x²+3
def f(x):
    return 2*x**2+3

#création de la fonction g(x)=2x²+3
def g(x):
    return 8*x+45

# Utilisation des fonctions pour afficher les images de f et g pour x de 0 à 10 avec un pas de 1
# et les comparer les valeurs
for i in range (0,11,1):
    print("f(",i,") = ",f(i)," et  g(",i,") = ",g(i))
    if f(i)>g(i):
        print ("f(",i,") > g(",i,")")
    if f(i)<g(i):
        print ("f(",i,") < g(",i,")")
    if f(i)==g(i):
        print ("f(",i,") = g(",i,")")


