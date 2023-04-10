import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(91,2),"1011011")
        self.assertEqual(convert(300,2),"100101100")
        self.assertEqual(convert(1500,2),"10111011100")

    def test_base3(self):
        self.assertEqual(convert(26,3),"222")
        self.assertEqual(convert(55,3),"2001")
        self.assertEqual(convert(93,3),"10110")
        self.assertEqual(convert(26,3),"222")
        self.assertEqual(convert(457,3),"121221")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        self.assertEqual(convert(15,4),"33")
        self.assertEqual(convert(84,4),"1110")
        self.assertEqual(convert(605,4),"21131")
        self.assertEqual(convert(1000,4),"33220")

    def test_base5(self):
        self.assertEqual(convert(35,5),"120")
        self.assertEqual(convert(118,5),"433")
        self.assertEqual(convert(673,5),"10143")
        self.assertEqual(convert(84,5),"314")

    def test_base6(self):
        self.assertEqual(convert(21,6),"33")
        self.assertEqual(convert(63,6),"143")
        self.assertEqual(convert(547,6),"2311")
        self.assertEqual(convert(3421,6),"23501")

    def test_base7(self):
        self.assertEqual(convert(22,7),"31")
        self.assertEqual(convert(86,7),"152")
        self.assertEqual(convert(237,7),"456")
        self.assertEqual(convert(773,7),"2153")

    def test_base8(self):
        self.assertEqual(convert(40,8),"50")
        self.assertEqual(convert(79,8),"117")
        self.assertEqual(convert(286,8),"436")
        self.assertEqual(convert(1302,8),"2426")

    def test_base9(self):
        self.assertEqual(convert(16,9),"17")
        self.assertEqual(convert(55,9),"61")
        self.assertEqual(convert(127,9),"151")
        self.assertEqual(convert(712,9),"871")

    def test_base10(self):
        self.assertEqual(convert(24,10),"24")
        self.assertEqual(convert(45,10),"45")
        self.assertEqual(convert(134,10),"134")
        self.assertEqual(convert(7584,10),"7584")

    def test_base11(self):
        self.assertEqual(convert(53,11),"49")
        self.assertEqual(convert(153,11),"12A")
        self.assertEqual(convert(352,11),"2A0")
        self.assertEqual(convert(98,11),"8A")

    def test_base12(self):
        self.assertEqual(convert(54,12),"46")
        self.assertEqual(convert(94,12),"7A")
        self.assertEqual(convert(342,12),"246")
        self.assertEqual(convert(731,12),"50B")

    def test_base13(self):
        self.assertEqual(convert(56,13),"44")
        self.assertEqual(convert(99,13),"78")
        self.assertEqual(convert(563,13),"344")
        self.assertEqual(convert(129,13),"9C")

    def test_base14(self):
        self.assertEqual(convert(57,14),"41")
        self.assertEqual(convert(95,14),"6B")
        self.assertEqual(convert(202,14),"106")
        self.assertEqual(convert(279,14),"15D")

    def test_base15(self):
        self.assertEqual(convert(132,15),"8C")
        self.assertEqual(convert(532,15),"257")
        self.assertEqual(convert(899,15),"3EE")
        self.assertEqual(convert(25600,15),"78BA")
        self.assertEqual(convert(151,15),"A1")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
        self.assertEqual(convert(50,16),"32")
        self.assertEqual(convert(768,16),"300")
        self.assertEqual(convert(479,16),"1DF")

if __name__ == "__main__":
        unittest.main()
