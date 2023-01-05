"""
 * Challenge #33
 * CHINESE SEXAGENARIAN CYCLE
 * Difficulty: MEDIUM

 * Statement: Create a function, that given a year, indicates the corresponding element and animal
 * in the sexagenarian cycle of the Chinese zodiac.
 * - Information: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - The sexagenarian cycle corresponds to the combination of the elements wood,
 * fire, earth, metal, water and the animals rat, ox, tiger, rabbit, dragon, snake,
 * horse, sheep, monkey, rooster, dog, pig (in this order).
 * Each element is repeated two years in succession.
 * - The last sexagenarian cycle began in 1984 (Wood Rat).
"""

ELEMENT = ('Wood', 'Fire', 'Earth', 'Metal', 'Water')
ANIMAL = ('Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig')


def get_sexagenarian(year: int) -> int:
    base_year = 1924
    sexagenarian = 1
    while True:
        if base_year <= year <= base_year + 60:
            return base_year, sexagenarian
        else:
            base_year += 60
            sexagenarian += 1


def get_animal_element(year: int) -> tuple:
    animal: str = ANIMAL[year % len(ANIMAL)]
    element: str = ELEMENT[year % len(ELEMENT)]
    return animal, element


def main():
    year = int(input("Year: "))
    sexagenarian = get_sexagenarian(year)
    pair = get_animal_element(abs(year - sexagenarian[0]))
    print(f"The year {year} is {pair[0]} - {pair[1]}")
    print(f"It belong to the {sexagenarian[1]} sexagenarian, that starts in {sexagenarian[0]} "
          f"and ends on {sexagenarian[0] + 60} ")


if __name__ == '__main__':
    main()
