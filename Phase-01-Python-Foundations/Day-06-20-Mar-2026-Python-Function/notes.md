'''
----All content of this file is written by me based on my understanding
of Day 06 Python Function topic.
---

## What I Studied Today

Today I learned Python Functions in depth, especially:

- Why functions are used
- How function execution works in memory
- Function arguments (default, positional, keyword)
- `*args` and `**kwargs`
- Return values and docstrings
- Variable scope (global/local/nonlocal)
- Nested functions

---

## 1. Functions and Their Purpose

A function is a reusable block of code that performs a specific task.
It helps in:

1. Reusability
2. Readability
3. Breaking large problem into smaller pieces (decomposition)
4. Hiding internal implementation details (abstraction)

### Basic Syntax

```python
def function_name(parameters):
    """docstring"""
    # logic
    return value
```

---

## 2. Function Execution and Lifetime

When Python interpreter sees `def`, it stores function definition and moves ahead.
Actual execution happens only when function is called.

At function call:

- A separate function scope is created in memory
- Local variables live inside that scope
- When function returns, that scope is destroyed

### Important

If no `return` is written, Python returns `None` by default.

---

## 3. Parameters vs Arguments

- **Parameter**: Variable in function definition
- **Argument**: Value passed during function call

Example:

```python
def power(a, b):      # a, b are parameters
    return a ** b

power(2, 3)           # 2, 3 are arguments
```

---

## 4. Types of Arguments

### 1) Default Argument

```python
def power(a=2, b=2):
    return a ** b
```

### 2) Positional Argument

```python
power(3, 2)
```

### 3) Keyword Argument

```python
power(b=3, a=2)
```

---

## 5. Variable-Length Arguments

### `*args` (multiple non-keyword arguments)

```python
def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product
```

### `**kwargs` (multiple keyword arguments)

```python
def display(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
```

---

## 6. Docstring

Docstring describes:

- function purpose
- input details
- output details

```python
print(is_even.__doc__)
```

---

## 7. Variable Scope

### Global Scope

Variables declared in main program.

### Local Scope

Variables declared inside function.

### Nonlocal Scope

Used in nested functions to modify enclosing function variable.

### Rule

Inside function, we can read global variable, but to modify it we use `global`.

---

## 8. Nested Functions

A function inside another function is called nested function.
Useful for:

- better organization
- helper logic encapsulation
- closure-like behavior

---

## Day 06 Practice Work (Student-Friendly Medium Problems)

I rewrote all 6 programs in simple style so the logic is easy to understand:

1. `even_odd_batch_analyzer.py`  
   Separate mixed list values into even, odd, and invalid values.

2. `smart_power_calculator.py`  
   Practice `power()` with default, positional, and keyword arguments.

3. `monthly_sales_commission.py`  
   Calculate sales and commission using decomposition and `*args`.

4. `student_result_builder.py`  
   Build a dynamic result card using `**kwargs` for subject marks.

5. `group_expense_splitter.py`  
   Split group expenses with default tax percentage.

6. `nested_scope_bill_counter.py`  
   Understand global, local, and nonlocal scope with a score tracker.

---

## My Day 06 Summary

Now I am comfortable writing beginner-to-medium level function programs using
`default`, positional, keyword, `*args`, and `**kwargs` arguments.

I also understand function scope and nested functions with simpler examples,
so I can solve problems with better confidence.
'''
