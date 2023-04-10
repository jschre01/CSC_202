# Start of unittest - add to completely test functions in exp_eval


import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)
        self.assertAlmostEqual(postfix_eval("5 3 -"), 2)
        self.assertAlmostEqual(postfix_eval("6 5 *"), 30)
        self.assertAlmostEqual(postfix_eval("55 11 /"), 5)
        self.assertAlmostEqual(postfix_eval("5 2 **"), 25)
        self.assertAlmostEqual(postfix_eval("7 3 <<"), 56)
        self.assertAlmostEqual(postfix_eval("60 2 >>"), 15)
        self.assertAlmostEqual(postfix_eval("6.6 5.3 + 12 -"), -.1)
        self.assertAlmostEqual(postfix_eval("4 8 * 12 8 - 3 ** + 4 4 1 + * -"), 76)


    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        with self.assertRaises(ValueError):postfix_eval("4 2 - 0 /")

    def test_postfix_eval_06(self):
        try:
            postfix_eval("4.0 8 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
            
    def test_postfix_eval_07(self):
        try:
            postfix_eval("4 8.0 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_08(self):
        try:
            postfix_eval("4.0 8 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_09(self):
        try:
            postfix_eval("4 8.0 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_10(self):
        try:
            postfix_eval("8 2 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")


    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("6.0 - 5.4"), "6.0 5.4 -")
        self.assertEqual(infix_to_postfix("4 * 8 + ( 12 - 8 ) ** 3 - 4 * ( 4 + 1 )"), "4 8 * 12 8 - 3 ** + 4 4 1 + * -")
        self.assertEqual(infix_to_postfix("6.6 * 7 ** 32 / 14"), "6.6 7 32 ** * 14 /")
        self.assertEqual(infix_to_postfix("8 << 2 ** 3"), "8 2 << 3 **")
        self.assertEqual(infix_to_postfix("8 * 3 << 2"), "8 3 2 << *")
        self.assertEqual(infix_to_postfix("8 << 2 * 3"), "8 2 << 3 *")
        self.assertEqual(infix_to_postfix("8 ** 2 << 2"), "8 2 2 << **")
        
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

if __name__ == "__main__":
    unittest.main()
