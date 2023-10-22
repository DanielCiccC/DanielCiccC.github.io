# Tutorial 12
### **ALWAYS A HUFFMAN ENCODING QUESTION IN THE EXAM**

### Test compression and encoding tries
- Compress string to smaller string
  - Why? Saves memory usage
- Each letter maps to a binary code
  - 0 for left child
  - 1 for right child
- Binary code: path from root to external 
leaf
- What is the word: 010110010

![Alt text](assets\IMG167.PNG)

### Tree optimisation and Huffman's Algorithm
- Purpose: Minimise size of encoding
- Idea: Frequent letters have shorter codes
- Run time: O(n + d∙log d)
  - n: size of text
  - d: number of distinct characters
    - Have to merge d subtrees
  - Priority queue is implemented using a heap

### Huffman's Algorithm
1. Calculate frequency of each character
2. Add each character to a Priority Queue
  - Key: Frequency of character/tree
  - Value: The tree
1. Until Priority Queue’s size is less than 1
  - Remove the 2 smallest elements from the priority queue
  - Create a binary tree with the 2 elements.
  - Add the binary tree with updated priority key to the priority queue

### Huffman algorithm: example

WORD: Abracadabra
|**Character**| a|b|c|d|r|
|---|---|---|---|---|---|
**Frequency**| 5|2|1|1|2

![Alt text](assets\IMG168.PNG)

- normally need 88 bits (11 x 8 bits)
- only need 23 bits
- New encoding: 0 110 111 0 100 0 101 0 110 111 0
  - Size: 23
