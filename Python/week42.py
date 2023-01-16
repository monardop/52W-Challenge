"""
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
"""


def valid_input():
    while True:
        entry = input("Set the temperature with format XXºC/XXºF:  ")
        if "ºF" in entry or "ºC" in entry:
            if "ºF" in entry:
                try:
                    entry = entry.replace("ºF", "")
                    entry = float(entry)
                except ValueError:
                    print("Invalid input")
                else:
                    print(f"{round(get_func(entry, 'F'),2)}ºC")
                    exit(1)
            elif "ºC" in entry:
                try:
                    entry = entry.replace("ºC", "")
                    entry = float(entry)
                except ValueError:
                    print("Invalid input")
                else:
                    print(f"{round(get_func(entry, 'C'), 3)}ºF")
                    exit(1)
        else:
            print("Please put ºF or ºC to indicate which unity are you using")


def fahrenheit_to_celcius(temperature: float) -> float:
    return temperature * 1.8 + 32


def celius_to_fahrenheit(temperature: float) -> float:
    return (temperature - 32) / 1.8


def get_func(temperature: float, degree: str) -> float:
    if degree == 'F':
        return fahrenheit_to_celcius(temperature)
    else:
        return celius_to_fahrenheit(temperature)


valid_input()
