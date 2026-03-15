# Day 01 – Python Basics

**Date:** 15 March 2026

This day focused on understanding the **fundamentals of Python programming** including its design philosophy, basic data types, variables, identifiers, and input/output operations.

---

# Topics Covered

1. About Python
2. Python Data Types
3. Variables, Keywords and Identifiers
4. Python Input and Output

---

# 1. About Python

Python is a **high-level, interpreted, and general-purpose programming language** created by **Guido van Rossum** in 1991.

It is one of the most popular languages used in:

* Data Science
* Web Development
* Machine Learning
* Artificial Intelligence
* Automation
* Software Development

---

# Why Python?

### 1. Design Philosophy

Python focuses on:

* Code readability
* Simple syntax
* Easy learning curve

Example:

```
print("Hello World")
```

Python code is **clean, readable, and well-structured**.

---

### 2. Batteries Included

Python provides many **built-in features and libraries** so developers don't need to implement everything from scratch.

Examples:

* Built-in functions (`print()`, `len()`, `type()`)
* Built-in data structures
* String operations
* Membership operators (`in`, `not in`)

Example:

```
text = "python"
print(text[::-1])
```

---

### 3. General Purpose Language

Python can be used in many domains such as:

* Data Science
* Web Development
* Mobile App Development
* Machine Learning
* Game Development
* Automation

---

### 4. Libraries and Community

Python has a **large ecosystem of libraries**.

Popular libraries include:

* NumPy → numerical computing
* Pandas → data analysis
* Matplotlib → data visualization
* Scikit-learn → machine learning
* TensorFlow / PyTorch → deep learning

Python also has a **very strong global developer community**.

---

### Why Python for Data Science?

Python is widely used in data science because:

* Easy to learn
* Strong mathematical libraries
* Large ecosystem
* Community support

Important libraries:

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

# 2. Python Data Types

Python provides different built-in data types.

## Basic Types

* `int` → integers
* `float` → decimal numbers
* `str` → strings
* `bool` → True / False

Example:

```
a = 10
b = 3.14
c = "Hello"
d = True
```

---

## Complex Type

Python also supports complex numbers.

```
e = 2 + 3j
```

* `e.real` → real part
* `e.imag` → imaginary part

---

## Collection Data Types

* **List** → ordered and mutable
* **Tuple** → ordered and immutable
* **Set** → unordered and unique values
* **Dictionary** → key-value pairs

Example:

```
my_list = [1,2,3]
my_tuple = (1,2,3)
my_set = {1,2,3}
my_dict = {"name":"Sameer","age":20}
```

---

## None Data Type

`None` represents the absence of a value.

```
x = None
```

---

# 3. Variables

Variables are used to **store values in memory**.

Example:

```
name = "Sameer"
age = 20
```

### Variable Naming Rules

* Must start with a letter or `_`
* Cannot start with a number
* Cannot contain spaces
* Cannot be a keyword
* Case-sensitive

Valid examples:

```
name
_age
score1
```

Invalid examples:

```
1name
user name
name!
```

---

# Keywords

Keywords are **reserved words in Python**.

Examples:

```
if
else
for
while
def
class
return
```

These cannot be used as variable names.

---

# Identifiers

Identifiers are names used for:

* variables
* functions
* classes
* modules

Examples:

```
name
calculate_sum
Student
```

---

# 4. Python Input / Output

## Output

Python uses the `print()` function.

Example:

```
print("Hello World")
```

---

## Input

Python uses the `input()` function to take input from the user.

Example:

```
name = input("Enter your name: ")
print(name)
```

Note: `input()` always returns a **string**.

Example with conversion:

```
age = int(input("Enter your age: "))
```

---

# Files in This Folder

```
notes.md → Detailed theory notes
practice.py → Basic Python experiments
exercise.py → Practice coding questions
mini_projects/ → Small Python projects
README.md → Summary of the day's learning
```

---

# What I Learned Today

* Python fundamentals
* Python design philosophy
* Basic data types
* Variables and naming rules
* Keywords and identifiers
* Input and output handling

---

# Next Step

Day 02 will cover:

* Conditional statements (`if`, `else`, `elif`)
* Loops (`for`, `while`)
* Basic logic building
