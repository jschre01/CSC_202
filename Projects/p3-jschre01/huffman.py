import errno
import os
import os.path
from os import path


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if(a.freq < b.freq):
        return True
    elif(a.freq == b.freq):
        if(a.char < b.char):
            return True
        else:
            return False
    else:
        return False

    
def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    comb_freq = a.freq + b.freq
    if(a.char < b.char):
        comb_char = a.char
    else:
        comb_char = b.char
    new_node = HuffmanNode(comb_char, comb_freq)
    new_node.set_left(a)
    new_node.set_right(b)
    return new_node
    
def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    freq_list = [0]*256
    file = open(filename, "r")
    for line in file:
        for i in range(len(line)):
            freq_list[ord(line[i])] += 1
    file.close()
    return freq_list
def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    node_count = 0
    node_list = []
    for i in range(len(char_freq)):
        if(char_freq[i] != 0):
            new_node = HuffmanNode(i, char_freq[i])
            if(len(node_list) == 0):
                node_list.append(new_node)
            else:
                j = 0
                flagbool = False
                while(comes_before(new_node, node_list[j]) == False and flagbool == False):
                    if(j == len(node_list) - 1):
                        flagbool = True
                        node_list.append(new_node)
                    else:
                        j += 1
                if(flagbool == False):
                    node_list.insert(j, new_node)
    while(len(node_list) > 1):
        a = node_list.pop(0)
        b = node_list.pop(0)
        new_huff = combine(a, b)
        if(len(node_list) == 0):
            node_list.append(new_huff)
        else:
            k = 0
            flagbool_2 = False
            while(comes_before(new_huff, node_list[k]) == False and flagbool_2 == False):
                if(k == len(node_list) - 1):
                    flagbool_2 = True
                    node_list.append(new_huff)
                else:
                    k += 1
            if(flagbool_2 == False):
                node_list.insert(k, new_huff)
    return node_list[0]     
            


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    Huffman_list = [''] * 256
    Huffman_list = create_code_helper(node, Huffman_list, "")
    return Huffman_list

def create_code_helper(node, code_list, code):
    if(node.right == None and node.left == None):
        code_list[node.char] = code
        return code_list
    else:
        if(node.left != None):
            create_code_helper(node.left, code_list, code + '0')
        if(node.right != None):
            create_code_helper(node.right, code_list, code + '1')
    return code_list

def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return "97 3 98 4 99 2" """
    output = ''
    for i in range(len(freqs)):
        if(freqs[i] != 0):
            if(output == ''):
                output = str(i) + ' ' + str(freqs[i])
            else:
                output = output + ' ' + str(i) + ' ' + str(freqs[i])
    return output

def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    if(path.exists(in_file)):
        freq_list = cnt_freq(in_file)
        flagbool = False
        for i in freq_list:
            if(i != 0):
                flagbool = True
        if(flagbool == True):
            Huffman_tree = create_huff_tree(freq_list)
            Huffman_list = create_code(Huffman_tree)
            header = create_header(freq_list)
            output = ''
            file = open(in_file, "r")
            for line in file:
                for i in range(len(line)):
                    output += Huffman_list[ord(line[i])]
            file.close()
            new_file = open(out_file, "w+")
            new_file.write(header + "\n")
            new_file.write(output)
            new_file.close()
        else:
            new_file_empty = open(out_file, "w+")
            new_file_empty.close()
            
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), in_file)
        

def huffman_decode(encoded_file, decode_file):
    "Takes input file name and output file name as parameters, decodes encoded file back to original"
    if(path.exists(encoded_file)):
        header = ''
        encoded = ''
        file = open(encoded_file, "r")
        for line in file:
            if(' ' in line):
                for i in range(len(line)):
                    header = header + line[i]
            else:
                for i in range(len(line)):
                    encoded = encoded + line[i]
        file.close()
        if(header == '' and encoded == ''):
            new_file = open(decode_file, "w+")
            new_file.close()
        elif(encoded == ''):
            new_file = open(decode_file, "w+")
            freq_list = parse_header(header)
            for k in range(len(freq_list)):
                if(freq_list[k] != 0):
                    for i in range(freq_list[k]):
                        new_file.write(chr(k))
            new_file.close()
        else:
            freq_list = parse_header(header)
            root = create_huff_tree(freq_list)
            curr_node = root
            new_file = open(decode_file, "w+")
            for j in range(len(encoded)):
                if(curr_node.right == None and curr_node.left == None):
                    new_file.write(chr(curr_node.char))
                    curr_node = root
                    if(encoded[j] == '0'):
                        if(curr_node.left != None):
                            curr_node = curr_node.left
                    elif(encoded[j] == '1'):
                        if(curr_node.right != None):
                            curr_node = curr_node.right
                elif(len(encoded) == j + 1):
                    if(encoded[j] == '0'):
                        if(curr_node.left != None):
                            curr_node = curr_node.left
                    elif(encoded[j] == '1'):
                        if(curr_node.right != None):
                            curr_node = curr_node.right
                    new_file.write(chr(curr_node.char))
                else:
                    if(encoded[j] == '0'):
                        if(curr_node.left != None):
                            curr_node = curr_node.left
                    elif(encoded[j] == '1'):
                        if(curr_node.right != None):
                            curr_node = curr_node.right
            new_file.close()
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), encoded_file)


def parse_header(header_string):
    "Takes input string and adds elements of string to a list of frequencies"
    freq_list = [0] * 256
    header = header_string.split(' ')
    char = None
    for i in range(len(header)):
        if(i % 2 == 0):
            char = int(header[i])
        else:
            freq_list[char] = int(header[i])
    return freq_list
        
