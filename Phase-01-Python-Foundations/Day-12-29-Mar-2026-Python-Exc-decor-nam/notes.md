# Day 12 Notes - Python Exceptions, Decorators and Namespaces

Date: 29 March 2026

These notes are based on:
- `exercise/exception.ipynb`
- `exercise/decorators.ipynb`
- `exercise/namespaces.ipynb`

---

## What I Studied Today

Today I practiced three important Python topics that improve code quality and
program understanding:

- syntax errors vs runtime exceptions
- handling errors using `try`, `except`, `else`, and `finally`
- manually raising exceptions and creating custom exception classes
- understanding decorators and writing user-defined decorators
- using function closures for wrappers
- namespaces and scope resolution using the LEGB rule
- `global` and `nonlocal` keyword behavior in nested functions

---

## 1. Syntax Error vs Exception

From `exception.ipynb`, I revised that errors happen in two stages:

1. During compilation/parsing -> Syntax Error
2. During execution -> Exception

Syntax errors are grammar problems like:

- missing colon in `if`
- incorrect indentation
- invalid Python syntax like old print style

Examples used:

```python
print 'hello world'

a=5
if a==3
	print("a is 3")
```

---

## 2. Common Runtime Exceptions

I practiced identifying common exception types:

1. `IndexError` -> invalid list index
2. `ModuleNotFoundError` -> importing missing module
3. `KeyError` -> missing dictionary key
4. `TypeError` -> invalid operation on mixed types
5. `ValueError` -> bad value for valid type
6. `NameError` -> undefined variable
7. `AttributeError` -> missing attribute/method

Notebook examples included:

```python
my_list = [1, 2, 3]
print(my_list[5])

my_dict = {"name": "sameer", "age": 20}
print(my_dict["gender"])

5 + "hello"
```

---

## 3. Exception Handling with `try-except`

I created `sample.txt` and practiced safe file reading:

```python
try:
	with open("sample1.txt", "r") as f:
		print(f.read())
except FileNotFoundError:
	print("File not found.")
```

I also practiced multiple `except` blocks and generic handling:

```python
except FileNotFoundError:
	...
except NameError:
	...
except ZeroDivisionError:
	...
except Exception as e:
	print(str(e))
```

This made it clear that specific exceptions should be handled before generic
ones.

---

## 4. `else` and `finally` in Exception Handling

From examples:

- `else` runs only when no exception happens
- `finally` runs in all cases

Used pattern:

```python
try:
	f=open("sample.txt", "r")
except FileNotFoundError:
	print("File not found.")
else:
	print(f.read())
finally:
	print("This will always execute.")
```

---

## 5. `raise` Keyword and Why It Matters

I practiced manually raising exceptions to enforce business rules.

`Bank.withdraw` example:

- amount must be positive
- amount cannot exceed balance

```python
if amount <= 0:
	raise Exception("Withdrawal amount must be positive.")
if amount > self.balance:
	raise Exception("Insufficient balance.")
```

This showed how to fail early with meaningful error messages.

---

## 6. Custom Exceptions

I created custom exception classes like `MyException` and `SecurityError`.

`Google.login` flow used `SecurityError` for:

- wrong device
- wrong email/password

and handled it with:

```python
except SecurityError as e:
	e.logout()
```

This demonstrated domain-specific error handling instead of generic exceptions.

---

## 7. Decorators

From `decorators.ipynb`, I revised that decorators add behavior around an
existing function.

I practiced:

1. function passed as argument (`modify(square, 5)`)
2. manual decoration (`a = my_decorator(hello)`)
3. `@decorator` syntax for cleaner code
4. practical timing decorator using `time.time()`
5. parameterized decorator (`sanity_check(int)`) for type guard

Timer decorator idea used:

```python
def timer(func):
	def wrapper():
		start = time.time()
		func()
		print(f"Time taken to execute {func.__name__}: {time.time()-start}")
	return wrapper
```

---

## 8. Namespaces and LEGB Rule

From `namespaces.ipynb`, I studied namespace types:

1. Builtin
2. Global
3. Enclosing
4. Local

I practiced LEGB search behavior and scope cases:

- local and global variables with same name
- accessing global inside function
- `global` keyword to modify global variable
- creating global variable from function
- function parameters as local variables
- builtins module inspection (`dir(builtins)`)
- shadowing built-in names (`max`)
- enclosing scope and `nonlocal` keyword

Key lesson: Python resolves names from local to enclosing to global to built-in,
and raises `NameError` if not found.

---

## 9. Important Day 12 Practice Files

- `exercise/exception.ipynb`
- `exercise/decorators.ipynb`
- `exercise/namespaces.ipynb`
- `exercise/sample.txt`

---

## 10. Key Takeaways

1. Understand whether the issue is syntax-time or runtime.
2. Use specific `except` blocks before broad `Exception` handling.
3. Use `else` for success path and `finally` for guaranteed cleanup.
4. Use `raise` to enforce rules and prevent invalid states.
5. Custom exceptions make code more domain-aware and readable.
6. Decorators are powerful for reusable cross-cutting behavior.
7. LEGB, `global`, and `nonlocal` are essential for predictable variable access.

---

## My Day 12 Summary

Day 12 helped me connect error handling, decorators, and namespaces as practical
tools for writing safer and cleaner Python code. I can now identify common
exceptions, handle them properly, create custom exceptions, decorate functions
for reusable logic, and reason about variable scope using LEGB.
