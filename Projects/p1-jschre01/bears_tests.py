import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_bear_05(self):
        self.assertTrue(bears(500))

    def test_bear_06(self):
        self.assertFalse(bears(105))

    def test_bear_07(self):
        self.assertTrue(bears(219))

    def test_bear_08(self):
        self.assertFalse(bears(100))

    def test_bear_09(self):
        self.assertTrue(bears(4000))

    def test_bear_10(self):
        self.assertFalse(bears(120))

    def test_bear_11(self):
        self.assertFalse(bears(165))

    def test_bear_12(self):
        self.assertFalse(bears(72))

    def test_bear_13(self):
        self.assertFalse(bears(273))

    def test_bear_14(self):
        self.assertTrue(bears(32000))

    def test_bear_15(self):
        self.assertTrue(bears(330))

    def test_bear_16(self):
        self.assertTrue(bears(818347651974035467503297424206899788054160511510766197370822842024033449101168638720817523081476039287721671031890017752304314136471348263332131897344000))

if __name__ == "__main__":
    unittest.main()
