# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Assignment 2
# Term:        Fall 2017

import unittest
import exp_eval

class TestAssign2(unittest.TestCase):



    def test_infix_to_postfix_1(self):
        # Tests conversion with parentheses
        infix = "( 2 ^ 3 / ( 5 * 4 ) + 6 )" 
        result = "2 3 ^ 5 4 * / 6 +"
        self.assertEqual(exp_eval.infix_to_postfix(infix), result)

    def test_infix_to_postfix_2(self):
        # Tests conversion with floats
        infix = "3 - 4 / 2.1 + 7 * 5 ^ 6"
        result = "3 4 2.1 / - 7 5 6 ^ * +"
        self.assertEqual(exp_eval.infix_to_postfix(infix), result)

    def test_infix_to_postfix_3(self):
        # Tests conversion with exponents
        infix = "( 2 ^ 3.0 ) ^ 4"
        result = "2 3.0 ^ 4 ^"
        self.assertEqual(exp_eval.infix_to_postfix(infix), result)

    def test_infix_to_postfix_4(self):
        # Tests conversion with negatives
        infix = "-2 * ( -3 + 4 ) ^ -1"
        result = "-2 -3 4 + -1 ^ *"
        self.assertEqual(exp_eval.infix_to_postfix(infix), result)



    def test_postfix_eval_1(self):
        # Test evaluate for a float result
        result = 6.4
        postfix = "2 3 ^ 5 4 * / 6 +"
        self.assertEqual(exp_eval.postfix_eval(postfix), result)

    def test_postfix_eval_2(self):
        # Test evaluate with all operators
        result = 176
        postfix = "3 4 2 / - 7 5 2 ^ * +"
        self.assertEqual(exp_eval.postfix_eval(postfix), result)

    def test_postfix_eval_3(self):
        # Test evaluate with multiple exponents 
        result = 4096.0
        postfix = "2 3.0 ^ 4 ^"
        self.assertEqual(exp_eval.postfix_eval(postfix), result)
    
    def test_postfix_eval_4(self):
        # Test evaluate with negatives
        result = -2
        postfix = "-2 -3 4 + -1 ^ *"
        self.assertEqual(exp_eval.postfix_eval(postfix), result)

    def test_postfix_eval_5(self):
        # Test evaluate with zero division
        with self.assertRaises(ValueError): 
            exp_eval.postfix_eval("3 0 /")



    def test_is_num_1(self):
        # Tests is num with an operator
        self.assertFalse(exp_eval.is_num("-"))

    def test_is_num_2(self):
        # Tests is num with a float
        self.assertTrue(exp_eval.is_num("2.0"))

    def test_is_num_3(self):
        # Test is num with a negative
        self.assertTrue(exp_eval.is_num("-1"))



    def test_precedence_1(self):
        # Checks if + and - have the same precedence
        self.assertEqual(exp_eval.precedence("+"), exp_eval.precedence("-"))

    def test_precedence_2(self):
        # Checks if / and * have the same precedence
        self.assertEqual(exp_eval.precedence("/"), exp_eval.precedence("*"))

    def test_precedence_3(self):
        # Checks if ^ has a greater precedence than *
        self.assertTrue(exp_eval.precedence("^") > exp_eval.precedence("*"))

    def test_precedence_4(self):
        # Checks if * has a greater precedence than +
        self.assertTrue(exp_eval.precedence("*") > exp_eval.precedence("+"))



    def test_postfix_valid_1(self):
        # Checks if a variety of invalid postfix expressions are invalid
        self.assertFalse(exp_eval.postfix_valid(""))
        self.assertFalse(exp_eval.postfix_valid("+"))
        self.assertFalse(exp_eval.postfix_valid("2 3"))
        self.assertFalse(exp_eval.postfix_valid("3 2 / - 7 5 2 ^ * +"))
        self.assertFalse(exp_eval.postfix_valid("3 4 5 2 / - 7 5 2 ^ * +"))
 
    def test_postfix_valid_2(self):
        # Checks if a variety of valid postfix expressions are valid
        self.assertTrue(exp_eval.postfix_valid("2 3 +"))
        self.assertTrue(exp_eval.postfix_valid("2 3 -"))
        self.assertTrue(exp_eval.postfix_valid("2 3 *"))
        self.assertTrue(exp_eval.postfix_valid("2 3 /"))
        self.assertTrue(exp_eval.postfix_valid("3 4 2 / - 7 5 2 ^ * +"))



    def test_do_math_1(self):
        # Tests math with +
        self.assertEqual(exp_eval.do_math("+", 1, 2), 3)

    def test_do_math_2(self):
        # Tests math with -
        self.assertEqual(exp_eval.do_math("-", 1, 2), -1)

    def test_do_math_3(self):
        # Tests math with *
        self.assertEqual(exp_eval.do_math("*", 1, 2), 2)

    def test_do_math_4(self):
        # Tests math with /
        self.assertEqual(exp_eval.do_math("/", 1, 2), 0.5)

    def test_do_math_5(self):
        # Tests math with zero division
        with self.assertRaises(ValueError):
            exp_eval.do_math("/", 1, 0)
    
    def test_do_math_6(self):
        # Tests math with ^
        self.assertEqual(exp_eval.do_math("^", 2, 4), 16)



    def test_float_or_int_1(self):
        # Test float or int with float string
        self.assertEqual(exp_eval.float_or_int("2.1"), 2.1)

    def test_float_or_int_2(self):
        # Test float or int with int string
        self.assertEqual(exp_eval.float_or_int("-2"), -2)



if __name__ == "__main__":
        unittest.main()
