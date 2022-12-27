""""
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
"""


def balance_check(a: str, b: str):
    return form_list.count(a) == form_list.count(b)


form = input("Insert the equation: ")
form_list = [n for n in form]
for a, b in zip(['(', '{', '['], [')', '}', ']']):
    if not balance_check(a, b):
        print(f"There was an error on {a}{b}")
        break
