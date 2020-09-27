import unittest
import importlib
script = importlib.import_module("script")

class TestStringMethods(unittest.TestCase):

    def testFunction(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()