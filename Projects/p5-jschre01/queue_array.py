
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.front = 0
        self.back = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return (self.num_items == 0)


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return (self.num_items == self.capacity)


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if(self.is_full() == False):
            if(self.is_empty()):
                self.items[self.back] = item
            elif(self.back + 1 == self.capacity):
                self.items[0] = item
                self.back = 0
            else:
                self.back += 1
                self.items[self.back] = item
            self.num_items += 1
        else:
            raise IndexError("List is full")

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if(self.is_empty() == False):
            if(self.front + 1 == self.capacity):
                value = self.items[self.front]
                self.front = 0
                self.num_items -= 1
                return value
            elif(self.size() == 1):
                value = self.items[self.front]
                self.num_items -= 1
                return value
            else:
                value = self.items[self.front]
                self.front += 1
                self.num_items -= 1
                return value
        else:
            raise IndexError("List is empty")


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items

