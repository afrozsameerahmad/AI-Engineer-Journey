'''
----All content of this file is written by me based on my understanding
of Day 07 Python Function In Depth topic.
---

## What I Studied Today

Today I studied advanced function usage in Python, especially:

- Functions as first-class objects
- Passing functions as arguments
- Returning functions from other functions
- Lambda (anonymous) functions
- Higher-order function tools: `map()`, `filter()`, `reduce()`
- Practice problems combining Day 06 + Day 07 function logic

---

## 1. Functions as First-Class Citizens

In Python, function is also an object.  
So we can:

1. Assign function to another variable
2. Store function inside list/dictionary
3. Pass function as argument
4. Return function from another function

Example idea:

```python
def square(x):
    return x * x

s = square
print(s(5))   # 25
```

Even if original name is removed, another reference can still call the function.

---

## 2. Passing and Returning Functions

### Function as Argument

```python
def func_a():
    print("Hello from func_a")

def func_b(z):
    print("Hello from func_b")
    return z()
```

### Function Returning Function

```python
def outer():
    def inner(a, b):
        return a + b
    return inner

print(outer()(3, 4))   # 7
```

This is the core idea of higher-order functions.

---

## 3. Lambda Functions

Lambda is a small anonymous function written in one line.

Syntax:

```python
lambda arguments: expression
```

Examples:

```python
square = lambda x: x * x
label = lambda x: "even" if x % 2 == 0 else "odd"
```

Use lambda for short one-expression logic, mostly with higher-order functions.

---

## 4. `map()`, `filter()`, `reduce()`

## `map()`

Applies a function to each item.

```python
list(map(lambda x: x ** 2, [1, 2, 3]))
```

## `filter()`

Keeps only items where condition is True.

```python
list(filter(lambda x: x > 5, [1, 2, 3, 6, 7]))
```

## `reduce()`

Combines iterable into one value (from `functools`).

```python
import functools
functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
```

---

## 5. Day 07 Practice Work

1. `even_num_from_list.py`  
   Used `filter()` + lambda to extract even numbers from list.

2. `perfect_number.py`  
   Created `is_perfect()` and filtered perfect numbers in a range.

3. `hyphen_sep.py`  
   Built function to sort hyphen-separated words alphabetically.

4. `take_a_list_return_new_list_unique.py`  
   Returned a new list of unique elements using loop + membership check.

5. `uppercase_lowecase.py`  
   Counted uppercase and lowercase characters using `isupper()` / `islower()`.

---

## 6. Revision Bridge from Day 06

Today I connected Day 07 with old practice from Day 06:

- First I understood normal functions (`def`) deeply.
- Then I used same function knowledge in higher-order patterns.
- Lambda became easier because Day 06 basics were clear.
- Day 06 ideas (`default/positional/keyword`, `*args`, `**kwargs`, scope) still remain important in larger function-based programs.

So Day 07 is like extension of Day 06, not a separate topic.

---

## My Day 07 Summary

Now I can work with functions as data in Python and can solve problems using
`lambda`, `map`, `filter`, and `reduce`.

I also improved my confidence by mixing older function fundamentals with new
functional-style practice problems.
'''
