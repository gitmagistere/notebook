#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

def Superposition(I,M,Opacite):
    Meff=int(255*(1-Opacite)+M*Opacite)
    E=int(I/255*(I+2*Meff/255*(255-I)))
    return(E)
    
def Multiplier(I,M,Opacite):
    Meff=int(255*(1-Opacite)+M*Opacite)
    E=int(I*Meff/255)
    return(E)
  
Filtres=[(255,0,0),(0,255,0),(0,0,255)]
img=Image.open("Criquet.JPG")
nbColonne,nbLigne=img.size
if nbColonne>800:
    img_petit=img.resize((800,int(nbLigne*800/nbColonne)))
    img=img_petit
    nbColonne,nbLigne=img.size
pixelFiltre=(0,255,255)
imgFiltree=Image.new(img.mode,img.size)
for numeroLigne in range(nbLigne):
    for numeroColonne in range(nbColonne):
        pixelImage=img.getpixel((numeroColonne,numeroLigne))
        pixelImageFiltre=(Multiplier(pixelImage[0],pixelFiltre[0],0.75),Multiplier(pixelImage[1],pixelFiltre[2],0.75),Multiplier(pixelImage[2],pixelFiltre[2],0.75))
        imgFiltree.putpixel((numeroColonne,numeroLigne),pixelImageFiltre)
imgResultat=imgFiltree.convert("L")
imgResultat.save("Criquet_Cyan_NB.jpg")
img.close()