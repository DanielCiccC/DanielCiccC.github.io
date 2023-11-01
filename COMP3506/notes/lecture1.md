# Lecture 1

### Running Time
- Algorithms transform input data into output data
- Running time of an algorithm typically grows with input size
- Average case time is often difficult to determine
- We focus on the worst case running time
  - easier to analyse
  - crucial for many real-world applications

### Best, Average and Worst Cases
Given a list of unsorted numbers, ``L``, and a specific number, ``k``, Return true if ``k`` is in 
``L``, or false otherwise. 

Consider the following algorithm to solve this problem:
```python
def number_exists(L, k):
    for item in L:
        if item == k:
        return True
    return False
```

### How Can We Analyse Algorithms?
- *Experimental (empirical) studies*
  - Write program implementing the algorithm
  - Run program with inputs of varying size and composition
  - Use a method like time.time() to measure actual running time
  - Plot the results
  - **Limitations**:
    - Need to implement the algorithm
      - May be difficult, time consuming, …
    - Time may differ based on the implementation
      - Example: Finding the maximum element in a list
    - Time may differ based on the hardware
    - Results may not be indicative of the running time on other inputs not included in the experiment
      - How do I know if my inputs are best, average, or worst case?
- *Theoretical analysis*
  - Use a high-level description of the algorithm
    - instead of an implementation
  - Characterise running time as a function of input size n
  - Takes into account all possible inputs
    - at least those that are “bad” (hence, worst-case)
  - Evaluation is independent of the hardware and software environment!

### Theoretical Analysis Steps:
1. **Express algorithm as pseudo-code**
    - Example: Find maximum element of an array
```
Algorithm arrayMax(A, n)

    Input array A of n integers 
    Output maximum element of A
    currentMax <- A[0]
    i <- 1 
    while i < n do
        if A[i] > currentMax then
            currentMax <- A[i]
        i <- i + 1 
    return currentMax
```
2. **Count primitive operations**
- Assume word RAM model in this course.
- IMPORTANT:
  - A word is a sequence of w bits (most of our computers have w = 64 bits)
  - Basic arithmetic operations take a `single` operation 
    - (+ - % * //) and so on
  - Bitwise operands take a `single` operation
    -  &, |, <<, >>, …
  - Comparisons take a ``single`` operation
    -  (>, <, ==, !=)
  - Accessing or writing a word in memory takes a single operation
  - Most modern computers are byte addressable
    - Need to be able to access every memory “cell” limits memory size
    -  w ≥ #bits required to represent the largest memory address
  - Example:
  - ``num = 10`` - 1 operation. Assigning a value to a variable
  - ``num = A[10]`` - 2 operations. Indexing into an array, and then assigning a value to a variable
  - ``while i < 10`` - 1 operation per iteration + 1 
  - Loops:
```python 
for i in range (10) # 1 + (n + 1)
    let counted operations = X  # n * X
    # count increment   # n
```
 - ``int i = 0`` is executed once
 - ``i < n`` conditional is evaluated ``n + 1`` times
 - ``i++`` increment is evaluated n times
1. **Describe algorithm as $f(n)$**
 - function of $n$ (the input size)
 - By inspecting the pseudo-code, we can determine the maximum number of primitive operations executed by an algorithm, as a function of the input size

2. **Perform asymptotic analysis**
 - express in asymptotic notation
 - Seven functions that often appear in algorithm analysis

| **Function** | term|
| --- | --- |
| Constant  | $\approx 1$
| Logarithmic  | $\approx log 2 n$
| Linear  | $\approx n$
| N-Log-N  | $\approx n log 2 n$
| Quadratic  | $\approx n 2$
| Cubic  | $\approx n 3$
| Exponential  | $\approx 2 n$

### Big O-notation
- Big-O notation describes an upper bound on a function
- $f(n)$ is $O(g(n))$ if $f(n)$ is asymptotically less than or equal to $g(n)$
That is,

Given functions $f(n)$ and $g(n)$, we say that $f(n)$ is $O(g(n))$
if there are positive constants $c$ and $n_{0}$ such that
$$f(n) \le c \cdot g(n)  \; \; \text{for} \; \; n  \ge n_{0} $$

![Alt text](assets\IMG169.PNG)

### Big-O and growth rate
- Big-O notation gives an upper bound on the growth rate of a function
- “f(n) is O(g(n))” means the growth rate of f(n) is no more than the growth rate of g(n)
- Big-O notation ranks functions according to their growth rate

### Some big-O rules
Rule 1: If f(n) is a polynomial of degree d, then f(n) is $O(n^{4})$
- We can drop lower-order terms
- We can drop constant factors (coefficients)
eg. $3n^{4} + 7n^{3} + 5$ is $O(n^{4})$

Rule 2: Use the smallest possible class of functions (the “tightest” possible bound)
- “2n is O(n)” instead of “2n is $O(n^{2})$”, even if the  latter is still mathematically correct…
- Quiz gotcha: Is “8n is $O(n^{3})$”?

Rule 3: Use the simplest expression of the class
-  “3n + 5 is O(n)” instead of “3n + 5 is O(3n)”

### Operations:
|Type | name| 
|---|---|
|$O(1)$| Constant
|$O(\log n)$| Logarithmic
|$O(n)$| Linear
|$O(n^{2})$ | Quadratic
|$O(2^{n})$ | Exponential
|$O(n!)$ | Factorial

### Some more operations
![Alt text](assets\IMG170.PNG)

### Big Omega notation
- Big-Omega notation describes a lower bound on a function
- f(n) is $\Omega (g(n))$ if $f(n)$ is asymptotically greater than or equal to $g(n)$
- That is,

Given functions $f(n)$ and $g(n)$, we say that $f(n)$ is $\Omega (g(n))$
if there are positive constants $c$ and $n_{0}$ such that
$$f(n) \ge c \cdot g(n)  \; \; \text{for} \; \; n  \ge n_{0} $$       

### Big-Theta Notation

- Big-Theta notation describes a tight bound on a function (if one exists)
- f(n) is $\Theta (g(n))$ if f(n) is asymptotically equal to g(n)
- That is,

Given functions $f(n)$ and $\Theta (n)$, we say that $f(n)$ is $\Theta (g(n))$
if there are positive constants $c_{1}, c_{2}$ and $n_{0}$ such that
$$c_{1} \cdot g(n) \le f(n) \le c_{2}\cdot g(n)  \; \; \text{for all} \; \; n  \ge n_{0} $$   
