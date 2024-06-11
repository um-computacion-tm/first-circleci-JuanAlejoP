import unittest
from main import addition

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 2), 4)

if __name__ == '__main__':
    unittest.main()