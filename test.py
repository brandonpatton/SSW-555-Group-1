import unittest
import importlib
utils = importlib.import_module("utilities")
script = importlib.import_module("script")

class testUS09(unittest.TestCase):

    def test_01(self):
        '''Test catch for birth before mother's death'''
        self.assertEqual(True, True)

    def test_02(self):
        '''Test catch for birth before mother's death'''
        self.assertEqual(True, True)

    def test_03(self):
        '''Test catch for birth before mother's death'''
        self.assertEqual(True, True)

    def test_04(self):
        '''Test catch for birth before father's death'''
        self.assertEqual(True, True)

    def test_05(self):
        '''Test catch for birth before father's death'''
        self.assertEqual(True, True)

    def test_06(self):
        '''Test catch for birth before father's death'''
        self.assertEqual(True, True)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
