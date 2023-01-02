"""
* CONVERSOR TIEMPO
 * Fecha publicación enunciado: 09/05/22
 * Fecha publicación resolución: 16/05/22
 * Dificultad: FACIL
 *
 * Enunciado: Crea una función que reciba días, horas, minutos y segundos
    (como enteros) y retorne su resultado en milisegundos.
"""
ans = []
for n in ['days', 'hours', 'minutes', 'seconds']:
    while True:
        try:
            value = int(input(f"Number of {n}: "))
            if value < 0:
                raise ValueError
            if (n == 'minutes' or n == 'seconds') and (value < 0 or value > 59):
                raise ValueError
        except ValueError:
            print("Wrong input")
        else:
            ans.append(value)
            break

final = (((ans[0]*24 + ans[1])
          * 60 + ans[2])
         * 60 + ans[3])

print(final * 1000)
