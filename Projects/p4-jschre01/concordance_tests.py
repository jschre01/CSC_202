import unittest
import filecmp
from concordance import *
import time

class TestList(unittest.TestCase):

   def test_01(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file1.txt")
       conc.write_concordance("file1_con.txt")
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

   def test_02(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file2.txt")
       conc.write_concordance("file2_con.txt")
       self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

   def test_03(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("declaration.txt")
       conc.write_concordance("declaration_con.txt")
       self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

   def test_FileNotFoundError1(self):
       conc = Concordance()
       with self.assertRaises(FileNotFoundError): conc.load_stop_table("not_a_stop_words.txt")

   def test_FileNotFoundError2(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       with self.assertRaises(FileNotFoundError): conc.load_concordance_table("not_even_a_file.txt")

   def test_empty_input(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("empty.txt")
       conc.write_concordance("empty_con.txt")
       self.assertTrue(filecmp.cmp("empty_con.txt", "empty_soln.txt"))

   def test_punctuation(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("punctuation.txt")
       conc.write_concordance("punctuation_con.txt")
       self.assertTrue(filecmp.cmp("punctuation_con.txt", "empty_soln.txt"))

   def test_single_line_duplicate_words(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file3.txt")
       conc.write_concordance("file3_con.txt")
       self.assertTrue(filecmp.cmp("file3_con.txt", "file3_sol.txt"))

   def test_file_large_single_duplicate(self):
       file = open("the_file.txt", "w+")
       for i in range(50000):
           for j in range(20):
               file.write("the ")
           file.write("\n")
       file.close()

   def test_file_large_single_duplicate_solution_generator(self):
       file = open("the_file_sol.txt", "w+")
       file.write("the:")
       for i in range(50000):
           file.write(" ")
           file.write(str(i + 1))
       file.close()

   def test_the_file(self):
       start_time = time.time()
       conc = Concordance()
       conc.load_stop_table("empty.txt")
       conc.load_concordance_table("the_file.txt")
       conc.write_concordance("the_file_con.txt")
       self.assertTrue(filecmp.cmp("the_file_con.txt", "the_file_sol.txt"))
       end_time = time.time()
       print("The")
       print(end_time - start_time)

   def test_dic(self):
       start_time = time.time()
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("dic_a-c.txt")
       conc.write_concordance("dic_a-c_con.txt")
       self.assertTrue(filecmp.cmp("dic_a-c_con.txt", "dic_a-c_sol.txt"))
       end_time = time.time()
       print("Dic")
       print(end_time - start_time)
            

if __name__ == '__main__':
   unittest.main()
