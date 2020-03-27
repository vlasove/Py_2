import unittest
import func

class TestFuncMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(func.add(2,3), 5)
        self.assertEqual(func.add(-2,2), 0)
        


if __name__ == '__main__':
    unittest.main()