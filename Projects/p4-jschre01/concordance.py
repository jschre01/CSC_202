from hash_quad import *
import string
import errno
import os
import os.path
import time
from os import path

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        if(path.exists(filename)):
            self.stop_table = HashTable(191)
            file = open(filename, "r")
            for line in file:
                new_entry = ''
                i = 0
                while(i < len(line) and line[i] != "\n"):
                    new_entry += line[i]
                    i += 1
                self.stop_table.insert(new_entry, None)
            file.close()
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)
        
    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        if(path.exists(filename)):
            self.concordance_table = HashTable(191)
            line_str = ''
            file = open(filename, "r")
            line_number = 0
            for line in file:
                line_number += 1
                for i in range(len(line)):
                    if(line[i] in string.ascii_lowercase):
                        line_str += line[i]
                    elif(ord(line[i]) == 32):
                        line_str += line[i]
                    elif(line[i] in string.ascii_uppercase):
                        line_str += chr(ord(line[i]) + 32)
                    elif(line[i] == "-" or line[i] == "/"):
                        line_str += ' '
                word_list = line_str.split(" ")
                for i in word_list:
                    if(self.stop_table.in_table(i) == False and i != ''):
                        self.concordance_table.insert(i, line_number)
                line_str = ''
            file.close()
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        new_file = open(filename, "w+")
        if(self.concordance_table.get_num_items() == 0):
            new_file.close()
        else:
            conc_list = self.concordance_table.get_all_keys()
            conc_list.sort()
            for i in conc_list:
                new_file.write(i)
                new_file.write(":")
                val = self.concordance_table.get_value(i)
                for j in val:
                    new_file.write(" ")
                    new_file.write(str(j))
                if(i != conc_list[-1]):
                    new_file.write("\n")
            new_file.close()    
