# Day 18 Notes: Recursion

## 1) What is Recursion?
- Recursion is a programming technique where a function calls itself to solve a problem.
- Each recursive call should bring the problem closer to a base case, which stops further recursion.

---

## 2) Types of Recursion
- **Functional Recursion:** The function returns a value used in further recursive calls (e.g., factorial, Fibonacci).
- **Parameterized Recursion:** The function takes parameters that change with each call, often used for accumulating results (e.g., sum from 1 to n).

---

## 3) Base Case & Recursive Case
- **Base Case:** The condition under which recursion ends (e.g., `if n == 0: return 1`).
- **Recursive Case:** The part where the function calls itself with modified arguments.

---

## 4) Common Recursion Problems
- Factorial calculation
- Fibonacci sequence
- Array reversal
- Palindrome check
- Printing values recursively

---

## 5) Recursion vs Iteration
- Recursion can make code simpler and more elegant for problems with a natural recursive structure (trees, combinatorics).
- Iteration is often more efficient in terms of space (no call stack overhead).

---

## 6) Time and Space Complexity
- Recursive solutions may have higher space complexity due to the call stack.
- Always analyze both time and space when designing recursive algorithms.

---

## 7) Example: Factorial (Functional Recursion)
```python
# Factorial using recursion
def fact(n):
	if n == 0 or n == 1:
		return 1
	return n * fact(n - 1)
```

---

## 8) Example: Parameterized Recursion
```python
# Sum from 1 to n using parameterized recursion
def func(sum, i, n):
	if i > n:
		return sum
	return func(sum + i, i + 1, n)
```

---

## 9) Example: Reverse Array Recursively
```python
# Reverse an array using recursion
def reverse(arr, left, right):
	if left >= right:
		return
	arr[left], arr[right] = arr[right], arr[left]
	reverse(arr, left + 1, right - 1)
```

---

## 10) Example: Palindrome Check (Recursive)
```python
# Check if a string is a palindrome using recursion
def is_palindrome(s, l, r):
	if l >= r:
		return True
	if s[l] != s[r]:
		return False
	return is_palindrome(s, l + 1, r - 1)
```

---

## 11) Practice
- Try writing recursive solutions for:
	- Printing a value n times
	- Calculating Fibonacci numbers
	- Checking for palindromes
	- Reversing arrays
	- Parameterized vs functional recursion
