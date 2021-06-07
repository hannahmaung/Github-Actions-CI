

import unittest 
import example


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(example.add(1, 2), 3)
        
    def test_sub(self):
        self.assertEqual(example.subtract(10, 5), 5)    

    def test_mult(self):
        self.assertEqual(example.multiply(1, 2), 2)

    def test_div(self):
        self.assertEqual(example.divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()