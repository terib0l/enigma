import unittest
import logging

from main import main as enigma
from log import logger

class EnigmaTest(unittest.TestCase):

    def test_input_not_equal_encrypt(self):
        text = "ABCD"
        self.assertTrue(enigma(text)[0] != text)

    def test_input_equal_decrypt(self):
        text = "ABCD"
        self.assertTrue(enigma(text)[1] == text)

if __name__ == "__main__":
    logger.setLevel(logging.WARNING)
    unittest.main()
