# Créé par Cilvaringz, le 01/02/2021 en Python 3.7

#1-------------------------------GEOMETRIE----------------------------------------------------------------------

#Fonction renvoyant le volume d'une boule------------------------------------------------------------------------
def volume_boule(r):
    from math import pi
    resultat=(4*pi*r**3)/3
    return resultat

#Test fonction
a=volume_boule(10)
print(a)
#-----------------------------------------------------------------------------------------------------------------

#Fonction renvoyant la longueur du côté d'un carré d'aire A------------------------------------------------------
def cote_carre(A):
    from math import sqrt #Importer la fonction renvoyant la racine carré d'un nombre
    resultat = sqrt(A)
    return resultat

#Test fonction
print(cote_carre(100))
#-------------------------------------------------------------------------------

#Fonction renvoyant le diamètre d'un cylindre connaissant la hauteur h et le volume V-------------------------------
def diametre_cylindre(h,V):
    from math import pi
    from math import sqrt
    r=sqrt(V/(pi*h))
    resultat = 2*r
    return resultat

#Test fonction
print(diametre_cylindre(3,5))
#-------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------2-CALCULS COMMERCIAUX----------------------------------------------

#Programme calculant le montant d'interet simple--------------------------------------------------------------------
def interet_simple():
    C0=float(input("Capital placé: "))
    t=float(input("Taux annuel des intéret en %: "))
    n=int(input("Période du placement en jours: "))

    I=round(C0*(t/100)*n,2)
    print("Un capital de", C0,"€ placé pendant", n,"jours au taux annuel de", t, "%, produit",I,"€ d'intérêts")
    return I
#interet_simple()

#-------------------------------------------------------------------------------------------------------------------

#Programme calculant le montant net---------------------------------------------------------------------------------
def montan_net(PBHT,remise):
    PNHT = PBHT*((100-remise)/100)
    return PNHT

print(montan_net(200,10))
#-------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------3-FONCTIONS -----------------------------------------------------
#Equation réduite d'une droite non // à l'axe des ordonnées
def equation_droite():

    xA,yA=eval(input("Entrer les coordonnées du point A : xA,yA"))
    xB,yB=eval(input("Entrer les coordonnées du point B tel que xB>xA"))

    #Détermination du coéficient a
    a=(yB-yA)/(xB-xA)

    #Détermination du coéficient b
    b=yB-a*xB

    #equation de la droite
    return "Equation de la droite passant par A et B : y="+str(a)+"x + "+str(b)

#print(equation_droite())

#-------------------------------------------------4-PROBLEME DU PREMIER DEGRE---------------------------------------

#Prix en fonction des km--------------------------------------------------------------------------------------------
def prix(x):
    y=0.05*x+21
    return y

print(prix(10))
#-------------------------------------------------------------------------------------------------------------------


#km en fonction du prix---------------------------------------------------------------------------------------------
def nb_km(y):
    x=(y-21)/0.05
    return x

print(nb_km(21.5))
