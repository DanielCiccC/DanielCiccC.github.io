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

### Inserting another node
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

|Performance
|---
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

### Min-heap vs maxheap
**Min-heap**
- ``key(i) >= Key(parent(i))``
- can ``getMin()`` in constant time $O(1)$
- ``removeMin()`` in $O(\log n)$ time

Can we do ``removeMin()`` in $O(1)$?
- A: Yes, but mostly out of scope for this course.
Generally (and a very interesting point)
- You can *never* have *both* $O(1)$ insert and $O(1)$ removeMin in the same DS.
  - Could sort in $O(n)$. We have proven this is not possible

## Maps
- Searchable collection of key-value entries
- Main operations
  - searching, inserting and deleting items
- Keys must be unique
  - cannot have multiple entries with same key
- Applications
    - address book
    - student-record database

### Map-ADT

**Function** | **Description**
|---|---|
| ``get(k)`` |
| ``put(k, v)`` |
| ``remove(k)``  |
| ``size()``|
| ``isEmpty()`` |
| ``entrySet()`` | yield a collection of key/value pairs - python ``items()``
| ``keySet()`` | yield an collection of keys
| ``values()`` | yield a collection of values

### Use of Null as Sentinel
- something we store when we don't have something there
  - get, put and remove return null 
(None) if a requested entry is not  present
- None is a sentinel value
  -  Thus, we cannot store None as a key!
- Alternative: throw an exception for a key that is not in the map

![Alt text](assets/IMG50.PNG)

``put(2, e)``: this particular implementation returns the old value

### Comparison with Earlier Data Structures
- Priority queues and maps both store key-value pairs
  - We call these key-value pairs entries-
-  Keys
   - Map keys must be *unique*
   - Priority queue allows multiple entries to have same key
     - Two or more elements may share the same priority of course!
- Total order relation on keys
  - Required for priority queues
  - Optional for maps (may or may not be ordered)-
- Accessing elements
  - Maps allow access to any entry by key
  - Priority queues allow access to highest priority element

### Simple List-Based Map
Implemented using an unsorted list 
- Store the items of the map in a list $S$ (based on a 
doubly-linked list), in arbitrary order

![Alt text](assets/IMG51.PNG)

- How are you going to find the key?

``get(k)`` Algorithm. Complexity: $O(n)$
```
Algorithm get(k):
  B = S.positions() {B is an iterator of the positions in S}
  while  B.hasNext()  do
    p = B.next() { the next position in B }
    if  p.element().getKey() = k  then
      return  p.element().getValue()
  return  null {there is no entry with key equal to k}
```

``put(k)`` Algorithm. Complexity: $O(n)$
```
Algorithm put(k, v):
  B = S.positions()
  while  B.hasNext()  do
    p = B.next()
    if  p.element().getKey() = k  then
      t = p.element().getValue()
      S.set(p,(k,v))
      return  t {return the old value}
  S.addLast((k,v))
  n = n + 1  {increment variable storing number of entries}
  return  null {there was no entry with key equal to k}
```
## Multimaps
- Can store multiple entries with the same key
- 'Remove all the elements with a given key'

## Sets
- Set – unordered collection of elements, without 
duplicates
  -  elements of a set are like keys of a map, but without 
any auxiliary values
- Multiset (alias *Bag*) – set-like container that 
allows duplicates
  - Likely never need to use that, but could come in handy for prime factorisation. E.g. ``{2, 2, 2, 3, 5} = 120``

### Set ADT:

|**Function name** | **Description**
|---|---
|``add(e)`` | Adds the element *e* to S (if not already present)
|``remove(e)`` | Removes the element *e* from $S$ if present
|``contains(e)`` | Returns whether *e* is an element of *S*
|``iterator()`` | Returns an iterators of the elements of *S*
|``addAll(T)`` | Updates $S$ to include all elements of set $T$, essentially $S \cup T$
|``retainAll(T)`` | Updates $S$ so that is only keeps elements that are also elements of set $t$, Effectively replacing $S$ by $S \cap T$ 
|``removeAll(T)`` | Updates by removing any of its elements that also occur in set $T$, essentially $S - T$

## Intuition: Union on sorted lists
Generalised merge of  two sorted lists A and B
 - Auxiliary methods
  - ``remove_first``
-  Runs in $O(n_{A} + n_{B})$ time assuming the auxiliary methods run in $O(1)$ time
