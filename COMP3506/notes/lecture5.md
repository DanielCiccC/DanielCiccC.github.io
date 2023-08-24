# Lecture 5

## Priority queues
### ADT
- Each entry is a pair (key, value)
- Main methods
  - ``insert(k,v)``
  - ``removeMin()``
- Additional methods
  - ``min()``
  - ``size()``, ``isEmpty()``

- Queue
  - FIFO
- Priority Queue
  - Elements are stored as Entries
  - Entry with the highest priority is stored first

![Alt text](assets/IMG46.PNG)

- An entry in a key is a key-value pair
- Can override the less than $\lt$ operator to compare entries

```python
class entry:
def __init__(self, k, v):
    self._key = k
    self._value = v

def __lt__(self, other):
    return self._key < other._key

def get_key(self):
    return self._key
```

- Imposing a total order on your keys means that trees are representing a kind of *ordered map*
  - however, true maps require *key-uniqueness*


### Comparator ADT
```python
# 2D coordinate class stub
class point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    # Less than ‘<‘ operator
    def __lt__(self, other): 
        xa = self.get_x()
        ya = self.get_y()
        xb = other.get_x()
        yb = other.get_y()
    if xa == xb:
        return ya < yb
    return xa < xb

```

### Sequence-based priority queue
- Implementation with an unsorted list
  - Insertion takes $O(1)$ time
  - ``removemin()`` and ``min()`` take $O(n)$ time

- Implementation with a sorted list
    - ``Insert(p)`` take $O(n)$ time
    - ``RemoveMin()`` and ``min()`` take $O(1)$ time

## Heaps
- Binary tree storing keys
- **Heap order**: the key of the node is $\ge$ the key of its parent
- Has to be a **complete binary tree**
  - at height $h$, the internal nodes are to the left of the external nodes
- **Last node** of a heap is the rightmost nodes of maximum depth

### Insertion into a heap
- **Insert** in the PQ ADT corresponds to inserting key $k$ into the heap
- Insertion algorithm:
  1. Find the insertion node $z$

### Upheap
- After inserting a new key $k$, the heap-order property (child nodes must have keys >= their parents) may be violated
- Since a heap has height $O(\log n)$ upheap runs in $O(\log n)$ time
  - worst case you swap all the way up the tree, which is length $\log n$

### Downheap
- Because height of tree is $\log n$, downheap runs in $O(\log n)$
- ``removeMin()`` corresponds to removing the root (smallest key) from the heap
- Algorithm:
  - Swap the last position with the root, and retrieve the node

### INserting another node
- Depends on how the binary tree is implemented. With a linkedlist, $O( 2 \log n)$ (traversing up the tree and back down again)
- Using an array:
  - For a node at index $i$:
    - left child is at the index $2i+1$
    - right child is at the index $2i + 2$
    - ``removeMin()`` corresponds to removing/swapping at index $n-1$, plus more swapping
    - Upheap and downheap operating correspond to swapping

### Heap-sort
- Take $n$ items, insert and ``removeMin()`` in $\log n$ time
- Heap-based priority queue can sort a sequence of $n$ elements in $n \log n$ time

### Heap construction
- Construct a heap containing $n$ items
- Using *Insert*
- **Bottom-up heap construction** : UPDATE THIS


### Analysis
- Worst-case time of a downheap with a proxy path
  - Worst case amount of work for each individual downheap has to participate
- The total number of nodes of the proxy paths is $O(n)$
- Bottom-up heap construction runs in $O(n)$ time

### Summary:
||
|---|---
|$O(n)$ | space
|$O(n)$ | build
|$O(\log n)$ | ``getMin()``
<!-- | $O(\log n)$ |  -->

## Adaptable priority queues
- Sometimes want to be able to remove any arbitrary element
### ADT Adaptable Priority Queue
|**Method**|**Description**
|---|---
|``remove(e)`` | remove an arbitrary element
|``replaceKey(e, k)`` | Essentially a priority update
| ``replaceValue(e, v)`` | changing the value of the item

![Alt text](assets/IMG47.PNG)


### Locating entries
- ``remove(), replaceKey(e, v)`` and ``replaceValue(e, v)`` need fast ways of locating an entry $e$ in a priority queue
- Can search the entire queue
  - Are faster methods
- Position in the data structure 

### Location-Aware Entries
- Locators can be used to keep track of 
elements as they are moved around 
inside a container
-  That is, keep “pointers” to keys inside 
the tree that follow each (key, value) 
node as they move around

### List implementation
- Location-aware list entry is an object storing
  - key
  - value
  - position (or rank) of the item in the list
- In turn, the position (or array cell) stores the entry
-  Back pointers (or ranks) are updated during swaps