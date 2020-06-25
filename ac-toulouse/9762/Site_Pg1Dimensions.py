from PIL import Image
img = Image.open("sernin.jpg")
largeur, hauteur = img.size
print("largeur de l'image :", largeur, "pixels")
print("hauteur de l'image :", hauteur, "pixels")

