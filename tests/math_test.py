import unittest
import mtm

class MainTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mtm.add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(mtm.subtract(1, 1), 0)

if __name__ == '__main__':
    unittest.main()