import unittest
from polynome.polynome import Polynome

class PolynomeTestCase(unittest.TestCase):
    def test_init_1_2_valid(self):
        p = Polynome([1, 2])
        self.assertIsNotNone(p)

    def test_init_clean_list_exception_dont_exist_polynome(self):
        with self.assertRaises(Exception) as context:
            p = Polynome([])
        self.assertTrue('Polynome don\'t exist without coefficients.' in str(context.exception))

    def test_str_5_5polynome(self):
        p = Polynome([5])
        self.assertEqual(str(p), '5')

    def test_str_deg_zero_zero_coef_polynome(self):
        p = Polynome([0])
        self.assertEqual(str(p), '0')

    def test_str_deg5_high_degree_polynome(self):
        p = Polynome([5, 0, 0, 0])
        self.assertEqual(str(p), '5x^3')

    def test_str_high_degree_polynome(self):
        p = Polynome([5, 0, 2, -6])
        self.assertEqual(str(p), '5x^3+2x^1-6')

    def test_str_deg5_notnull_coef_polynome(self):
        p = Polynome([6, -9, 2, -2])
        self.assertEqual(str(p), '6x^3-9x^2+2x^1-2')



if __name__ == '__main__':
    unittest.main()
