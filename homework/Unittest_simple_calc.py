import unittest
import test_simple_calc


class TestCase(unittest.TestCase):
    def test_add_func(self):
        self.assertEqual(test_simple_calc.add(5, 2), 7)
        self.assertEqual(test_simple_calc.add(2.5, 7.5), 10)
        self.assertEqual(test_simple_calc.add(-10, 10), 0)

    def test_substract_func(self):
        self.assertEqual(test_simple_calc.subtract(5, 3), 2)
        self.assertEqual(test_simple_calc.subtract(2.1, 1.1), 1.0)
        self.assertEqual(test_simple_calc.subtract(-10, 100), -110)

    def test_multiply_func(self):
        self.assertEqual(test_simple_calc.multiply(1, 10), 10)
        self.assertEqual(test_simple_calc.multiply(-5, 5), -25)
        self.assertEqual(test_simple_calc.multiply(2.3, 5.6), 12.879999999999999)

    def test_devide_func(self):
        self.assertEqual(test_simple_calc.divide(2, 2), 1)
        self.assertEqual(test_simple_calc.divide(x=7, y=2), 3.5)
        with self.assertRaises(ValueError):
            test_simple_calc.divide(5, 0)
        self.assertRaises(ValueError, lambda: test_simple_calc.divide(3, 0))


if __name__ == '__main__':
    unittest.main()

