---
All content of this file is written by me based on my understanding
of Day 10 Python OOP 3 (Inheritance, Polymorphism, Abstraction, Aggregation) topic.
---

## What I Studied Today

Today I studied advanced OOP concepts in Python, especially:

- Inheritance and what actually gets inherited
- `super()` keyword for constructor/method call chaining
- Types of inheritance (single, multilevel, hierarchical, multiple, hybrid)
- Polymorphism (overriding, simulated overloading, operator overloading)
- Abstraction using `ABC` and `@abstractmethod`
- Aggregation (Has-A relationship)

---

## 1. Inheritance

Inheritance means a child class can reuse attributes and methods of a parent class.
It helps reduce duplicate code and creates a class hierarchy.

Udemy-style idea used in exercise:

- `User` has common features (login/register)
- `Student`, `Teacher`, `Admin` can inherit common behavior

Basic example used:

```python
class User:
	def __init__(self):
		self.name = 'Sameer'

	def login(self):
		print(f'{self.name} logged in successfully')

class Student(User):
	def __init__(self):
		super().__init__()
		self.roll_number = 1
```

---

## 2. What Gets Inherited?

From parent to child (normally):

1. Constructor (`__init__`) behavior, unless child defines its own constructor
2. Non-private attributes
3. Non-private methods

Important point from exercise:

- Private members like `__price` are name-mangled and cannot be directly accessed in child class.

---

## 3. `super()` Keyword

`super()` is used to call parent class constructor and methods from child class.

Two major usages practiced:

1. Constructor chaining

```python
class SmartPhone(Phone):
	def __init__(self, price, brand, camera, os, ram):
		super().__init__(price, brand, camera)
		self.os = os
		self.ram = ram
```

2. Calling parent method while overriding

```python
class SmartPhone(Phone):
	def buy(self):
		print("Buying a smartphone")
		super().buy()
```

---

## 4. Types of Inheritance

I practiced these inheritance patterns:

1. Single inheritance
2. Multilevel inheritance
3. Hierarchical inheritance
4. Multiple inheritance
5. Hybrid inheritance

In multiple inheritance, one class inherits from multiple parents.
In hybrid inheritance, more than one inheritance pattern is combined.

---

## 5. Polymorphism

Polymorphism means "multiple forms" (same interface, different behavior).

I practiced 3 forms:

1. Simulated method overloading using default argument

```python
class Shape:
	def area(self, a, b=None):
		if b is None:
			return a * a
		return a * b
```

2. Method overriding in child classes

```python
class Animal:
	def sound(self):
		return "Animal makes a sound"

class Dog(Animal):
	def sound(self):
		return "Dog barks"
```

3. Operator overloading (`__add__`) for custom object addition

```python
class Point:
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
```

---

## 6. Abstraction

Abstraction means hiding internal implementation details and exposing only required operations.

I used abstract base class tools:

- `from abc import ABC, abstractmethod`
- abstract class `BankAccount`
- concrete implementations `WebBankAccount` and `MobileBankAccount`

Common operations were same (`check_balance`, `withdraw`, `deposit`) but implementation class can differ.

---

## 7. Aggregation (Has-A Relationship)

Aggregation means one class has a reference to another class, but both can exist independently.

Example practiced:

- `Customer` has an `Address`
- `Address` can exist independently
- `Customer` methods use `Address` object methods/data

```python
addr = Address("Lucknow", 10001, "UP")
cust = Customer("Sameer", "Male", addr)
```

---

## My Day 10 Summary

Now I can clearly differentiate and implement:

- Inheritance and its types
- Method overriding and operator overloading
- Abstract base classes and abstract methods
- Aggregation relationship between classes
- Parent-child interaction with `super()`

This day made my OOP understanding stronger and more practical for real project design.
