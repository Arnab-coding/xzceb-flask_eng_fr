import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        # Test for null input
        self.assertEqual(englishToFrench(None), None)
        # Test for translation of 'Hello'
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        # Test for null input
        self.assertEqual(frenchToEnglish(None), None)
        # Test for translation of 'Bonjour'
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

print('OK')        