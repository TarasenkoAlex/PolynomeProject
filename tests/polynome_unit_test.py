import unittest
from polynome.polynome import Polynome

class PolynomeTestCase(unittest.TestCase):

    #region Tests INIT.

    def test_init_4_16_valid(self):
        # Arrange
        pol = Polynome([4, 16])
        #Act
        #Assert
        self.assertIsNotNone(pol)

    def test_init_zerostart_valid(self):
        # Arrange
        pol = Polynome([0, 0, 0])
        #Act
        #Assert
        self.assertIsNotNone(pol)

    def test_init_zero_start_valid(self):
        # Arrange
        pol = Polynome([0, 2, 0])
        #Act
        #Assert
        self.assertIsNotNone(pol)

    def test_init_clean_list_exception_dont_exist_polynome(self):
        # Arrange
        # Act
        with self.assertRaises(Exception) as context:
            pol = Polynome([])
        # Assert
        self.assertTrue('Coefficients must be not empty.' in str(context.exception))

    #endregion

    #region Tests STR.

    def test_str_8_8polynome(self):
        # Arrange
        pol = Polynome([8])
        # Act
        s = str(pol)
        # Assert
        self.assertEqual(s, '8')

    def test_str_deg_zero_zero_coef_polynome(self):
        # Arrange
        pol = Polynome([0])
        # Act
        s = str(pol)
        # Assert
        self.assertEqual(s, '0')

    def test_str_deg_zero_doublezero_coef_polynome(self):
        # Arrange
        pol = Polynome([0, 0])
        # Act
        s = str(pol)
        # Assert
        self.assertEqual(s, '0')

    def test_str_deg9_high_degree_polynome(self):
        # Arrange
        pol = Polynome([9, 0, 0, 0])
        # Act
        s = str(pol)
        # Assert
        self.assertEqual(s, '9x^3')

    def test_str_high_degree_polynome(self):
        # Arrange
        pol = Polynome([8, 0, 4, 996])
        # Act
        s = str(pol)
        # Assert
        self.assertEqual(s, '8x^3 + 4x + 996')

    def test_str_deg3_notnull_coef_polynome(self):
        # Arrange
        pol = Polynome([4, -8, 16, -32])
        # Act
        s = str(pol)
        # Assert
        self.assertEqual(s, '4x^3 - 8x^2 + 16x - 32')

    #endregion

    #region Tests EQ.

    def test_eq_deg2_deg2_True(self):
        # Arrange
        firstPol = Polynome([9, 1, -9])
        secondPol = Polynome([9, 1, -9])
        # Act
        eq = firstPol.__eq__(secondPol)
        # Assert
        self.assertTrue(eq)

    def test_eq_deg3_deg2_False(self):
        # Arrange
        firstPol = Polynome([4, 3, 2, -1])
        secondPol = Polynome([3, 2, -1])
        # Act
        eq = firstPol.__eq__(secondPol)
        # Assert
        self.assertFalse(eq)

    def test_eq_deg3_deg2_False(self):
        # Arrange
        firstPol = Polynome([3, 2, -1])
        secondPol = Polynome([2, -1])
        # Act
        eq = firstPol.__compare__(secondPol)
        # Assert
        self.assertEqual(eq, 1)

    def test_eq_deg2_deg3_False(self):
        # Arrange
        firstPol = Polynome([2, -1])
        secondPol = Polynome([3, 2, -1])
        # Act
        eq = firstPol.__compare__(secondPol)
        # Assert
        self.assertEqual(eq, -1)

    def test_eq_deg2_deg2_other_coeff_False(self):
        # Arrange
        firstPol = Polynome([9, 1, -9])
        secondPol = Polynome([8, -1, -9])
        # Act
        eq = firstPol.__eq__(secondPol)
        # Assert
        self.assertFalse(eq)

    def test_eq_deg2_deg2_other_coeffs_False(self):
        # Arrange
        firstPol = Polynome([9, 1, -9])
        secondPol = Polynome([18, -2, -79])
        # Act
        eq = firstPol.__eq__(secondPol)
        # Assert
        self.assertFalse(eq)

    def test_eq_deg2_string_exception_other_isnt_polynom(self):
        # Arrange
        firstPol = Polynome([-8, -2, -1])
        secondPol = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = firstPol.__eq__(secondPol)
        # Assert
        self.assertTrue("Second polynome don't exist." in str(context.exception))

    def test_eq_deg2_int_True(self):
        # Arrange
        firstPol = Polynome([5])
        secondPol = int(5)
        # Act
        eq = firstPol.__eq__(secondPol)
        # Assert
        self.assertTrue(eq)

    def test_eq_deg2_int_False(self):
        # Arrange
        firstPol = Polynome([5])
        secondPol = int(6)
        # Act
        eq = firstPol.__eq__(secondPol)
        # Assert
        self.assertFalse(eq)

    def test_eq_deg2_float_True(self):
        # Arrange
        firstPol = Polynome([4.8])
        secondPol = float(4.8)
        # Act
        eq = firstPol.__eq__(secondPol)
        # Assert
        self.assertTrue(eq)

    def test_eq_deg2_float_False(self):
        # Arrange
        firstPol = Polynome([5])
        secondPol = float(3.1)
        # Act
        eq = firstPol.__eq__(secondPol)
        # Assert
        self.assertFalse(eq)

    def test_eq_deg2_string__exception_other_isnt_polynom(self):
        # Arrange
        firstPol = Polynome([5])
        secondPol = "asdf"
        # Act
        with self.assertRaises(Exception) as context:
            eq = firstPol.__compare__(secondPol)
        # Assert
        self.assertTrue("Second polynome don't exist." in str(context.exception))

    #endregion

    #region Tests LT

    def test_lt_deg2_deg2_True(self):
        # Arrange
        firstPol = Polynome([3, 2, -1])
        secondPol = Polynome([2, -1])
        # Act
        eq = secondPol < firstPol
        # Assert
        self.assertTrue(eq)

    def test_lt_deg2_deg2_False(self):
        # Arrange
        firstPol = Polynome([3, 2, -1])
        secondPol = Polynome([2, -1])
        # Act
        eq = firstPol < secondPol
        # Assert
        self.assertFalse(eq)

    #endregion

    #region Tests LE

    def test_le_deg2_deg2_True(self):
        # Arrange
        firstPol = Polynome([3, 2, -1])
        secondPol = Polynome([2, -1])
        # Act
        eq = secondPol <= firstPol
        # Assert
        self.assertTrue(eq)

    def test_le_deg2_deg2_False(self):
        # Arrange
        firstPol = Polynome([3, 2, -1])
        secondPol = Polynome([2, -1])
        # Act
        eq = firstPol <= secondPol
        # Assert
        self.assertFalse(eq)

    #endregion

    # region Tests GT

    def test_gt_deg2_deg2_False(self):
        # Arrange
        firstPol = Polynome([3, 2, -1])
        secondPol = Polynome([2, -1])
        # Act
        eq = secondPol > firstPol
        # Assert
        self.assertFalse(eq)

    def test_gt_deg2_deg2_True(self):
        # Arrange
        firstPol = Polynome([3, 2, -1])
        secondPol = Polynome([2, -1])
        # Act
        eq = firstPol > secondPol
        # Assert
        self.assertTrue(eq)

    # endregion

    # region Tests GE

    def test_ge_deg2_deg2_False(self):
        # Arrange
        firstPol = Polynome([3, 2, -1])
        secondPol = Polynome([2, -1])
        # Act
        eq = secondPol >= firstPol
        # Assert
        self.assertFalse(eq)

    def test_ge_deg2_deg2_True(self):
        # Arrange
        firstPol = Polynome([3, 2, -1])
        secondPol = Polynome([2, -1])
        # Act
        eq = firstPol >= secondPol
        # Assert
        self.assertTrue(eq)

    # endregion

    #region Tests MUL.

    def test_mul_deg2_deg_0_2polenome(self):
        # Arrange
        firstPol = Polynome([2, 1, 4])
        secondPol = Polynome([2])
        # Act
        eq = firstPol * secondPol
        # Assert
        self.assertEqual(str(eq), '4x^2 + 2x + 8')

    def test_mul_deg2_deg_1_3polenome(self):
        # Arrange
        firstPol = Polynome([2, 1, 4])
        second = Polynome([2, 0])
        # Act
        eq = firstPol * second
        # Assert
        self.assertEqual(str(eq), '4x^3 + 2x^2 + 8x')

    def test_mul_deg2_deg_2_4polenome(self):
        # Arrange
        firstPol = Polynome([2, 2, 4])
        secondPol = Polynome([2, 1, 1])
        # Act
        eq = firstPol * secondPol
        # Assert
        self.assertEqual(str(eq), '4x^4 + 6x^3 + 12x^2 + 6x + 4')

    def test_mul_deg2_deg_zero_zero_polenome(self):
        # Arrange
        firstPol = Polynome([2, 2, 4])
        second = Polynome([0])
        # Act
        eq = firstPol * second
        # Assert
        self.assertEqual(str(eq), '0')

    def test_mul_deg2_string_exception_other_isnt_polynome(self):
        # Arrange
        firstPol = Polynome([28, 71, 9])
        secondPol = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = firstPol * secondPol
        # Assert
        self.assertTrue("Second polynome don't exist." in str(context.exception))

    def test_mul_deg2_int4_2polynome(self):
        # Arrange
        firstPol = Polynome([5, 4, -2])
        secondPol = int(5)
        # Act
        eq = firstPol * secondPol
        # Assert
        self.assertEqual(str(eq), '25x^2 + 20x - 10')

    def test_mul_deg2_float1_5_2polynome(self):
        # Arrange
        firstPol = Polynome([2, 1, -2])
        secondPol = float(2.5)
        # Act
        eq = firstPol * secondPol
        # Assert
        self.assertEqual(str(eq), '5.0x^2 + 2.5x - 5.0')

    def test_mul_deg2_int4_float1_5_2polynome(self):
        # Arrange
        firstPol = Polynome([2, 1, -2])
        secondPol = int(4)
        thirdPol = float(2.5)
        # Act
        eq = firstPol * secondPol * thirdPol
        # Assert
        self.assertEqual(str(eq), '20.0x^2 + 10.0x - 20.0')

    #endregion

    #region Tests RMUL.

    def test_rmul_deg2_int4_2polynome(self):
        # Arrange
        firstPol = Polynome([5, 4, -2])
        secondPol = int(5)
        # Act
        eq = secondPol * firstPol
        # Assert
        self.assertEqual(str(eq), '25x^2 + 20x - 10')

    def test_rmul_deg2_float1_5_2polynome(self):
        # Arrange
        firstPol = Polynome([2, 1, -2])
        secondPol = float(2.5)
        # Act
        eq = secondPol * firstPol
        # Assert
        self.assertEqual(str(eq), '5.0x^2 + 2.5x - 5.0')

    def test_rmul_deg2_int4_float1_5_2polynome(self):
        # Arrange
        firstPol = Polynome([2, 1, -2])
        secondPol = int(4)
        thirdPol = float(2.5)
        # Act
        eq = secondPol * thirdPol * firstPol
        # Assert
        self.assertEqual(str(eq), '20.0x^2 + 10.0x - 20.0')

    #endregion

    # region Tests MUL.

    def test_imul_deg2_deg_0_2polenome(self):
        # Arrange
        firstPol = Polynome([2, 1, 4])
        secondPol = Polynome([2])
        # Act
        firstPol *= secondPol
        # Assert
        self.assertEqual(str(firstPol), '4x^2 + 2x + 8')

    #endregion

    #region Tests ADD.

    def test_add_deg2_deg2_2polynome(self):
        # Arrange
        firstPol = Polynome([-3, -2, -1])
        secondPol = Polynome([18, 15, -2])
        # Act
        eq = firstPol + secondPol
        # Assert
        self.assertEqual(str(eq), '15x^2 + 13x - 3')

    def test_add_deg2_deg2_1polynome(self):
        # Arrange
        firstPol = Polynome([-3, -2, -1])
        secondPol = Polynome([8, 2, -8])
        # Act
        eq = firstPol + secondPol
        # Assert
        self.assertEqual(str(eq), '5x^2 - 9')

    def test_add_deg3_deg3_1polynome(self):
        # Arrange
        firstPol = Polynome([-6, -8, -1, 0])
        secondPol = Polynome([6, 8, 8, 7])
        # Act
        eq = firstPol + secondPol
        # Assert
        self.assertEqual(str(eq), '7x + 7')

    def test_add_deg2_deg2_zero_polynome(self):
        # Arrange
        firstPol = Polynome([-112, -771, -892])
        secondPol = Polynome([112, 771, 892])
        # Act
        eq = firstPol + secondPol
        # Assert
        self.assertEqual(str(eq), '0')

    def test_add_deg2_deq0_2polynome(self):
        # Arrange
        firstPol = Polynome([2, 100, -25])
        second = Polynome([0])
        # Act
        eq = firstPol + second
        # Assert
        self.assertEqual(str(eq), '2x^2 + 100x - 25')

    def test_add_deg2_deq2_0polynome(self):
        # Arrange
        firstPol = Polynome([22, 14, -20])
        secondPol = Polynome([-22, -14, 30])
        # Act
        eq = firstPol + secondPol
        # Assert
        self.assertEqual(str(eq), '10')

    def test_add_deg0_deq0_zero_polynome(self):
        # Arrange
        firstPol = Polynome([0])
        second = Polynome([0])
        # Act
        eq = firstPol + second
        # Assert
        self.assertEqual(str(eq), '0')

    def test_add_deg2_string_exception_other_isnt_polynom(self):
        # Arrange
        firstPol = Polynome([512, 1, -2])
        secondPol = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = firstPol + secondPol
        # Assert
        self.assertTrue("Second polynome don't exist." in str(context.exception))

    def test_add_deg2_int4_2polynome(self):
        # Arrange
        firstPol = Polynome([259, 881, -2])
        second = int(4)
        # Act
        eq = firstPol + second
        # Assert
        self.assertEqual(str(eq), '259x^2 + 881x + 2')

    def test_add_deg2_float3_4_2polynome(self):
        # Arrange
        firstPol = Polynome([2, 1, -2])
        secondPol = float(83.4)
        # Act
        eq = firstPol + secondPol
        # Assert
        self.assertEqual(str(eq), '2x^2 + x + 81.4')

    def test_add_deg2_int4_float1_3_2polynome(self):
        # Arrange
        firstPol = Polynome([28, 7, -2])
        second = int(6)
        thirdPol = float(187.3)
        # Act
        eq = firstPol + second + thirdPol
        # Assert
        self.assertEqual(str(eq), '28x^2 + 7x + 191.3')

    #endregion

    #region Tests RADD.

    def test_radd_deg2_deg2_2polynome(self):
        # Arrange
        firstPol = Polynome([-3, -2, -1])
        secondPol = Polynome([18, 15, -2])
        # Act
        eq = firstPol .__radd__(secondPol)
        # Assert
        self.assertEqual(str(eq), '15x^2 + 13x - 3')

    def test_radd_deg2_deg2_1polynome(self):
        # Arrange
        firstPol = Polynome([-3, -2, -1])
        secondPol = Polynome([8, 2, -8])
        # Act
        eq = firstPol.__radd__(secondPol)
        # Assert
        self.assertEqual(str(eq), '5x^2 - 9')

    def test_radd_deg3_deg3_1polynome(self):
        # Arrange
        firstPol = Polynome([-6, -8, -1, 0])
        secondPol = Polynome([6, 8, 8, 7])
        # Act
        eq = firstPol.__radd__(secondPol)
        # Assert
        self.assertEqual(str(eq), '7x + 7')

    def test_radd_deg2_deg2_zero_polynome(self):
        # Arrange
        firstPol = Polynome([-112, -771, -892])
        secondPol = Polynome([112, 771, 892])
        # Act
        eq = firstPol.__radd__(secondPol)
        # Assert
        self.assertEqual(str(eq), '0')

    def test_radd_deg2_deq0_2polynome(self):
        # Arrange
        firstPol = Polynome([2, 100, -25])
        second = Polynome([0])
        # Act
        eq = firstPol.__radd__(second)
        # Assert
        self.assertEqual(str(eq), '2x^2 + 100x - 25')

    def test_radd_deg2_deq2_0polynome(self):
        # Arrange
        firstPol = Polynome([22, 14, -20])
        secondPol = Polynome([-22, -14, 30])
        # Act
        eq = firstPol.__radd__(secondPol)
        # Assert
        self.assertEqual(str(eq), '10')

    def test_radd_deg0_deq0_zero_polynome(self):
        # Arrange
        firstPol = Polynome([0])
        second = Polynome([0])
        # Act
        eq = firstPol.__radd__(second)
        # Assert
        self.assertEqual(str(eq), '0')

    def test_radd_deg2_string_exception_other_isnt_polynom(self):
        # Arrange
        firstPol = Polynome([512, 1, -2])
        secondPol = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = secondPol + firstPol
        # Assert
        self.assertTrue("Second polynome don't exist." in str(context.exception))

    def test_radd_deg2_int4_2polynome(self):
        # Arrange
        firstPol = Polynome([259, 881, -2])
        second = int(4)
        # Act
        eq = second + firstPol
        # Assert
        self.assertEqual(str(eq), '259x^2 + 881x + 2')

    def test_radd_deg2_float3_4_2polynome(self):
        # Arrange
        firstPol = Polynome([2, 1, -2])
        secondPol = float(83.4)
        # Act
        eq = secondPol + firstPol
        # Assert
        self.assertEqual(str(eq), '2x^2 + x + 81.4')

    def test_radd_deg2_int4_float1_3_2polynome(self):
        # Arrange
        firstPol = Polynome([28, 7, -2])
        second = int(6)
        thirdPol = float(187.3)
        # Act
        eq = second + thirdPol + firstPol
        # Assert
        self.assertEqual(str(eq), '28x^2 + 7x + 191.3')

    #endregion

    # region Tests ADD.

    def test_iadd_deg2_deg2_2polynome(self):
        # Arrange
        firstPol = Polynome([-3, -2, -1])
        secondPol = Polynome([18, 15, -2])
        # Act
        firstPol += secondPol
        # Assert
        self.assertEqual(str(firstPol), '15x^2 + 13x - 3')

    #endregion

    #region Tests SUB.

    def test_sub_deg2_deg2_2polynome(self):
        # Arrange
        firstPol = Polynome([-3, 2, 5])
        secondPol = Polynome([-1, 5, -2])
        # Act
        eq = firstPol - secondPol
        # Assert
        self.assertEqual(str(eq), '-2x^2 - 3x + 7')

    def test_sub_deg2_deg2_1polynome(self):
        # Arrange
        firstPol = Polynome([-3, -2, -1])
        secondPol = Polynome([-8, -2, -3])
        # Act
        eq = firstPol - secondPol
        # Assert
        self.assertEqual(str(eq), '5x^2 + 2')

    def test_sub_deg3_deg3_1polynome(self):
        # Arrange
        firstPol = Polynome([-3, -2, -1, 0])
        secondPol = Polynome([-3, -2, -7, -21])
        # Act
        eq = firstPol - secondPol
        # Assert
        self.assertEqual(str(eq), '6x + 21')

    def test_sub_deg2_deg2_zero_polynome(self):
        # Arrange
        firstPol = Polynome([-2, -1, -2])
        secondPol = Polynome([-2, -1, -2])
        # Act
        eq = firstPol - secondPol
        # Assert
        self.assertEqual(str(eq), '0')

    def test_sub_deg2_deq0_2polynome(self):
        # Arrange
        firstPol = Polynome([28, 71, -2])
        secondPol = Polynome([0])
        # Act
        eq = firstPol - secondPol
        # Assert
        self.assertEqual(str(eq), '28x^2 + 71x - 2')

    def test_sub_deg2_deq2_0polynome(self):
        # Arrange
        firstPol = Polynome([27, -5, -2])
        secondPol = Polynome([27, -5, -30])
        # Act
        eq = firstPol - secondPol
        # Assert
        self.assertEqual(str(eq), '28')

    def test_sub_deg0_deq0_zero_polynome(self):
        # Arrange
        firstPol = Polynome([0])
        secondPol = Polynome([0])
        # Act
        eq = firstPol - secondPol
        # Assert
        self.assertEqual(str(eq), '0')

    def test_sub_deg2_string_exception_other_isnt_polynom(self):
        # Arrange
        firstPol = Polynome([20, 18, -27])
        second = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = firstPol - second
        # Assert
        self.assertTrue("Second polynome don't exist." in str(context.exception))

    def test_sub_deg2_int4_2polynome(self):
        # Arrange
        firstPol = Polynome([4, -1, -2])
        secondPol = int(6)
        # Act
        eq = firstPol - secondPol
        # Assert
        self.assertEqual(str(eq), '4x^2 - x - 8')

    def test_sub_deg2_float3_4_2polynome(self):
        # Arrange
        firstPol = Polynome([2, 1, -2])
        second = float(30.4)
        # Act
        eq = firstPol - second
        # Assert
        self.assertEqual(str(eq), '2x^2 + x - 32.4')

    def test_sub_deg2_int4_float1_3_2polynome(self):
        # Arrange
        firstPol = Polynome([8, 1, -2])
        secondPol = int(7)
        thirdPol = float(2.3)
        # Act
        eq = firstPol - secondPol - thirdPol
        # Assert
        self.assertEqual(str(eq), '8x^2 + x - 11.3')

    #endregion

    #region Tests RSUB.

    def test_rsub_deg2_deg2_2polynome(self):
        # Arrange
        firstPol = Polynome([-3, 2, 5])
        secondPol = Polynome([-1, 5, -2])
        # Act
        eq = firstPol.__rsub__(secondPol)
        # Assert
        self.assertEqual(str(eq), '2x^2 + 3x - 7')

    def test_rsub_deg2_deg2_1polynome(self):
        # Arrange
        firstPol = Polynome([-3, -2, -1])
        secondPol = Polynome([-8, -2, -3])
        # Act
        eq = firstPol.__rsub__(secondPol)
        # Assert
        self.assertEqual(str(eq), '-5x^2 - 2')

    def test_rsub_deg3_deg3_1polynome(self):
        # Arrange
        firstPol = Polynome([-3, -2, -1, 0])
        secondPol = Polynome([-3, -2, -7, -21])
        # Act
        eq = firstPol.__rsub__(secondPol)
        # Assert
        self.assertEqual(str(eq), '-6x - 21')

    def test_rsub_deg2_deg2_zero_polynome(self):
        # Arrange
        firstPol = Polynome([-2, -1, -2])
        secondPol = Polynome([-2, -1, -2])
        # Act
        eq = firstPol.__rsub__(secondPol)
        # Assert
        self.assertEqual(str(eq), '0')

    def test_rsub_deg2_deq0_2polynome(self):
        # Arrange
        firstPol = Polynome([28, 71, -2])
        secondPol = Polynome([0])
        # Act
        eq = firstPol.__rsub__(secondPol)
        # Assert
        self.assertEqual(str(eq), '-28x^2 - 71x + 2')

    def test_rsub_deg2_deq2_0polynome(self):
        # Arrange
        firstPol = Polynome([27, -5, -2])
        secondPol = Polynome([27, -5, -30])
        # Act
        eq = firstPol.__rsub__(secondPol)
        # Assert
        self.assertEqual(str(eq), '-28')

    def test_rsub_deg0_deq0_zero_polynome(self):
        # Arrange
        firstPol = Polynome([0])
        secondPol = Polynome([0])
        # Act
        eq = firstPol.__rsub__(secondPol)
        # Assert
        self.assertEqual(str(eq), '0')

    def test_rsub_deg2_string_exception_other_isnt_polynom(self):
        # Arrange
        firstPol = Polynome([20, 18, -27])
        second = 'string'
        # Act
        with self.assertRaises(Exception) as context:
            eq = second - firstPol
        # Assert
        self.assertTrue("Second polynome don't exist." in str(context.exception))

    def test_rsub_deg2_int4_2polynome(self):
        # Arrange
        firstPol = Polynome([-4, 1, 2])
        secondPol = int(-6)
        # Act
        eq = secondPol - firstPol
        # Assert
        self.assertEqual(str(eq), '4x^2 - x - 8')

    def test_rsub_deg2_float3_4_2polynome(self):
        # Arrange
        firstPol = Polynome([-2, -1, 2])
        second = float(-30.444466)
        # Act
        eq = second - firstPol
        # Assert
        self.assertEqual(str(eq), '2x^2 + x - 32.444')

    def test_rsub_deg2_int4_float1_3_2polynome(self):
        # Arrange
        firstPol = Polynome([-8, -1, -2])
        secondPol = int(7)
        thirdPol = float(2.5)
        # Act
        eq = secondPol - thirdPol - firstPol
        # Assert
        self.assertEqual(str(eq), '8x^2 + x + 6.5')

    #endregion

    # region Tests SUB.

    def test_isub_deg2_deg2_2polynome(self):
        # Arrange
        firstPol = Polynome([-3, 2, 5])
        secondPol = Polynome([-1, 5, -2])
        # Act
        firstPol -= secondPol
        # Assert
        self.assertEqual(str(firstPol), '-2x^2 - 3x + 7')

    #endregion

    #region Tests NE.

    def test_ne_deg2_deg2_True(self):
        # Arrange
        firstPol = Polynome([72, 18, -2])
        secondPol = Polynome([72, 52, -2])
        # Act
        eq = firstPol != secondPol
        # Assert
        self.assertTrue(eq)

    def test_ne_deg2_deg2_False(self):
        # Arrange
        firstPol = Polynome([27, -91, -2])
        secondPol = Polynome([27, -91, -2])
        # Act
        eq = firstPol != secondPol
        # Assert
        self.assertFalse(eq)

    #endregion

if __name__ == '__main__':
    unittest.main()
