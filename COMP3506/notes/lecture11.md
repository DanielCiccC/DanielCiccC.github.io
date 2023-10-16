# Lecture 11

## Text compression
### What is compression?

- Idea: We want to reduce the size of some data. This allows faster transfer across networks, smaller footprint to store, … 
- Why: Because data is exploding!!11!

### When is compression used?

- Very often!
- Files: zip, gzip, bzip2, xz, …
- File systems: NTFS, ZFS, …
- Images: gif, jpeg, …
- Sound: mp3, …
- Videos: mpeg, divx, …
- And so on!

### Basic idea
- We are given a text M
- We encode M to generate a (hopefully) compressed representation C (M) 
- Given C (M ), we can decode it to get back M’
  - Lossless compression: M = M’
  - Lossy otherwise
- Compression ratio: bits in C(M) / bits in M
    - the smaller the value the better

### Lossy vs Lossless
Lossy compression
- Common for images, sound, video
- Often not noticed by consumers
- Typical ratio: 10% or less!

Lossless compression
- Text, source code, executables
  -  codepressing source code repository, etc.
- Typical ratios: 50%? 

### Simple Ideas and Intuition
- Look for redundancy
  - look for patterns to exploit
- Code things that occur often with fewer bits

```
GTCACCCCCCCCCGTCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCTGG
```

-  If I see a “C”, I look forwards until I see something else, and then I replace the C sequence with a count
```
= GTC1AC9GTC41TGG
```
Ratio: $(11*8 + 3*32) / (58*8)$
  Around 40% of the original!

- The more general idea here is called Run Length Encoding (RLE). 
- List the character and then the run length as a pair:

### Smarter DNA coding
- Alphabet size is 4, so we can represent 
each base (A, G, T, C) with just two bits!
- A = 00, G = 01, T = 10, C = 11
- Uses 112 bits (ignoring padding)
- That’s about 25% of the original!
- Known as a “fixed length” code
  - This would work well if they were all the same frequency
- Intuition: C turns up a lot… Shouldn’t we 
give C a shorter code word? 
- Known as a “variable length” coding
- Uses a different number of bits to 
encode each character

### Variable length codes
- Ambiguity problems
- G = 10, A = 0, C = 1, T = 11
- Given a sequence of bits: 1100
  - Is it TAA? CCAA? CGA? …
- Codewords must be prefix free

### Prefix Codes
- We can compress a string X into a smaller string Y by using a prefix code for the characters of X

- Mapping each character of an alphabet to a binary code-word
  - no code-word is the prefix of another code-word
  - Proof: No internal node is used as an endpoint
- Encoding trie represents a prefix code
  - each external node stores a character
  - code word of a character is given by the path from the root to the external node storing the character 
    - 0 for a left child and 1 for a right child

|**Codex** | **Graph** |
|---|---|
| ![Alt text](assets\IMG158.PNG) | ![Alt text](assets\IMG159.PNG) |


### Encoding Tree Optimisation
- Given a text string X, find a prefix code for the characters of X that yields the smallest possible encoding for X
  - frequent characters should have short code-words
  - rare characters should have long code-words

- X = abracadabra
- $T_{1}$ encodes X into 29 bits
  - 010 11 011 010 00 010 10 010 11 011 010
- $T_{2}$ encodes X into 23 bits
  
![Alt text](assets\IMG160.PNG)

- We want to find an optimal prefix-free coding scheme
- How do we do that? Huffman coding!

### Huffman Coding: History
Given a string X, constructs a prefix code that 
minimises the size of the encoding of X
- Given: a set of $n$ positive weights $w_{i}$
- Compute: a set of $n$ corresponding codeword lengths, $l_{i}$, such that:

$$\sum _{i=1} ^{n} 2^{-li} \le 1 \; \; \text{and}  \; \; \sum _{i=1} ^{n} w_{i} \cdot l_{i} \; \; \text{is minimal}$$

- ensures we get a viable code (can't set li = 0)
- minimises the overall cost of storing the input

```
Algorithm Huffman(X):
    Input:  string X of length n
    Output:optimal encoding tree for X

Compute frequency f(c) of each character c of X
PQ <- new empty Priority Queue
for each character c in alphabet of X do
    T <- single node binary tree storing c
PQ.insert(f(c),  T)
while PQ.size() > 1 do
    (f1, T1) = PQ.removeMin()
    (f2, T2) = PQ.removeMin()
    T <- a new binary tree T with left subtree T1 and right subtree T2
    PQ.insert(f1+ f2, T)
    (f, T) = PQ.removeMin()
return T
```

![Alt text](assets\IMG161.PNG)

### Analysis of Huffman’s Algorithm
Assuming that
- n is the size of X
- d is the number of distinct characters of X
- PQ is implemented using a heap
- Runs in O(n + d∙log d) time

## Real Huffman coding
In practice, we don’t actually care about the codewords in the first instance – we
actually want to compute the set of codeword lengths (how many bits to assign to each codeword)

#### Huffman's example

![Alt text](assets\IMG162.PNG)

Assign codewords by the branch direction of the tree: “If we go left, assign 0, else assign 1”
But we can do better (where better does not mean a better code, but more beautiful, elegant, and less overhead when transmitting the codebook)

![Alt text](assets\IMG163.PNG)

**Canonical codes**
- chop off the lest significant bit (LSB)
