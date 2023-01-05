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
YEAR = 1924

def get_sexagenarian(year: int):

