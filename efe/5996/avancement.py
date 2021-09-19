print("équation de réaction I2 + 2 S2O32 -> 2 I-  + + S4O62-")

print("entrer les quantités de matières initiales")
n0diiode=float(input ("n0diidode= (en mol) "))
n0thio=float(input ("n0thiosulfate= (en mol)"))
xmax1=n0diiode
xmax2=n0thio/2
if xmax1==xmax2:
    print("les proportions sont stoechiométriques")
    xmax=xmax1
elif xmax1<xmax2:
    print("le diiode est le réactif limitant")
    xmax=xmax1
else:
    print("le thiosulfate  est le réactif limitant")
    xmax=xmax2

print("la valeur de l'avancement maximale est ",xmax, "mol")
print("à l’état final, la quantité d’ions iodure est de ", 2*xmax, "mol\n")
print("à l’état final, la quantité d’ions S4O62- est de ", xmax, "mol")

