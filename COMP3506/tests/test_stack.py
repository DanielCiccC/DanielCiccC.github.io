"""
Author: ThomasH
"""

# Import helper libraries
import sys
import argparse
import time
import random

# Import our data structures
from structures.m_extensible_list import ExtensibleList
from structures.m_stack import EStack, LStack
from structures.m_single_linked_list import SingleNode, SingleLinkedList

def esetup():
    estack = EStack()
    for i in range(1, 4):
        estack.push(i)
        
    return estack

def test_einit():
    estack = EStack()
    assert(estack.get_size() == 0)
    assert(estack.get_capacity() == 4)
    assert(estack._data[0] == None)
    assert(estack._data[1] == None)
    assert(estack._data[2] == None)
    assert(estack._data[3] == None)
    print(f'test {test_einit.__name__} passed \n' + '*' * 30)

def test_epush():
    estack = esetup()
    assert(estack.get_at(0) == 1)
    assert(estack.get_at(1) == 2)
    assert(estack.get_at(2) == 3)
    print(f'test {test_epush.__name__} passed \n' + '*' * 30)

def test_epop():
    estack = esetup()
    assert(estack.pop() == 3)
    assert(estack.pop() == 2)
    assert(estack.pop() == 1)
    print(f'test {test_epop.__name__} passed \n' + '*' * 30)

def test_epeek():
    estack = esetup()
    assert(estack.peek() == 3)
    estack.push("World")
    estack.push("Hello")
    assert(estack.peek() == "Hello")
    estack.pop()
    assert(estack.peek() == "World")
    print(f'test {test_epeek.__name__} passed \n' + '*' * 30)

def test_eempty():
    estack = esetup()
    assert(estack.empty() == False)
    estack = EStack()
    assert(estack.empty() == True)
    print(f'test {test_eempty.__name__} passed \n' + '*' * 30)

def lsetup():
    lstack = LStack()
    for i in range(1, 4):
        lstack.push(i)
        
    return lstack

def test_linit():
    lstack = LStack()
    assert(lstack._head == None)
    assert(lstack._size == 0)
    print(f'test {test_linit.__name__} passed \n' + '*' * 30)

def test_lpush():
    lstack = lsetup()
    assert(lstack.get_head().get_data() == 3)
    assert(lstack.get_head().get_next().get_data() == 2)
    assert(lstack.get_head().get_next().get_next().get_data() == 1)
    print(f'test {test_lpush.__name__} passed \n' + '*' * 30)

def test_lpop():
    lstack = lsetup()
    assert(lstack.pop() == 3)
    assert(lstack.pop() == 2)
    assert(lstack.pop() == 1)
    print(f'test {test_lpop.__name__} passed \n' + '*' * 30)

def test_lpeek():
    lstack = lsetup()
    assert(lstack.peek() == 3)
    lstack.push("World")
    lstack.push("Hello")
    assert(lstack.peek() == "Hello")
    lstack.pop()
    assert(lstack.peek() == "World")
    print(f'test {test_lpeek.__name__} passed \n' + '*' * 30)

def test_lempty():
    lstack = lsetup()
    assert(lstack.empty() == False)
    lstack2 = LStack()
    assert(lstack2.empty() == True)
    print(f'test {test_lempty.__name__} passed \n' + '*' * 30)

if __name__ == "__main__":
    print("==== Executing Stack Tests ====")
    test_einit()
    test_epush()
    test_epop()
    test_epeek()
    test_eempty()
    test_linit()
    test_lpush()
    test_lpop()
    test_lpeek()
    test_lempty()
    print('=' * 30 + '\n All tests passed. \n' + '=' * 30)