"""
author: DanielCiccC
"""

# Import helper libraries
import sys
import argparse
import time
import random
import unittest

# Import our data structures
from structures.m_extensible_list import ExtensibleList
from structures.m_stack import EStack, LStack
from structures.m_single_linked_list import SingleNode, SingleLinkedList

class MyTestCase(unittest.TestCase):
    def increase_size(self, ext_list, elements):
        for i in elements:
            ext_list.append(i)
        return ext_list

    def setup(self, len=None):
        ext_list = ExtensibleList()
        
        elements = len
        if len == None:
            elements = 10000
        
        for i in range(elements):
            ext_list.append(i)  
        return ext_list

    def test_str(self):
        ext_list = ExtensibleList()
        assert(str(ext_list) == '[None], [None], [None], [None]')
        ext_list = self.setup(5)
        assert(str(ext_list) == '0, 1, 2, 3, 4, [None], [None], [None]')
        ext_list.remove(4)
        assert(str(ext_list) == '0, 1, 2, 3, [None], [None], [None], [None]')

    def test_resize(self):
        ext_list = self.setup(3)
        assert(ext_list.get_capacity() == 4)
        ext_list = self.increase_size(ext_list, range(4, 9))
        # print(ext_list.get_capacity())
        assert(ext_list.get_capacity() == 8)
        ext_list = self.increase_size(ext_list, range(1))
        # print(ext_list.get_capacity())
        assert(ext_list.get_capacity() == 16)
        ext_list = self.setup(1024)
        assert(ext_list.get_capacity() == 1024)
        ext_list = self.increase_size(ext_list, range(1))
        assert(ext_list.get_capacity() == 2048)    

    def test_reset(self):
        ext_list = self.setup(5)
        assert(ext_list.get_capacity() == 8)
        assert(ext_list.get_size() == 5)
        assert(ext_list[0] == 0)
        ext_list.reset()
        assert(ext_list.get_capacity() == 4)
        assert(ext_list.get_size() == 0)
        with self.assertRaises(IndexError):
            value = ext_list[0]  # This will raise an IndexError

    def test_dunder_get(self):
        ext_list = ExtensibleList()
        with self.assertRaises(IndexError):
            value = ext_list[0]  # This will raise an IndexError
        # assert ext_list[0] result in index error
        ext_list.append(0)
        assert(ext_list[0] == 0)
        with self.assertRaises(IndexError):
            value = ext_list[1]  # This will raise an IndexError
        with self.assertRaises(IndexError):
            value = ext_list[-1]  # This will raise an IndexError
        # assrt ext_list[1] result in IndexError
        # assert ext_list[-1] result in IndexError
        ext_list.reset()
        with self.assertRaises(IndexError):
            value = ext_list[0]  # This will raise an IndexError
        #assert ext_list[0] result in IndexError
        ext_list = self.setup(7)
        assert(ext_list[6] == 6)
        with self.assertRaises(IndexError):
            value = ext_list[7]  # This will raise an IndexError
        # assert() ext_list[7] result in IndexError

    def test_get_at(self):
        ext_list = ExtensibleList()
        assert(ext_list.get_at(0) == None)
        assert(ext_list.get_at(4) == None)
        ext_list.append(10)
        assert(ext_list.get_at(0) == 10)
        ext_list = self.setup(7)
        assert(ext_list.get_at(4) == 4)
        assert(ext_list.get_at(-1) == None)
        ext_list = self.setup(4)
        assert(ext_list.get_at(0) == 0)
        assert(ext_list.get_at(4) == None)

    def test_dunder_set(self):
        ext_list = ExtensibleList()
        # with self.assertRaises(IndexError):
        ext_list[0] = 0 
        ext_list[3] = 4 
        ext_list[-1] = 1 
        ext_list[4]  = 1
        assert(str(ext_list) == '[None], [None], [None], [None]')
        ext_list = self.setup(4)
        ext_list[0] = 4
        assert(ext_list[0] == 4)
        ext_list[4] = 1 # This will raise an IndexError     
        assert(str(ext_list) == '4, 1, 2, 3')  
        

    def test_set_at(self):
        ext_list = ExtensibleList()
        ext_list.set_at(0, 1)
        ext_list.set_at(3, 4)
        ext_list.set_at(-1, 1)
        ext_list.set_at(4, 1)
        assert(str(ext_list) == '[None], [None], [None], [None]') #None of the above should work
        ext_list = self.setup(4)
        ext_list.set_at(0, 4)
        ext_list.set_at(2, 4)
        assert(ext_list.get_at(0) == 4)
        assert(str(ext_list) == '4, 1, 4, 3')  

    def test_append(self):
        ext_list = ExtensibleList()
        ext_list.append(0)
        assert(ext_list[0] == 0)
        with self.assertRaises(IndexError):
            value = ext_list[1] # This will raise an IndexError 
        assert(ext_list.get_at(1) == None)
        with self.assertRaises(IndexError):
            value = ext_list[3] # This will raise an IndexError 
        ext_list = self.setup(8)
        assert(ext_list.get_at(1) == 1)

    def test_remove(self):
        ext_list = ExtensibleList()
        ext_list.append(0)
        assert(ext_list.get_at(0) == 0)
        ext_list.remove(0)
        assert(ext_list.get_at(0) == None)
        ext_list = self.setup(8)
        ext_list.remove(2)
        # print(ext_list)
        assert(str(ext_list) == '0, 1, 3, 4, 5, 6, 7, [None]')
        assert(ext_list.get_size() == 7)
        assert(ext_list.get_capacity() == 8)
        ext_list = self.setup(4)
        ext_list.remove(2)
        assert(ext_list.get_capacity() == 4)

    def test_remove_at(self):
        ext_list = ExtensibleList()
        assert(ext_list.remove_at(0) == None)
        ext_list = self.setup(4)
        assert(ext_list.remove_at(1) == 1)
        assert(ext_list.get_size() == 3)
        assert(ext_list.remove_at(-1) == None)
        assert(ext_list.get_size() == 3)
        assert(ext_list.get_at(3) == None)
        ext_list.append(5)
        assert(ext_list.remove_at(3) == 5)
        
    def test_is_empty(self):
        ext_list = ExtensibleList()
        assert(ext_list.is_empty())
        ext_list.append(0)
        assert(not ext_list.is_empty())
        ext_list.remove_at(-1)
        assert(not ext_list.is_empty())
        ext_list.remove_at(0)
        assert(ext_list.is_empty())

    def test_is_full(self):
        ext_list = ExtensibleList()
        assert(ext_list.is_full() is False)
        ext_list.append(0)
        assert(ext_list.is_full() is False)
        ext_list.append(0)
        assert(ext_list.is_full() is False)
        ext_list.append(0)
        assert(ext_list.is_full() is False)
        ext_list.append(0)
        assert(ext_list.is_full())
        ext_list.remove_at(3)
        assert(ext_list.is_full() is False)
        ext_list = self.setup(7)
        assert(ext_list.is_full() is False)
        ext_list = self.setup(8)
        assert(ext_list.is_full())
            
    def test_get_size(self):
        ext_list = ExtensibleList()
        assert(ext_list.get_size() == 0)
        ext_list = self.setup(4)
        assert(ext_list.get_size() == 4)
        ext_list = self.setup(10000)
        assert(ext_list.get_size() == 10000)

    def test_get_capacity(self):
        ext_list = ExtensibleList()
        assert(ext_list.get_capacity() == 4)
        ext_list = self.setup(4)
        assert(ext_list.get_capacity() == 4)
        ext_list.append(0)
        assert(ext_list.get_capacity() == 8)
        ext_list = self.setup(1024)
        assert(ext_list.get_capacity() == 1024)
        ext_list.append(1024)
        assert(ext_list.get_capacity() == 2048)

if __name__ == "__main__":
    print ("==== Executing Extensible List Tests ====")
    test = MyTestCase()
    test.test_str()
    test.test_resize()
    test.test_reset()
    test.test_dunder_get()
    test.test_get_at()
    test.test_dunder_get()
    test.test_get_at()
    test.test_dunder_set()
    test.test_set_at()
    test.test_append()
    test.test_remove()
    test.test_remove_at()
    test.test_is_empty()
    test.test_is_full()
    test.test_get_size()
    test.test_get_capacity()
    print( '=' *30)
    print('\n All tests passed. \n' + '=' * 30)
