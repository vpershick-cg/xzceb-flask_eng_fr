import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        '''Test for null input for english_to_french.'''
        self.assertEqual(english_to_french(null), '') # null input should return ''
        '''Test for the translation of the world ‘Hello’ and ‘Bonjour’.'''
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # Hello should translate to Bonjour 
        
class TestF2E(unittest.TestCase): 
    '''
    Test for null input for french_to_english
    Test for the translation of the world ‘Bonjour’ and ‘Hello’.
    '''
    def test1(self): 
        self.assertEqual(french_to_english(null), '') # null input should return ''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # Bonjour should translate to Hello 
        