# Tutorial 1 - Slides

### Arrays
- Storing a group of elements of the same type

|Action|Time||
|---|---|---|
|Access Element|Constant||
||||

### Algorithms
- Finite sequence of well-defined, computer implementable instructions
- Always unambiguous
- The user doesn't like to wait - we choose the fastest algorithms to solve our problems

Measure algorithms experimentally
- One way to study the efficiency is to implement it and expierment with various inputs and record the time spent
- plot results and complete statistical analysis
#### Issues with experimental analysis
- Difficult to compare unless tested on identical software and hardware
- May leave out certain inputs, which may be important and have different running times

### Beyond experimental analysis
Develop an approach to analysing algorithm efficiency
- allow us to evaluate relative efficiency of two algorithms

### Important details to measure
- Runtime and memory
- Focussed on worst-case scenarios
  - Can also analyse best case and average case scenarios, those these are typically harder to do

### Theoretical Algorithm Analysis
1. Describe using pseudocode
2. Count primitive operations
3. Describe the function of f(n)
- Number of inputs (n)
4. Perform asymptotic analysis

## Asymptotic Analysis
Determine Big O, $\Omega$, $\Theta$ bounds on runtime
- Big O notation describes the upper bound on the function
- UPDATE

- $O(g(n))$ defines an infinite set of functions
- They have to be asymptotically equal

## Definition example
- UPDATE

## Big O
When we usually talk about asyptotic analysis, we use the following rules:
1. Drop lower order terms and constants
2. Make your bounds as tight as possible
3. Simplify as much as possible

## Big O example
- UPDATE

## Big $\Omega$
Is the lower bound

## Big #\Theta$
Is the tight bound

##  Asymptotic Algorithm Analysis example


<!-- # Tutorial Questions
### 1. (a)

$$
f(n) = a_{k}n^{k}+a_{k-1}n^{k-1}+...a_{1}n+a_{0}
$$ 
Drop lower order terms
$$f(n) = a_{k}n^{k}$$
Then drop constants
$$f(n) = n^{k}$$
$$\therefore f(n) \in O(n^{k})$$
### 1. (b)
$$\Omega (n^{k}) $$
### 1. (c)
Yes, it does, $\Theta (n^{k})$

### 2. -->
