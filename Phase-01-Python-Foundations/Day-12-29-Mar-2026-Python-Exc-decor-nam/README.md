# Day 12 - Python Exceptions, Decorators and Namespaces

**Date:** 29 March 2026

This folder contains Day 12 work focused on Python error handling,
user-defined decorators, and scope resolution through namespaces.

---

# Day 12 Coverage

1. Syntax errors vs runtime exceptions
2. Common built-in exception types in Python
3. Exception handling with `try`, `except`, `else`, `finally`
4. Catching specific exceptions and fallback generic handler
5. Raising exceptions manually with `raise`
6. Creating and using custom exception classes
7. Decorator fundamentals and closure-based wrappers
8. `@decorator` syntax
9. Real use-case decorators (`timer`, `sanity_check`)
10. Namespace types: local, enclosing, global, built-in
11. LEGB rule for name resolution
12. `global` and `nonlocal` keywords

---

# Exercise Notebooks

1. `exercise/exception.ipynb`
	- Compared syntax errors and exceptions
	- Triggered examples: `IndexError`, `KeyError`, `TypeError`, `ValueError`,
	  `NameError`, `AttributeError`, `ModuleNotFoundError`
	- Practiced `try-except` with file handling (`sample.txt`)
	- Used multiple `except` blocks for targeted handling
	- Practiced `else` and `finally` behavior
	- Used `raise` for validating withdraw rules in `Bank` class
	- Built custom exceptions (`MyException`, `SecurityError`)
	- Implemented login-check example with custom security exception flow

2. `exercise/decorators.ipynb`
	- Revised first-class functions in Python
	- Built simple decorator that wraps output with separators
	- Used both manual decoration and `@decorator` syntax
	- Implemented `timer` decorator using `time` module
	- Implemented parameterized `sanity_check(data_type)` decorator
	- Validated function argument type before executing target function

3. `exercise/namespaces.ipynb`
	- Studied namespace definition and dictionary mapping idea
	- Learned scope and LEGB lookup order
	- Compared local vs global variable access
	- Practiced `global` keyword for updating outer variable
	- Practiced `nonlocal` keyword inside nested functions
	- Explored built-in namespace using `builtins` module
	- Observed built-in shadowing case (`max`)

---

# Important Day 12 Files

- `notes.md`
- `README.md`
- `exercise/exception.ipynb`
- `exercise/decorators.ipynb`
- `exercise/namespaces.ipynb`
- `exercise/sample.txt`

---

# Folder Structure

```text
notes.md
README.md
exercise/
	 decorators.ipynb
	 exception.ipynb
	 namespaces.ipynb
	 sample.txt
```

---

# Learning Outcome

- Can identify and classify syntax errors vs runtime exceptions
- Can write robust exception handling flows with specific catches
- Can use `raise` to enforce custom business validations
- Can design custom exception classes for domain-specific scenarios
- Can build and apply decorators for reusable behavior
- Can reason about variable lookup and scope using LEGB
