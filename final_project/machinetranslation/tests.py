import unittest

#from translator import englishToFrench,frenchToEnglish

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(englishToFrench('Beauty'),'Monde')

class TestF2E(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchToEnglish('Monde'),'Beauty')

unittest.main()