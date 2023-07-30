# Chapt 3.1. Experimental studies

We are interested in the desgin of "good" data structures and algorithms

**Data Structure**: a systematic way of organising and accessing data

**Algorithm**: A step-by-step procedure for performing some task in a finite amount of time.


## Experimental studies
- We can study the running time of an algorithm by recording the time spent between each execution

```python
for time import time
start_time = time()
# run the algorithm
end_time = time()
elaqpsed = end time - start_time
```
- We can use this approach to gather experimental data on the efficiency of Python's list class
- Not the best measure of algorithm efficiency; other background process may yield and unfair test. A fairer metric is the number of CPU cycles that are used by the algorithm

We are interested in the general dependence of running time on the size and structure of the input.
- Perform independent experiments on many different test inputs of various sizes, i.e.

![](assets/IMG1.PNG)

### Challenges of experimental analysis:
- Experimental running times of two differing algorithms are difficult to compare unless experiements are performed on the same hardware and software requirements
- Experiments can only be completed on a limited set of inputs
- An algorithm must be fully implemented in order to execute it, to study its running time experimentally.

## Goal of experimental analysis:
- Evaluate relative efficiency of algorithms in a way that is independent of the hardware and software envrionment
- Is performed at a high-level description of the algorithm without need for implementation
- Takes into account all possible inputs.

### Counting prime operations:
Perform an analysis directly on a high-level description of the algorithm. Define a set of *primitive operations* such as the following:
- Assigning an identifier to an object
- Determining the object associated with an identifier
- Performing an arithmetic operation (e.g. adding two numbers)
A primitive operation corresponds to a low-level instruction with an execution time that is constant. 

Henceforth, to capture the growth of an algorithms's running time, we will associate a function $f(n)$ that characterises the number of primitive operations performed, relative to the input size $n$.

## Focus on worst-case input
- characterise the running times in terms of the wrost case, as a function of the input size, $n$, of the algorithm.
  - easier than avergae case analysis


# Recursion
Begin with the following four example of the use of recursion, providing an python implementation for each:
1. The factorial function
2. An English rules
3. Binary search
4. File system for a computer, in which directories can be nested arbitrarily deep within other directories

## The factorial function
$$ 
n! = 
\begin{cases}
        1 & \text{if } x \in n = 0\\
        n \cdot (n-1)\cdot (n-1) \cdot \cdot \cdot 2 \cdot 1 & \text{if } x \ge 1
\end{cases}
$$
There is a natural recursive definition for the factorial function. Observe that $5!=5\cdot 4 \cdot 3 \cdot 2 \cdot 1 = 5\cdot 4!$. Thus, the recrusive defintion can be formalised as
$$ 
n! = 
\begin{cases}
        1 & \text{if } x \in n = 0\\
        n \cdot (n-1)! & \text{if } x \ge 1
\end{cases}
$$

### Recursive implementation of the Factorial function
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```
- repetition is provided by the repeated invocations of the function
---
  
## Drawing the English Rulers
- For each inch, we place a tick with a numeric label. We denote the length of the tick designating a whole inch as the *major tick length*
- Between marks for whole inches, the rules contains a series of minor ticks, placed at intervals of 1/2 inch, 1/4 inch, etc.
![](assets/IMG2.PNG)

Although it is possible to draw such a ruler with iteration, the task is considerably easier with iteration

### Python Implementation
```python
def draw_line(tick_length, tick_label=''):
"""Draw one line with given tick length (followed by optional label)"""
line = '-' * tick_length
if tick_label:
    line += ' ' + tick_label

def draw_interval(center_length):
    """ Draw tick length based upon a central tick length."""
    if center_length > 0:       # stop when length drops to 0
        draw_interval(center_length - 1)    # recursively draw top ticks
        draw_line(center_length)            # draw center tick
        draw_interval(center_length - 1)    # recursively draw bottom ticks

def draw_ruler(num_inches, major length):
    """Draw English ruler with given numbr of inches, major tick length"""
    draw_line(major_length, '0')        # draw 0 inch line
    for j in range(1, 1+num_inches):
        draw_interval(major_length - 1)     # draw interior tick for inch
        draw_line(major_length, str(j))     # draw in j line and label
```
The execution of the recursive *draw_interval* function can be visualised using a recursion trace.

![](assets/IMG3.PNG)


---
## Binary search