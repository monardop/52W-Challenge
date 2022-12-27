"""
/*
 * Reto #5
 * ASPECT RATIO DE UNA IMAGEN
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.

"""

import requests
import cv2

url_imagen = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

imagen = requests.get(url_imagen).content

with open("imagen.jpg","wb") as f:
    f.write(imagen)

img = cv2.imread("imagen.jpg")
wid = img.shape[1]
hgt = img.shape[0]

ratio = round(wid/hgt, 2)

if ratio == 1.78:
    print("The ratio is 16:9")
elif ratio == 1.33:
    print("The ratio is 4:3")
elif ratio == 1:
    print("The ratio is 1:1 (square)")
else: 
    print("Unknown ratio")
