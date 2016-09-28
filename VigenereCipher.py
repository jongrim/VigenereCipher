#! python
import re
import string
import sys


def get_digit_from_alpha(alpha):
    vig_dig_dict = {}
    position = 0

    for letter in string.ascii_lowercase:
        vig_dig_dict[letter] = position
        position += 1

    return vig_dig_dict[alpha]


def get_alpha_from_dig(digit):
    vig_alpha_dict = {}

    for number in range(26):
        vig_alpha_dict[number] = string.ascii_lowercase[number]

    return vig_alpha_dict[digit]


def vigenere_encrypt():
    plaintext = input('Please enter the plaintext you would like to encrypt\n').lower()
    key = input('Please enter the key you would like to use\n').lower()

    plaintext = re.sub(r'\d+', '', plaintext)
    key = re.sub(r'\d+', '', key)
    ciphertext = []
    key_position = 0

    for letter in plaintext:
        if letter.isalpha():
            ciphertext.append(get_alpha_from_dig((get_digit_from_alpha(letter) +
                                                  get_digit_from_alpha(key[key_position % len(key)])) % 26))
            key_position += 1
        elif letter.isspace():
            ciphertext.append(letter)

    print(''.join(ciphertext))

    sys.exit(0)


def vigenere_decrypt():
    ciphertext = input('Please enter the ciphertext to decrypt\n').lower()
    key = input('Please enter the key to decrypt with\n').lower()

    key_position = 0
    plaintext = []

    for letter in ciphertext:
        if letter.isalpha():
            plaintext.append(get_alpha_from_dig((get_digit_from_alpha(letter) -
                                                 get_digit_from_alpha(key[key_position % len(key)])) % 26))
            key_position += 1
        elif letter.isspace():
            plaintext.append(letter)

    print(''.join(plaintext))

    sys.exit(0)


def main():
    operations = {0: vigenere_encrypt, 1: vigenere_decrypt}

    operation = None
    while operation is None:
        operation = int(input("""Please select what operation you would like to perform:
      [0] Encryption via Vigenere cipher
      [1] Decryption via Vigenere cipher
      """))
        if operation not in operations:
            print('Sorry, that action is not allowed')
            operation = None

    operations[operation]()

# TODO add the ability for command line arguments - encrypt or decrypt
# TODO add the ability to read the message and key from file
# TODO add the ability to write the ciphertext or plaintext to file

if __name__ == '__main__':
    main()
