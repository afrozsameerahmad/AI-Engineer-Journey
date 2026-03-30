# Day 13 Notes - Python Recursion 

Date: 30 March 2026

These notes are based on:
- `exercises/recursion.ipynb`
- `tasks/cal_n_natural_num.ipynb`
- `tasks/list.ipynb`
- `tasks/multiply.ipynb`
- `tasks/palindrome.ipynb`
- `tasks/power_set.ipynb`
- `tasks/rabbit_problem.ipynb`

---

## What I Studied Today

Today's session was dedicated to understanding recursion as a problem-solving technique and comparing it with iterative approaches.

- The core definition of a recursive function (a function that calls itself).
- The importance of a **base case** to terminate the recursion.
- The role of the **recursive case** in breaking the problem down.
- How the **call stack** manages recursive function calls.
- The concept of a **recurrence relation** (e.g., `F(n) = n * F(n-1)`).
- Solving various problems using recursion:
    - Factorial of a number.
    - Sum of first N natural numbers.
    - Printing elements of a list.
    - Multiplication via repeated addition.
    - Checking for palindromes.
- Using an iterative approach for efficiency, demonstrated with the Fibonacci sequence (Rabbit Problem).
- An introduction to **backtracking** as a recursive strategy for the Power Set problem.

---

## 1. Recursion Fundamentals

From `exercises/recursion.ipynb`, I learned that a recursive solution has two key parts:

1.  **Base Case**: The simplest version of the problem that doesn't require further recursion.
2.  **Recursive Case**: The part that simplifies the problem and calls the function again with the simplified input.

The factorial function is a classic example:

```python
# Base case: if n is 0 or 1, the factorial is 1.
# Recursive case: n * factorial of (n-1).
def factorial(n):
    if (n==0 or n==1):
        return 1        
    else:
        return n * factorial(n-1)

print(factorial(5)) # Output: 120
```

---

## 2. Recursion vs. Iteration

While recursion is elegant, it's not always the most efficient method due to the overhead of the function call stack. The Fibonacci sequence, which I explored in `tasks/rabbit_problem.ipynb`, is a great example where an iterative solution is often preferred.

**Iterative Fibonacci (Rabbit Problem):**

```python
# Calculates the number of rabbit pairs after n months.
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# After 12 months
print(fib(12)) # Output: 144
```
This approach avoids deep recursion and is generally faster and more memory-efficient for this problem.

---

## 3. Recursive Task Implementations

I applied recursion to solve several smaller problems:

### a. Sum of First N Natural Numbers (`tasks/cal_n_natural_num.ipynb`)

```python
def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n - 1) + n

result = cal_sum(5)
print(result) # Output: 15
```

### b. Print List Elements (`tasks/list.ipynb`)

```python
def print_list(lst, index=0):
    if(index == len(lst)):
        return
    print(lst[index])
    print_list(lst, index+1)

fruits = ['apple', 'banana', 'cherry']
print_list(fruits)
```

### c. Palindrome Checker (`tasks/palindrome.ipynb`)

```python
def is_palindrome(text):
    if len(text) <= 1:
        return True
    # Compare the first and last characters
    if text[0] == text[-1]:
        # Recur with the substring in between
        return is_palindrome(text[1:-1])
    else:
        return False

print(is_palindrome("madam")) # Output: True
print(is_palindrome("hello")) # Output: False
```

### d. Power Set with Backtracking (`tasks/power_set.ipynb`)

This task introduced backtracking, a recursive algorithm that builds a solution incrementally and removes solutions that don't satisfy the constraints.

```python
def power_set(nums):
    result = []
    
    def backtrack(index, current):
        # Add the current subset to the result
        result.append(current[:])
        
        # Explore further options
        for i in range(index, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop() # Backtrack
    
    backtrack(0, [])
    return result

print(power_set([1, 2, 3]))
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

Backtracking is a recursive technique for solving problems by trying to build a solution incrementally.

```python
def power_set(nums):
    result = []
    def backtrack(index, current):
        result.append(current[:])
        for i in range(index, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result

print(power_set([1, 2, 3]))
```
