"""
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""

morse_code = {
    'A': '· —',
    'B': '— · · ·	',
    'C': '	— · — ·',
    'CH': '— — — —',
    'D': '— · ·',
    'E': '·',
    'F': '· · — ·',
    'G': '- - ·',
    'H': '· · · ·',
    'I': '· ·',
    'J': '· - - -',
    'K': '- · -',
    'L': '· - · ·',
    'M': '- -',
    'N': '- ·',
    'Ñ': '- - · - -',
    'O': '- - -',
    'P': '· - - ·',
    'Q': '- - · -',
    'R': '· - ·',
    'S': '· · ·',
    'T': '-',
    'U': '· · -',
    'V': '· · · -',
    'W': '· - -',
    'X': '- · · -',
    'Y': '- · - - ',
    'Z': '- - · ·',
    '0': '- - -',
    '1': '· - - - -',
    '2': '· · - - -',
    '3': '· · · - -',
    '4': '· · · · -',
    '5': '· · · · ·',
    '6': '- · · · ·',
    '7': '- - · · ·',
    '8': '- - - · ·',
    '9': '- - - - ·',
    '.': '· - · - · -',
    ',': '- - · · - -',
    '?': '· · - - · ·'
}

phrase = input("Insert a message: ")
phrase = phrase.upper()
morse_msg = ""
for n in phrase:
    if n == " ":
        morse_msg += "  "
    else:
        morse_msg += morse_code[n]
print(morse_msg)

