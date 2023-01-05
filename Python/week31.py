"""
 * Challenge #31
 * LEAP YEARS
 * Difficulty: EASY
 *
 * Statement: Create a function that prints the next 30 leap years following a given one.
 * - Use the least number of lines to solve the exercise.
 *
"""


def leap_year(year: int) -> bool:
    return year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)


def generate_years(base_year = 2023, show_all=True):
    if show_all:
        print("The next 30 years will be:")
        for year in range(base_year, base_year + 31):
            print(f"{year}: {'Leap year' if leap_year(year) else 'Not leap year'}")
    else:
        print("Leap years:")
        for year in range(base_year, base_year + 31):
            if leap_year(year):
                print(year, end="\t")


# generate_years(show_all=False)
# generate_years()
generate_years(base_year=1997)
