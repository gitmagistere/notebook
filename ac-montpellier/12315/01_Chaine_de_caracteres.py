# Tentative Bernard Werber

#Objectif du travail. Je souhaite:
                                    # 1) parcourir un texte
                                    # 2) stocker la position du mot "veux"
                                    # 3) afficher la position du mot "veux"

#---------Déclaration des variables globales----------#

texte = "Entre Ce que je pense Ce que je veux dire Ce que je crois dire Ce que je dis Ce que vous avez envie d'entendre Ce que vous croyez entendre Ce que vous entendez Ce que vous avez envie de comprendre Ce que vous croyez comprendre Ce que vous comprenez Il y a dix possibilités qu'on ait des difficultés à communiquer. Mais essayons quand même..."

position_depart = 0 # la position de départ dans la chaine de caractère vaut 0
position_veux = 0 # la position du mot "veux" dans la chaine de caractère ( 0 au démarrage du programme)

#-----------instructions traitement de la chaine de caractères--------------# 


# tant que la position de départ est inférieure à la longeur du texte -4 (nombre de caractères du mot veux) alors je parcours la chaine.
while position_depart < len(texte)-3:

    
    if texte[position_depart:position_depart+4] == "veux": # si dans le texte ma position depart + 4 caractères est strictement égale à veux
        position_veux = position_depart # alors je stocke la position_veux qui dans ce cas là est la position_depart
        break #je stoppe la boucle

    # sinon je me décale de 1 caractère sur la chaine car je n'ai pas trouvé le mot veux.
    position_depart += 1
    #print("je suis décalé de 1")
    

print("la position de \"veux\" est")
print (position_veux)


#Voici une séquence d'ARNm : UAACGGAAUGUUCAUAUGCCCAAUGAUUUAGUU
#Objectif du travail. Je souhaite:
                                    # 1) parcourir la séquence d'ARNm
                                    # 2) stocker la position du codon initiateur "AUG"
                                    # 3) afficher la position du codon initiateur "AUG"
