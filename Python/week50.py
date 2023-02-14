"""
'Karaca' algorithm.
"""


def encrypt_msg(text: str) -> str:
    """
    This is a basic encrypt algo
    :param text: msg to encrypt
    :return: encrypted msg
    """
    for number in ['0', '1', '2', '3', '4']:
        if number in text:
            return "Your msg will be corrupted."

    new_text = text[::-1]
    for letter, num in zip(['a', 'e', 'i', 'o', 'u'], ['0', '1', '2', '3', '4']):
        new_text.replace(letter, num)
    new_text += 'aca'

    return new_text.lower()


def decrypt_msg(text: str) -> str:
    """
    Uses Karaca decrypt method
    :param text: encrypted msg
    :return: decrypted msg
    """
    if text.endswith('aca') is False:
        return "Not encrypted"
    new_text = text.replace('aca', '')
    new_text = new_text[::-1]
    for letter, num in zip(['a', 'e', 'i', 'o', 'u'], ['0', '1', '2', '3', '4']):
        new_text.replace(num, letter)
    return new_text


def menu() -> int:
    """
    Gets a valid option from the user
    :return: option selected by the user
    """
    while True:
        try:
            option = int(input('1 - Encrypt\n2 - decrypt\nChoose: '))
            if option not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Incorrect input")
        else:
            return option


selection = menu()
if selection == 1:
    print(encrypt_msg(input('Insert a msg: ')))
else:
    print(decrypt_msg(input('Insert a msg: ')))
