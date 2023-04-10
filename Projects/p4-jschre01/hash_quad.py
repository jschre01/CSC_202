class HashEntry:

    def __init__(self, key):
        self.key = key
        self.Value = []



class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        keys list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table)
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        ind = self.horner_hash(key)
        if(self.hash_table[ind] == None):
            new_entry = HashEntry(key)
            new_entry.Value.append(value)
            self.hash_table[ind] = new_entry
            self.num_items += 1
        elif(self.hash_table[ind].key == key):
            if(self.hash_table[ind].Value[-1] != value):
                self.hash_table[ind].Value.append(value)
        elif(self.hash_table[ind] == None):
            new_entry = HashEntry(key)
            new_entry.Value.append(value)
            self.hash_table[ind] = new_entry
            self.num_items += 1
        elif(self.in_table(key)):
            new_ind = self.get_index(key)
            if(self.hash_table[new_ind].Value[-1] != value):
                self.hash_table[new_ind].Value.append(value)
        else:
            new_ind = self.quad_probe(ind)
            new_entry = HashEntry(key)
            new_entry.Value.append(value)
            self.hash_table[new_ind] = new_entry
            self.num_items += 1
            
                
            '''ind = self.horner_hash(key)
            if(self.hash_table[ind] == None):
                new_entry = HashEntry(key)
                new_entry.Value.append(value)
                self.hash_table[ind] = new_entry
                self.num_items += 1
            else:
                new_ind = self.quad_probe(ind)
                new_entry = HashEntry(key)
                new_entry.Value.append(value)
                self.hash_table[new_ind] = new_entry
                self.num_items += 1'''
        if(self.get_load_factor() > 0.5):
                old_table = self.hash_table
                self.table_size = (self.table_size * 2) + 1
                self.hash_table = [None] * self.table_size
                self.num_items = 0
                for i in old_table:
                    if(i != None):
                        for j in i.Value:
                            self.insert(i.key, j)

    def quad_probe(self, index):
        """ Finds the correct index for an insertion or search in event of collision"""
        i = index
        mult = 1
        while(self.hash_table[i] != None):
            i = index + (mult)**2
            mult += 1
            while(i >= self.table_size):
                i = i - self.table_size
        return i
    
    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horners rule, as described in project specification."""
        ind = 0
        if(len(key) < 8):
            n = len(key)
        else:
            n = 8
        for i in range(n):
            ind += (ord(key[i]) * (31**(n-1-i)))
        ind = ind % self.table_size
        return ind
        
    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        ind = self.horner_hash(key)
        if(self.hash_table[ind] == None):
            return False
        elif(self.hash_table[ind].key == key):
            return True
        else:
            i = ind
            mult = 1
            while(self.hash_table[i] != None):
                if(self.hash_table[i].key == key):
                    return True
                else:
                    i = ind + (mult)**2
                    mult += 1
                    while(i >= self.table_size):
                        i = i - self.table_size
            return False

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        ind = self.horner_hash(key)
        if(self.hash_table[ind] == None):
            return None
        elif(self.hash_table[ind].key == key):
            return ind
        else:
            i = ind
            mult = 1
            while(self.hash_table[i] != None):
                if(self.hash_table[i].key == key):
                    return i
                else:
                    i = ind + (mult)**2
                    mult += 1
                    while(i >= self.table_size):
                        i = i - self.table_size
            return None
        
    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        out_list = []
        for i in range(len(self.hash_table)):
            if(self.hash_table[i] != None):
                out_list.append(self.hash_table[i].key)
        return out_list
    
    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        ind = self.get_index(key)
        if(ind == None):
            return None
        else:
            return self.hash_table[ind].Value

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items
     
    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size
    
    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return (self.num_items/self.table_size)
        
