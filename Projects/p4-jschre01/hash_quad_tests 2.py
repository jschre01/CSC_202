import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        self.assertEquals(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        self.assertEquals(ht.get_num_items(), 0)

    def test_01c(self):
        ht = HashTable(7)
        self.assertAlmostEquals(ht.get_load_factor(), 0)

    def test_01d(self):
        ht = HashTable(7)
        self.assertEquals(ht.get_all_keys(), [])

    def test_01e(self):
        ht = HashTable(7)
        self.assertEquals(ht.in_table("cat"), False)

    def test_01f(self):
        ht = HashTable(7)
        self.assertEquals(ht.get_value("cat"), None)

    def test_01g(self):
        ht = HashTable(7)
        self.assertEquals(ht.get_index("cat"), None)

    def test_01h(self):
        ht = HashTable(7)
        self.assertEquals(ht.horner_hash("cat"), 3)

    def test_02a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_table_size(), 7)

    def test_02b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_num_items(), 1)

    def test_02c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEquals(ht.get_load_factor(), 1/7)

    def test_02d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_all_keys(), ["cat"])

    def test_02e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.in_table("cat"), True)

    def test_02f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_value("cat"), [5])

    def test_02g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_index("cat"), 3)

    def test_03(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        self.assertEquals(ht.get_value("cat"), [5, 17])

    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEquals(ht.get_index("cat"), 3)

        ht.insert("dog", 8)
        self.assertEquals(ht.get_num_items(), 2)
        self.assertEquals(ht.get_index("dog"), 6)
        self.assertAlmostEquals(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", 10)
        self.assertEquals(ht.get_num_items(), 3)
        self.assertEquals(ht.get_index("mouse"), 4)
        self.assertAlmostEquals(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", 12) # hash table should be resized
        self.assertEquals(ht.get_num_items(), 4)
        self.assertEquals(ht.get_table_size(), 15)
        self.assertAlmostEquals(ht.get_load_factor(), 4 / 15)
        self.assertEquals(ht.get_index("cat"), 12)
        self.assertEquals(ht.get_index("dog"), 14)
        self.assertEquals(ht.get_index("mouse"), 13)
        self.assertEquals(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEquals(keys, ["cat", "dog", "elephant", "mouse"])

    def test_05(self):
        ht = HashTable(10)
        ht.insert("d", 5)
        ht.insert("d",6)
        ht.insert("dd", 17)
        self.assertEquals(ht.in_table("dd"), True)

    def test_06(self):
        ht = HashTable(10)
        ht.insert("d", 5)
        ht.insert("dd", 17)
        self.assertEquals(ht.get_index("dd"), True)

    def test_07(self):
        ht = HashTable(10)
        ht.insert("d", 5)
        ht.insert("dd", 17)
        self.assertEquals(ht.get_value("dd"), [17]) 

    def test_08(self):
        ht = HashTable(5)
        ht.insert("d", 5)
        ht.insert("d",6)
        ht.insert("d",7)
        ht.insert("d",8)

        ht.insert("dd", 17)
        ht.insert("dd", 18)

        ht.insert("cd", 17)
        ht.insert("cd", 18)
        ht.insert("cd", 19)

        ht.insert("ac", 17)
        ht.insert("ac", 18)

        self.assertEquals(ht.in_table("dd"), True)

    def test_09(self):
        ht = HashTable(10)
        ht.insert("dd", "star")
        self.assertEquals(ht.get_value("dd"), ["star"])

    def test_10(self):
        ht = HashTable(10)
        ht.insert("asfsdgsgdfg", 5)
        ht.insert("asfsdgsgdfg", 7)
        ht.insert("asfsdgsgdfg", 9)
        ht.insert("asfsdgsgdwttr", 5)
        ht.insert("asfsdgsgdrewrfg", 5)
        ht.insert("asfsdgsgdfg", 11)
        ht.insert("asfsdgfsfsgdfg", 5)
        ht.insert("asfsqwerdgsgdfg", 5)

        self.assertEquals(ht.get_value("asfsdgsgdfg"), [5,7,9,11])

    def test_11(self):
        ht = HashTable(10)
        ht.insert("asfsdfg", 5)
        ht.insert("asfsdfg", 7)
        ht.insert("asfsdfg", 9)
        ht.insert("asfsdgsgdwttr", 5)
        ht.insert("asfsdgsgdrewrfg", 5)
        ht.insert("asfsdfg", 11)
        ht.insert("asfsdgfsfsgdfg", 5)
        ht.insert("asfsqwerdgsgdfg", 5)

        self.assertEquals(ht.get_value("asfsdfg"), [5,7,9,11])


if __name__ == '__main__':
   unittest.main()
