import unittest
from polynome.polynome import Polynome

class PolynomeTestCase(unittest.TestCase):
    def test_init_1_2_valid(self):
        # Arrange
        p = Polynome([1, 2])
        #Act
        #Assert
        self.assertIsNotNone(p)

    def test_init_clean_list_exception_dont_exist_polynome(self):
        # Arrange
        # Act
        with self.assertRaises(Exception) as context:
            p = Polynome([])
        # Assert
        self.assertTrue('Polynome don\'t exist without coefficients.' in str(context.exception))

    def test_str_5_5polynome(self):
        # Arrange
        p = Polynome([5])
        # Act
        s = str(p)
        # Assert
        self.assertEqual(s, '5')

    def test_str_deg_zero_zero_coef_polynome(self):
        # Arrange
        p = Polynome([0])
        # Act
        s = str(p)
        # Assert
        self.assertEqual(s, '0')

    def test_str_deg5_high_degree_polynome(self):
        # Arrange
        p = Polynome([5, 0, 0, 0])
        # Act
        s = str(p)
        # Assert
        self.assertEqual(s, '5x^3')

    def test_str_high_degree_polynome(self):
        # Arrange
        p = Polynome([5, 0, 2, -6])
        # Act
        s = str(p)
        # Assert
        self.assertEqual(s, '5x^3+2x^1-6')

    def test_str_deg5_notnull_coef_polynome(self):
        # Arrange
        p = Polynome([6, -9, 2, -2])
        # Act
        s = str(p)
        # Assert
        self.assertEqual(s, '6x^3-9x^2+2x^1-2')

    def test_eq_deg2_deg2_True(self):
        # Arrange
        first = Polynome([3, 2, -1])
        second = Polynome([3, 2, -1])
        # Act
        eq = first.__eq__(second)
        # Assert
        self.assertTrue(eq)

    def test_eq_deg3_deg2_False(self):
        # Arrange
        first = Polynome([4, 3, 2, -1])
        second = Polynome([3, 2, -1])
        # Act
        eq = first.__eq__(second)
        # Assert
        self.assertFalse(eq)

    def test_eq_deg2_deg2_other_coeff_False(self):
        # Arrange
        first = Polynome([-3, -2, -1])
        second = Polynome([3, 2, -1])
        # Act
        eq = first.__eq__(second)
        # Assert
        self.assertFalse(eq)


    def test_eq_deg2_string_exception_other_isnt_polynom(self):
        # Arrange
        first = Polynome([-3, -2, -1])
        second = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = first.__eq__(second)
        # Assert
        self.assertTrue('Other isn\'t polynome.' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
