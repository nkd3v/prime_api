import unittest

from app import app

class AppTestCase(unittest.TestCase):
    def test_plus_negative(self):
        res = app.plus(-1, -1)
    
    def test_plus_positive(self):
        res = app.plus(1, 1)
    
    def test_plus_fraction(self):
        res = app.plus(1.1, 1.1)

if __name__ == "__main__":
    unittest.main()
