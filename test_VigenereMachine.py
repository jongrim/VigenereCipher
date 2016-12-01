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
        # Test handling special characters in the plaintext
        vm.plaintext = 'te st,12'
        self.assertEqual('tf ut,12', vm.encrypt())
        # Test handling a key with uppercase characters
        vm.plaintext, vm.cipher_key = 'test', 'Abc'
        self.assertEqual('tfut', vm.encrypt())
        # Test handling plaintext with uppercase characters
        vm.plaintext, vm.cipher_key = 'TEST', 'abc'
        self.assertEqual('tfut', vm.encrypt())

    def test_decrypt(self):
        vm = VigenereMachine(ciphertext='tfut', cipher_key='abc')
        self.assertEqual('test', vm.decrypt())
        # Test handling special characters in the ciphertext
        vm.ciphertext = 'tf ut,12'
        self.assertEqual('te st,12', vm.decrypt())
        # Test handling a key with uppercase characters
        vm.ciphertext, vm.cipher_key = 'tfut', 'ABC'
        self.assertEqual('test', vm.decrypt())
        # Test handling uppercase characters in the ciphertext
        vm.ciphertext = 'TFUT'
        self.assertEqual('test', vm.decrypt())

    def test_cipher_key(self):
        with self.assertRaises(ValueError) as cm:
            vm = VigenereMachine()
            vm.cipher_key = '@hello'
        self.assertIsInstance(cm.exception, ValueError)
        self.assertEqual(cm.exception.args, ('The key may only contain alphabetic characters', ))
