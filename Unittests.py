#! python
import unittest

from VigenereCipher import VigenereMachine


class TestVigenereMachine(unittest.TestCase):

    def test_get_encrypted_letter(self):
        vm = VigenereMachine(plaintext='aaa', cipher_key='abc')
        result = vm.get_encrypted_letter(0, 'a')
        self.assertEqual(result, 'a')
        result = vm.get_encrypted_letter(1, 'a')
        self.assertEqual(result, 'b')
        result = vm.get_encrypted_letter(1, 'b')
        self.assertEqual(result, 'c')
        result = vm.get_encrypted_letter(2, 'z')
        self.assertEqual(result, 'b')

    def test_get_decrypted_letter(self):
        vm = VigenereMachine(cipher_key='abc', ciphertext='aaa')
        result = vm.get_decrypted_letter(key_position=0, letter='a')
        self.assertEqual(result, 'a')
        result = vm.get_decrypted_letter(key_position=1, letter='b')
        self.assertEqual(result, 'a')
        result = vm.get_decrypted_letter(key_position=2, letter='z')
        self.assertEqual(result, 'x')
        result = vm.get_decrypted_letter(key_position=2, letter='a')
        self.assertEqual(result, 'y')

    def test_encrypt(self):
        vm = VigenereMachine(plaintext='test', cipher_key='abc')
        self.assertEqual('tfut', vm.encrypt())
        vm = VigenereMachine(plaintext='te st', cipher_key='abc')
        self.assertEqual('tf ut', vm.encrypt())

    def test_decrypt(self):
        vm = VigenereMachine(ciphertext='tfut', cipher_key='abc')
        self.assertEqual('test', vm.decrypt())
        vm = VigenereMachine(ciphertext='tf ut', cipher_key='abc')
        self.assertEqual('te st', vm.decrypt())