"""
 * Reto #15
 * ¿CUÁNTOS DÍAS?
 * Dificultad: DIFÍCIL

 * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""


class Constructor:
    def __init__(self):
        self.day, self.month, self.year = self.valid_date()

    @staticmethod
    def leap_year(year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0

    def valid_date(self) -> tuple:
        normal_days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        leap_days = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        while True:
            print("The year must be after 1601")
            date = input("Insert date in format dd/mm/yyyy: ")
            try:
                day, month, year = date.split('/')
                if int(year) < 1601:
                    print("Wrong year")
                    raise ValueError
                if int(month) > 13 or int(month) < 1:
                    print('Wrong month')
                    raise ValueError
                if self.leap_year(int(year)):
                    if int(day) > leap_days[int(month)] or int(day) < 1:
                        print("Wrong number of day")
                        raise ValueError
                else:
                    if int(day) > normal_days[int(month)] or int(day) < 1:
                        print("Wrong number of day")
                        raise ValueError
            except ValueError:
                print("Try again")
            else:
                return int(day), int(month), int(year)


class Date(Constructor):

    def __init__(self):
        super().__init__()
        self.relative_days: int = self.get_relative_days()

    def get_relative_days(self):
        normal_days = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
        leap_days = (0, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335)
        year_dif = self.year - 1601
        rel_days = (year_dif * 365
                    - year_dif // 4
                    - year_dif // 100
                    + year_dif // 400)
        days_this_year = leap_days[self.month] if self.leap_year(self.year) else normal_days[self.month]
        return rel_days + self.day + days_this_year

    def __sub__(self, other) -> int:
        return abs(self.relative_days - other.relative_days)

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}, {'leap year' if self.leap_year(self.year) else 'not leap'}"


date1 = Date()
print(date1)
date2 = Date()
print(date2)
print(date1 - date2)
