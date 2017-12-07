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
        first = Polynome([-3, -2, -91])
        second = Polynome([3, 2, -1])
        # Act
        eq = first.__eq__(second)
        # Assert
        self.assertFalse(eq)

    def test_eq_deg2_deg2_other_coeffs_False(self):
        # Arrange
        first = Polynome([3, -2, -1])
        second = Polynome([13, 2, 1])
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

    def test_add_deg2_deg2_2polynome(self):
        # Arrange
        first = Polynome([-3, -2, -1])
        second = Polynome([8, 5, -2])
        # Act
        eq = first + second
        # Assert
        self.assertEqual(str(eq), '5x^2+3x^1-3')

    def test_add_deg2_deg2_1polynome(self):
        # Arrange
        first = Polynome([-3, -2, -1])
        second = Polynome([4, 2, -2])
        # Act
        eq = first + second
        # Assert
        self.assertEqual(str(eq), '1x^2-3')

    def test_add_deg3_deg3_1polynome(self):
        # Arrange
        first = Polynome([-3, -2, -1, 0])
        second = Polynome([3, 2, 5, 2])
        # Act
        eq = first + second
        # Assert
        self.assertEqual(str(eq), '4x^1+2')

    def test_add_deg2_deg2_zero_polynome(self):
        # Arrange
        first = Polynome([-2, -1, -2])
        second = Polynome([2, 1, 2])
        # Act
        eq = first + second
        # Assert
        self.assertEqual(str(eq), '0')

    def test_add_deg2_deq0_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = Polynome([0])
        # Act
        eq = first + second
        # Assert
        self.assertEqual(str(eq), '2x^2+1x^1-2')

    def test_add_deg2_deq2_0polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = Polynome([-2, -1, 3])
        # Act
        eq = first + second
        # Assert
        self.assertEqual(str(eq), '1')

    def test_add_deg0_deq0_zero_polynome(self):
        # Arrange
        first = Polynome([0])
        second = Polynome([0])
        # Act
        eq = first + second
        # Assert
        self.assertEqual(str(eq), '0')

    def test_add_deg2_string_exception_other_isnt_polynom(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = first + second
        # Assert
        self.assertTrue('Other isn\'t polynome.' in str(context.exception))

    def test_add_deg2_int4_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = int(4)
        # Act
        eq = first + second
        # Assert
        self.assertEqual(str(eq), '2x^2+1x^1+2')

    def test_add_deg2_float3_4_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = float(3.4)
        # Act
        eq = first + second
        # Assert
        self.assertEqual(str(eq), '2x^2+1x^1+1.4')

    def test_add_deg2_int4_float1_3_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = int(4)
        third = float(1.3)
        # Act
        eq = first + second + third
        # Assert
        self.assertEqual(str(eq), '2x^2+1x^1+3.3')

    def test_sub_deg2_deg2_2polynome(self):
        # Arrange
        first = Polynome([-3, 2, 5])
        second = Polynome([-1, 5, -2])
        # Act
        eq = first - second
        # Assert
        self.assertEqual(str(eq), '-2x^2-3x^1+7')

    def test_sub_deg2_deg2_1polynome(self):
        # Arrange
        first = Polynome([-3, -2, -1])
        second = Polynome([-5, -2, -2])
        # Act
        eq = first - second
        # Assert
        self.assertEqual(str(eq), '2x^2+1')

    def test_sub_deg3_deg3_1polynome(self):
        # Arrange
        first = Polynome([-3, -2, -1, 0])
        second = Polynome([-3, -2, -5, -2])
        # Act
        eq = first - second
        # Assert
        self.assertEqual(str(eq), '4x^1+2')

    def test_sub_deg2_deg2_zero_polynome(self):
        # Arrange
        first = Polynome([-2, -1, -2])
        second = Polynome([-2, -1, -2])
        # Act
        eq = first - second
        # Assert
        self.assertEqual(str(eq), '0')

    def test_sub_deg2_deq0_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = Polynome([0])
        # Act
        eq = first - second
        # Assert
        self.assertEqual(str(eq), '2x^2+1x^1-2')

    def test_sub_deg2_deq2_0polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = Polynome([2, 1, -3])
        # Act
        eq = first - second
        # Assert
        self.assertEqual(str(eq), '1')

    def test_sub_deg0_deq0_zero_polynome(self):
        # Arrange
        first = Polynome([0])
        second = Polynome([0])
        # Act
        eq = first - second
        # Assert
        self.assertEqual(str(eq), '0')

    def test_sub_deg2_string_exception_other_isnt_polynom(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = first - second
        # Assert
        self.assertTrue('Other isn\'t polynome.' in str(context.exception))

    def test_sub_deg2_int4_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = int(4)
        # Act
        eq = first - second
        # Assert
        self.assertEqual(str(eq), '2x^2+1x^1-6')

    def test_sub_deg2_float3_4_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = float(3.4)
        # Act
        eq = first - second
        # Assert
        self.assertEqual(str(eq), '2x^2+1x^1-5.4')

    def test_sub_deg2_int4_float1_3_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = int(4)
        third = float(1.3)
        # Act
        eq = first - second - third
        # Assert
        self.assertEqual(str(eq), '2x^2+1x^1-7.3')

    def test_mul_deg2_deg_0_2polenome(self):
        # Arrange
        first = Polynome([2, 1, 4])
        second = Polynome([2])
        # Act
        eq = first * second
        # Assert
        self.assertEqual(str(eq), '4x^2+2x^1+8')

    def test_mul_deg2_deg_1_3polenome(self):
        # Arrange
        first = Polynome([2, 1, 4])
        second = Polynome([2, 0])
        # Act
        eq = first * second
        # Assert
        self.assertEqual(str(eq), '4x^3+2x^2+8x^1')

    def test_mul_deg2_deg_2_4polenome(self):
        # Arrange
        first = Polynome([2, 2, 4])
        second = Polynome([2, 1, 1])
        # Act
        eq = first * second
        # Assert
        self.assertEqual(str(eq), '4x^4+6x^3+12x^2+6x^1+4')

    def test_mul_deg2_deg_zero_zero_polenome(self):
        # Arrange
        first = Polynome([2, 2, 4])
        second = Polynome([0])
        # Act
        eq = first * second
        # Assert
        self.assertEqual(str(eq), '0')

    def test_mul_deg2_string_exception_other_isnt_polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = first * second
        # Assert
        self.assertTrue('Other isn\'t polynome.' in str(context.exception))

    def test_mul_deg2_int4_2polynome(self):
        # Arrange
        first = Polynome([5, 4, -2])
        second = int(4)
        # Act
        eq = first * second
        # Assert
        self.assertEqual(str(eq), '20x^2+16x^1-8')

    def test_mul_deg2_float1_5_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = float(1.5)
        # Act
        eq = first * second
        # Assert
        self.assertEqual(str(eq), '3.0x^2+1.5x^1-3.0')

    def test_mul_deg2_int4_float1_5_2polynome(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = int(4)
        third = float(1.5)
        # Act
        eq = first * second * third
        # Assert
        self.assertEqual(str(eq), '12.0x^2+6.0x^1-12.0')

    def test_ne_deg2_deg2_True(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = Polynome([2, 5, -2])
        # Act
        eq = first != second
        # Assert
        self.assertTrue(eq)

    def test_ne_deg2_deg2_False(self):
        # Arrange
        first = Polynome([2, 1, -2])
        second = Polynome([2, 1, -2])
        # Act
        eq = first != second
        # Assert
        self.assertFalse(eq)


if __name__ == '__main__':
    unittest.main()
