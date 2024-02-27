import unittest

from app import app

class AppTestCase(unittest.TestCase):
    def test_when_x_is_17(self):
        res = app.is_prime(7)
        self.assertEqual(res, "true")
        
    def test_when_x_is_36(self):
        res = app.is_prime(36)
        self.assertEqual(res, "false")
        
    def test_when_x_is_13219(self):
        res = app.is_prime(13219)
        self.assertEqual(res, "true")
        

if __name__ == "__main__":
    unittest.main()
