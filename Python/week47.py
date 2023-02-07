"""
Most common vowel
"""

phrase = input("Enter the phrase to analyze:\n").lower()

vowel_dict = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

for letter in phrase:
    if letter in ['a', 'á', 'à', 'â']:
        vowel_dict['a'] += 1
    elif letter in ['e', 'è', 'é', 'ê']:
        vowel_dict['e'] += 1
    elif letter in ['i', 'í', 'ì', 'î']:
        vowel_dict['i'] += 1
    elif letter in ['o', 'ó', 'ò', 'ô']:
        vowel_dict['o'] += 1
    elif letter in ['u', 'ú', 'ù', 'û']:
        vowel_dict['u'] += 1

print("Result:")
print(vowel_dict)
