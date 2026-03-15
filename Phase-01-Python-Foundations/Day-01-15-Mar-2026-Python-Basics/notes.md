# Day 01 – Python Basics

Date: 15 March 2026

## Topics Covered

1. About Python
2. Data Types
3. Variables, Keywords and Identifiers
4. Python Input / Output

---

# 1. About Python

Python is a **high-level, interpreted, and general-purpose programming language** created by **Guido van Rossum in 1991**.

Python is known for its **simplicity, readability, and powerful ecosystem**, which makes it one of the most popular programming languages in the world.

---

## Why Python?

### 1. Design Philosophy

Python follows a design philosophy that emphasizes:

* **Code readability**
* **Simple and clear syntax**
* **Less code compared to other languages**

Example:

```python
print("Hello World")
```

Python code is **well-indented and easy to understand**, which makes it beginner friendly.

---

### 2. Batteries Included

Python follows the philosophy **"Batteries Included"**.

This means Python provides many **built-in features and libraries** that make development easier.

Examples:

* Built-in functions like `len()`, `type()`, `print()`
* String operations
* Membership operators (`in`, `not in`)
* Built-in data structures like lists, tuples, dictionaries, and sets

Example:

```python
text = "python"
print(text[::-1])  # reverse string
```

---

### 3. General Purpose Language

Python is a **general-purpose programming language**, which means it can be used in many fields.

Examples:

* Data Science
* Web Development
* Automation / Scripting
* Artificial Intelligence
* Machine Learning
* Mobile App Development
* Game Development
* Cybersecurity

---

### 4. Libraries and Community

Python has a **huge ecosystem of libraries**.

Some popular libraries include:

* **NumPy** → numerical computing
* **Pandas** → data analysis
* **Matplotlib / Seaborn** → data visualization
* **Scikit-learn** → machine learning
* **TensorFlow / PyTorch** → deep learning

Python also has a **very large community**, which means:

* Many tutorials and resources
* Open-source projects
* Community support

---

### 5. Why Python for Data Science?

Python is the **most widely used language in data science** because:

* Easy to learn and write
* Strong mathematical and statistical libraries
* Huge data science ecosystem
* Large community support

Important libraries used in data science:

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* TensorFlow
* PyTorch

---

# 2. Python Data Types

Python provides different built-in data types.

### Basic Data Types

* `int` → integers (10, 25)
* `float` → decimal numbers (3.14)
* `str` → strings ("Hello")
* `bool` → boolean values (True / False)

Example:

```python
a = 10
b = 3.14
c = "Hello"
d = True
```

---

### Complex Data Type

Python also supports complex numbers.

Example:

```python
e = 2 + 3j
```

Real part → `e.real`
Imaginary part → `e.imag`

---

### Collection Data Types

Python also has built-in collections:

List → ordered and mutable
Tuple → ordered and immutable
Set → unordered and unique values
Dictionary → key-value pairs

Example:

```python
my_list = [1,2,3]
my_tuple = (1,2,3)
my_set = {1,2,3}
my_dict = {"name":"Sameer","age":20}
```

---

### None Data Type

`None` represents absence of a value.

Example:

```python
x = None
```

---

# 3. Variables

Variables are used to **store data values**.

Example:

```python
name = "Sameer"
age = 20
```

---

## Rules for Variable Names

1. Must start with a letter or underscore `_`
2. Cannot start with a number
3. Cannot contain spaces
4. Cannot be a Python keyword
5. Variable names are **case sensitive**

Example:

Valid:

```
name
_age
score1
```

Invalid:

```
1name
name!
user name
```

---

# 4. Keywords

Keywords are **reserved words in Python**.

They have a special meaning and **cannot be used as variable names**.

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

Python currently has around **35 keywords**.

---

# 5. Identifiers

Identifiers are the **names used for variables, functions, classes, and modules**.

Examples:

```
name
age
calculate_sum
Student
```

Identifiers must follow Python naming rules.

---

# 6. Python Input / Output

### Output

Python uses the `print()` function to display output.

Example:

```python
print("Hello World")
```

---

### Input

Python uses the `input()` function to take input from the user.

Example:

```python
name = input("Enter your name: ")
print(name)
```

Important:

The `input()` function **always returns a string**.

If we need another data type, we must convert it.

Example:

```python
age = int(input("Enter your age: "))
```

---

# Summary

Today I learned:

* Basics of Python
* Why Python is popular
* Python data types
* Variables and naming rules
* Keywords and identifiers
* Input and output in Python
