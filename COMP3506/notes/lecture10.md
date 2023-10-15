# Lecture 10

## Strings and pattern matching

### Strings
- Sequence of characters
- Alhpabet $\Sigma$ - set of possible characters for a family of strings
  - {0,1} (binary alphabet)
  - {A, C, G, T} (DNA structures)

- Substring ``S[i,...j]``
- Prefix: substring of the type ``S[0..i]``
- Suffix: substring of the type ``S[i...m-1]``

### Pattern Matching Problem
- Given string ``T`` (text) and P(pattern)
  - Find substring of ``T`` equal to ``P``

### Brute force pattern matching
- Compare the pattern P with the text T
for each possible shift of P relative to T

```
Algorithm BruteForceMatch(T, P)
    Input: text T of size n and pattern P of size m
    Output: starting index of a substring of T equal to P 
        or -1 if no such substring exists 

    for  i <- 0 to n – m  do
    { test shift i of the pattern }
        j <- 0
        while  j < m OR T[i + j] = P[j]  do
            j <- j + 1
        if  j = m  then
            return  i {match at i}
        else
            break while loop {mismatch}
        return  -1 {no match anywhere}

```

- Brute-force pattern matching runs in time O(nm)
- Example of worst case:
  - T = aaa … ah and P = aaah

![Alt text](assets\IMG138.PNG)

### Can we do better?
- Boyer-Moore pattern matching algorithm
- Attempts to improve the Brute-Force 
approach by using two heuristics
  - Looking-glass heuristic
  - Character-jump heuristic

### Boyer-Moore: Looking-Glass Heuristic
- Compare P with a subsequence of T moving 
backwards

![Alt text](assets\IMG139.PNG)

### Boyer-Moore: Character-Jump Heuristic
- When a mismatch occurs at T[i] = c
  - if P contains c, shift P to align the last occurrence of c in 
P with T[i] 
![Alt text](assets\IMG140.PNG)

- Else, shift P to align P[0] with T[i + 1]

![Alt text](assets\IMG141.PNG)

### Example
- at the end, mitmatches on a h and realigns
![Alt text](assets\IMG142.PNG)

### Last-Occurrence Function
- Boyer-Moore’s algorithm preprocesses the 
pattern P and the alphabet $\Sigma$ to build the last-occurrence function L mapping $\Sigma$ to integers, where $L(c)$ is defined as
  - largest index i such that P[i] = c or
  - -1 if no such index exists 

- Example 
  - $\Sigma = {a, b, c, d}$ 
  - $P = abacab$


![Alt text](assets\IMG143.PNG)

### Last Occurrence Function
Can be represented by an array indexed by the numeric codes of the characters
- computed in $O(m + s)$ time, where m is the 
size of P and s is the size of $\Sigma$
- accessed in O(1) time

```
Algorithm BoyerMooreMatch(T, P, S)
L <- lastOccurenceFunction(P, S)
i <- m - 1   { m is size of P }
j <- m - 1

repeat 
    if T[i] = P[j] then
        if  j = 0 then
            return  i { match at i }
        else
            i <- i - 1
            j <- j - 1
    else
        { character-jump }
        l <- L[T[i]]
        i <- i + m – min(j, 1 + l)
        j <- m - 1
    until  i > n - 1
    return -1 { no match}
```

### Performance analysis

- Runs in O(nm + s) time
  - Could potentially be worst than brute force time
- Example of worst case
  - T = aaa … a
  - P = baaa
- Boyer-Moore’s algorithm 
is significantly faster than 
the brute-force algorithm

#### Worst case example

![Alt text](assets\IMG144.PNG)

### Knuth-Morris-Pratt (KMP) Algorithm

- Compares the pattern to the text left-to-right
  - but shifts the pattern more intelligently than the brute-force algorithm
- When a mismatch occurs, what is the most we can shift the pattern so as to avoid redundant comparisons?
- Answer: the largest prefix of ``P[0...j-1]`` that is a suffix of ``P[1...j-1]``
  - repeat redundant patterns
  - computes a failure function

![Alt text](assets\IMG145.PNG)

### KMP failure function
- KMP algorithm preprocesses the pattern 
- Failure function F(j) is defined as the size of the largest prefix of P[0..j] that is also a suffix of P[1..j]
- KMP algorithm modifies the brute-force algorithm so that if a mismatch occurs at P[j] $\ne$ T[i]  we set j <- F(j - 1)

|``J``|0|1|2|3|4|5|
|---|---|---|---|---|---|---|
|``P[j]``| a|b|a|a|b|a|
|``F(j)``| 0|0|1|1|2|3|

### KMP Algorithm

- Failure function can be represented by an array and can be computed in $O(m)$ time
- Each iteration of the while-loop, either
  - i increases by one, or
  - shift amount i - j increases by at least one (observe that F(j - 1) < j)
- Hence, there are no more than 2n iterations of the while-loop
- Thus, KMP’s algorithm runs in optimal time $O(m + n)$

```
Algorithm KMPMatch(T, P)
F <- failureFunction(P)
i <- 0
j <- 0
while  i < length(T)
    if  T[i] = P[j]  then
        if  j = length(P) - 1  then
            return  i - j { match }
        else
            i <- i + 1
            j <- j + 1
else
    if  j > 0 then
        j <- F[j - 1]
    else
        i <- i + 1
return  -1 { no match }
```

### Example

![Alt text](assets\IMG146.PNG)


## Tries - Retrieval Tries

### Preprocessing steps
- Preprocessing the pattern speeds up pattern matching queries
  - After preprocessing the pattern, KMP’s algorithm performs pattern matching in time proportional to the text size
- If text is large, and searched often, preprocess the text (**create and index**)
  - trie supports pattern matching queries in time proportional to the pattern size

Standard trie for the set of strings
S = { bear, bell, bid, bull, buy, sell, stock, stop }

![Alt text](assets\IMG147.PNG)

- sometime represented as a special symbol to denote that a word ends on an internal node

![Alt text](assets\IMG148.PNG)

### Analysis of standard tries

- ``n`` total size of the strings in S
- ``m`` size of the string parameter of the (e.g. search) operation
- ``d`` size of the alphabet (mostly fixed? i.e. acgt)
- uses O(n) space
- supports searches, insertions and deletions in time O(dm)


- Insert words of the text into trie
- Each leaf is associated w/ one particular word
- Leaf stores indices where associated word begins (“see” starts at index 0 & 24, leaf for “see” stores those indices)

![Alt text](assets\IMG149.PNG)

![Alt text](assets\IMG150.PNG)

### Compressed Tries
- Compressed trie has internal nodes of degree at least two
- Obtained from standard trie by compressing chains of redundant nodes

- “i” and “d” in “bid” are redundant
  - they signify the same word


![Alt text](assets\IMG151.PNG)

- What is the maximum number of nodes in a compressed trie storing s words?
  - s + (s -1) = 2 s -1

### Compact Representation

Want to create a compact representation of a compressed tree 

Compact representation of a compressed trie for an array of strings
- Stores ranges of indices instead of substrings at the nodes 
- Uses $O(s)$ space, where s is the number of strings in the array
- Serves as an auxiliary index structure


### Tries - outside of patterns

- Tries have other common uses outside of simple pattern matching (finding patterns in a given text efficiently)
- One common example: Autosuggestion engines

### Input: Query Logs
- Take a large log of historical queries
- Count the number of times each query appears
- Basic idea: The autosuggestion engine should spit out suggestions based on historical popularity
- Input data then becomes a sequence of <query> <count> pairs

### Building the Trie
- Each node (or edge) also holds a weight corresponding to the volume of queries that were issued for that prefix
