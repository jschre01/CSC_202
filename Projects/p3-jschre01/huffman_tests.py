import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_multiline_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_declaration_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_empty_textfile(self):
        huffman_encode("empty.txt", "empty_out.txt")
        err = subprocess.call("diff -wb empty_out.txt empty_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_single_duplicate_textfile(self):
        huffman_encode("single_duplicate.txt", "single_duplicate_out.txt")
        err = subprocess.call("diff -wb single_duplicate_out.txt single_duplicate_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_FileNotFoundError(self):
        with self.assertRaises(FileNotFoundError): huffman_encode("this_ain't_even_a_file.txt", "this_ain't_even_a_file_out.txt")

    def test_decode_01_textfile(self):
        huffman_decode("file1_soln.txt", "file1_original.txt")
        err = subprocess.call("diff -wb file1_original.txt file1.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_02_textfile(self):
        huffman_decode("file2_soln.txt", "file2_original.txt")
        err = subprocess.call("diff -wb file2_original.txt file2.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_multiline_textfile(self):
        huffman_decode("multiline_soln.txt", "multiline_original.txt")
        err = subprocess.call("diff -wb multiline_original.txt multiline.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_declaration_textfile(self):
        huffman_decode("declaration_soln.txt", "declaration_original.txt")
        err = subprocess.call("diff -wb declaration_original.txt declaration.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_empty_textfile(self):
        huffman_decode("empty_soln.txt", "empty_original.txt")
        err = subprocess.call("diff -wb empty_original.txt empty.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_single_duplicate_textfile(self):
        huffman_decode("single_duplicate_soln.txt", "single_duplicate_original.txt")
        err = subprocess.call("diff -wb single_duplicate_original.txt single_duplicate.txt", shell = True)
        self.assertEqual(err, 0)

    def tests_decode_FileNotFoundError(self):
        with self.assertRaises(FileNotFoundError): huffman_decode("this_ain't_even_a_file_soln.txt", "this_ain't_even_a_file_original.txt")

                
if __name__ == '__main__': 
   unittest.main()
