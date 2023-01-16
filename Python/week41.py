"""
 * Enunciado: Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".
"""


def ohm_law(voltage=0, current=0, resistance=0):
    if voltage == current == 0 or current == resistance == 0 or resistance == voltage == 0:
        return "Error"
    elif voltage != 0 and current != 0 and resistance != 0:
        return "Error"

    if voltage == 0:
        return f"{round(current*resistance, 2)} V"
    elif current == 0:
        return f"{round(voltage / resistance, 2)} A"
    else:
        return f"{round(voltage / current, 2)} ohms"


print(ohm_law())  # error
print(ohm_law(1, 2, 4))  # error
print(ohm_law(1, 2))
print(ohm_law(0, 1, 6))
print(ohm_law(3, 0, 8))

