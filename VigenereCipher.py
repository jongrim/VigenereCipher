#! python
import re
import string


class VigenereMachine:
    num_dict = {num: alpha for num, alpha in enumerate(string.ascii_lowercase)}
    alpha_dict = {alpha: num for num, alpha in enumerate(string.ascii_lowercase)}

    def __init__(self, plaintext=None, cipher_key=None, ciphertext=None):
        if plaintext:
            self._plaintext = plaintext.lower()
        if cipher_key:
            if not cipher_key.isalpha():
                raise ValueError('The key may only contain alphabetic characters')
            else:
                self._cipher_key = cipher_key.lower()
        if ciphertext:
            self._ciphertext = ciphertext.lower()

    @property
    def plaintext(self):
        return self._plaintext

    @plaintext.setter
    def plaintext(self, new_text):
        self._plaintext = new_text.lower()

    @property
    def cipher_key(self):
        return self._cipher_key

    @cipher_key.setter
    def cipher_key(self, new_key):
        if not new_key.isalpha():
            raise ValueError('The key may only contain alphabetic characters')
        else:
            self._cipher_key = new_key.lower()

    @property
    def ciphertext(self):
        return self._ciphertext

    @ciphertext.setter
    def ciphertext(self, new_text):
        self._ciphertext = new_text.lower()

    def encrypt(self):
        self._ciphertext = []
        key_position = 0
        for letter in self._plaintext:
            if letter.isalpha():
                self._ciphertext.append(self.get_encrypted_letter(key_position, letter))
                key_position += 1
            else:
                self._ciphertext.append(letter)
        self._ciphertext = ''.join(self._ciphertext)
        return self._ciphertext

    def decrypt(self):
        self._plaintext = []
        key_position = 0
        for letter in self._ciphertext:
            if letter.isalpha():
                self._plaintext.append(self.get_decrypted_letter(key_position, letter))
                key_position += 1
            else:
                self._plaintext.append(letter)
        self._plaintext = ''.join(self._plaintext)
        return self._plaintext

    def get_encrypted_letter(self, key_position, letter):
        return VigenereMachine.num_dict[
            (self.alpha_dict[letter] + self.alpha_dict[self._cipher_key[key_position % len(self._cipher_key)]]) % 26]

    def get_decrypted_letter(self, key_position, letter):
        return VigenereMachine.num_dict[
            (self.alpha_dict[letter] - self.alpha_dict[self._cipher_key[key_position % len(self._cipher_key)]]) % 26]
