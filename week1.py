"""
* ¿ES UN ANAGRAMA?
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
"""
palabra1 = input("Ingrese primera palabra: ").lower()
palabra2 = input("Ingrese segunda palabra: ").lower()

if palabra1 == palabra2:
    print("Ambas palabras son iguales")
    exit(1)

letter_count = {}
for letter in palabra1:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

for letter in letter_count.keys():
    if palabra2.count(letter) != letter_count[letter]:
        print("Son distintos")
        exit(1)
print("Son anagramas")
