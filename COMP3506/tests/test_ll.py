"""
author: DanielCiccC
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

def setup(len=None):
    
    linked_list = SingleLinkedList()
    
    elements = len
    if len == None:
        elements = 10000
    
    for i in range(elements):
        linked_list.insert_to_front(SingleNode(i))
    
    return linked_list
    

def test_init():
    # setup() no setup in this one
    linked_list = SingleLinkedList()
    assert(linked_list._head == None)
    assert(linked_list._size == 0)
    print(f'test {test_init.__name__} passed \n' + '*' * 30)
    
def test_str():
    ll = setup(5)
    # print(ll.__str__)
    assert(str(ll) == '4 -> 3 -> 2 -> 1 -> 0 -> [EOL]')
    ll = SingleLinkedList()
    # print(ll)
    assert(str(ll) == '[EOL]')
    print(f'test {test_str.__name__} passed \n' + '*' * 30)

def test_traverse_and_delete():
    ll = setup()
    ll.traverse_and_delete()
    assert(ll._head == None)
    assert(ll._size == 0)
    ll = SingleLinkedList() #an empty single linked list
    ll.traverse_and_delete()
    assert(ll._head == None)
    assert(ll._size == 0)
    print(f'test {test_traverse_and_delete.__name__} passed \n'  + '*' * 30)

def test_get_size():
    ll = setup()
    assert(ll.get_size() == 10000)
    ll = setup(15)
    assert(ll.get_size() == 15)
    assert(ll.get_size() == ll._size)
    ll = SingleLinkedList()
    assert(ll.get_size() == 0)
    print(f'test {test_get_size.__name__} passed \n'  + '*' * 30)
    
def test_set_size():
    ll = setup()
    ll.set_size(10)
    assert(ll.get_size() == 10)
    assert(ll.get_size() == ll._size)
    num = ll.remove_from_back()
    assert(num.get_data() == 0)
    assert(ll.get_size() == 9)
    ll = SingleLinkedList()
    ll.set_size(10)
    ll.insert_to_front(SingleNode('test'))
    assert(ll.get_size() == 11)
    print(f'test {test_set_size.__name__} passed \n'  + '*' * 30)

def test_get_head():
    ll = setup()
    assert(ll.get_head().get_data() == 9999)
    ll.remove_from_front()
    assert(ll.get_head().get_data() == 9998)
    print(f'test {test_get_head.__name__} passed \n'  + '*' * 30)
    
def test_set_head():
    ll = setup()
    ll.set_head(SingleNode('test'))
    assert(ll.get_head().get_data() == 'test')
    assert(ll.get_size() == 10000)
    print(f'test {test_set_head.__name__} passed \n'  + '*' * 30)

def test_insert_to_front():
    ll = SingleLinkedList()
    ll.insert_to_front(SingleNode('t1'))
    assert(ll.get_size() == 1)
    assert(ll.get_head().get_data() == 't1')
    
    ll = setup()
    ll.insert_to_front(SingleNode('t1'))
    assert(ll.get_size() == 10001)
    assert(ll.get_head().get_data() == 't1')
    assert(ll.find_element('t1').get_data() == 't1')
    print(f'test {test_insert_to_front.__name__} passed \n'  + '*' * 30) 

def test_insert_to_back():
    ll = SingleLinkedList()
    ll.insert_to_back(SingleNode('t1'))
    assert(ll.get_size() == 1)
    assert(ll.get_head().get_data() == 't1')
    ll = setup()
    ll.insert_to_back(SingleNode('t1'))
    assert(ll.get_size() == 10001)
    assert(ll.get_head().get_data() == 9999)
    assert(ll.find_element('t1').get_data() == 't1') #has not been tested yet
    ll.remove_from_back()
    assert(ll.get_size() == 10000)
    assert(ll.get_head().get_data() == 9999)
    print(f'test {test_insert_to_back.__name__} passed \n'  + '*' * 30)


def test_remove_from_front():
    ll = setup()
    removed_item = ll.remove_from_front() 
    assert(removed_item.get_data() == 9999)
    assert(ll.get_head().get_data() == 9998)
    assert(ll.get_size() == 9999)
    ll = SingleLinkedList()
    assert(ll.remove_from_front() == None)
    assert(ll.get_head() == None)
    assert(ll.get_size() == 0)
    print(f'test {test_remove_from_front.__name__} passed \n'  + '*' * 30)
    

def test_remove_from_back():
    ll = SingleLinkedList()
    assert(ll.remove_from_back() == None)
    assert(ll.get_head() == None)
    assert(ll.get_size() == 0)  
    ll = setup()
    assert(ll.remove_from_back().get_data() == 0)
    assert(ll.get_head().get_data() == 9999)
    assert(ll.get_size() == 9999)  
    print(f'test {test_remove_from_back.__name__} passed \n'  + '*' * 30)

def test_find_element():
    ll = SingleLinkedList()
    assert(ll.find_element('element') == None)
    assert(ll.get_head() == None)
    assert(ll.get_size() == 0)  
    
    ll.insert_to_front(SingleNode('test'))
    assert(ll.find_element('not_a_test') == None)
    assert(ll.get_head().get_data() == 'test')
    assert(ll.get_size() == 1)  
    
    assert(ll.find_element('test').get_data() == 'test')
    assert(ll.get_size() == 1)  
    print(f'test {test_find_element.__name__} passed \n'  + '*' * 30)

def test_find_and_remove_element():
    ll = SingleLinkedList()
    assert(ll.find_element('test') == None)
    assert(ll.get_head() == None)
    assert(ll.get_size() == 0)  
    
    ll.insert_to_front(SingleNode('test'))
    assert(ll.find_element('not_a_test') == None)
    assert(ll.get_head().get_data() == 'test')
    assert(ll.get_size() == 1)  
    
    assert(ll.find_element('test').get_data() == 'test')
    assert(ll.get_size() == 1)  
    print(f'test {test_find_and_remove_element.__name__} passed \n'  + '*' * 30)

def test_reverse():
    ll = setup()
    ll.reverse() #now the starting number should be 9999
    head = ll.get_head()
    num = 0 # now starting at 0, instead of 9999
    while head.get_next() is not None:
        assert(head.get_data() == num)
        num += 1
        head = head.get_next()
    print(f'test {test_reverse.__name__} passed \n'  + '*' * 30)


#teardown the linkedlist here
def teardown():
    pass

if __name__ == "__main__":
    print ("==== Executing Single List Tests ====")
    test_init()
    test_str()
    test_traverse_and_delete()
    test_get_size()
    test_set_size()
    test_get_head()
    test_set_head()
    test_insert_to_front()
    test_insert_to_back()
    test_remove_from_front()
    test_remove_from_back()
    test_find_element()
    test_find_and_remove_element()
    test_reverse()
    print( '=' *30 + '\n All tests passed. \n' + '=' * 30)
    