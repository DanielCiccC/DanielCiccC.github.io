
# Import helper libraries
import sys
import argparse
import time

# Import our data structures
from structures.m_extensible_list import ExtensibleList
from structures.m_stack import EStack, LStack
from structures.m_single_linked_list import SingleLinkedList, SingleNode
from execute_refgrid import RefGrid

# The RefGrid object that we will operate on
my_refgrid = RefGrid()

# Task 2.1: Reverse-k
arg = 'data/another.refgrid'
# Read the refgrid to a linked list
my_refgrid.read_to_linkedlist(arg)
# my_refgrid.read_to_extlist(arg)
# my_refgrid.reverse_seq(10)
# print('\n')
pattern = 'ga'
target = 'a'
my_refgrid.cut_and_splice(pattern, len(pattern), target, len(target))

# print(my_refgrid.is_viable())
# print(my_refgrid.stringify_linkedlist(), end="")
print(my_refgrid.stringify_spliced_linkedlist(), end="")
