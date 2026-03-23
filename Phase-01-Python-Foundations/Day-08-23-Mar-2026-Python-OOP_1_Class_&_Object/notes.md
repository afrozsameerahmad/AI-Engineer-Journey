# Day 08 Notes - Python OOP 1 (Class & Object)

Date: 23 March 2026

These notes are based on:
- `exercise/00PS.ipynb`
- `exercise/self.ipynb`
- `exercise/magic_methods.ipynb`
- `exercise/class_diagram.ipynb`
- `practice/atm.py`
- `practice/create_own_datatype.py`

---

## 1. OOP Basics

- OOP (Object Oriented Programming) is based on `class` and `object`.
- Class = blueprint or set of rules.
- Object = real instance created from class.
- In Python, built-in values are also objects (like `list`, `str`, `int` objects).
- Core OOP pillars:
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

---

## 2. Class, Object, Method, Function

- Class members are mainly:
1. Attributes (data/state)
2. Methods (behavior/actions)

- Method vs Function:
1. Method is called on an object (example: `l.append(6)`).
2. Function is called directly (example: `len(l)`).

---

## 3. `self` Keyword

- `self` is reference to the current object.
- In instance methods, first parameter must be `self`.
- Python automatically passes current object when we call `obj.method()`.
- We use `self` to:
1. Access instance attributes (`self.pin`, `self.balance`)
2. Access one method from another method in same class (`self.create_pin()`)

From `self.ipynb`: `id(self)` inside constructor and `id(obj)` outside are same for that object.

---

## 4. Constructor and Magic Methods

- Constructor in Python: `__init__`
- Called automatically when object is created.
- Used for initialization/configuration.

Magic methods studied:
1. `__init__` -> object initialization
2. `__str__` -> string representation for `print(obj)`
3. `__add__`, `__sub__`, `__mul__`, `__truediv__` -> operator overloading

---

## 5. Practice: `Atm` Class (`practice/atm.py`)

### Current Design

- Attributes:
1. `pin`
2. `balance`

- Methods:
1. `menu()`
2. `create_pin()`
3. `change_pin()`
4. `check_balance()`
5. `withdraw_money()`
6. `deposit_money()`

### Key Learning

- State + behavior in one class.
- Menu loop routes user input to methods.
- Every transaction method verifies PIN before operation.

---

## 6. Practice: Custom Fraction Datatype (`practice/create_own_datatype.py`)

### What It Demonstrates

- Building your own datatype/class (`Fraction`).
- Overloading operators using dunder methods.
- Printing with `__str__`.
- Converting fraction to decimal with custom method.

### Implemented Operations

1. Addition
2. Subtraction
3. Multiplication
4. Division

---

## 7. Class Diagram Thinking

From `class_diagram.ipynb`:
- Attributes and methods should be planned before coding.
- Public members can be accessed from outside.
- Private members should be hidden and accessed via class methods.

---

## 8. Interview-Focused Takeaways (Day 8)

1. Explain class vs object clearly with one real example.
2. Explain why `self` is required in instance methods.
3. Explain constructor lifecycle (`__init__` auto-runs).
4. Explain method vs function with examples (`append` vs `len`).
5. Explain magic methods and why operator overloading is useful.
6. Use ATM/Fraction as project examples to show OOP understanding.

---

## 9. Improvement Ideas (Next Step)

1. In `Fraction`, return `Fraction` objects (not strings) from arithmetic methods.
2. Add zero-division checks and denominator validation.
3. In `Atm`, hide sensitive data with private attributes (`__pin`, `__balance`).
4. Add input validation and better error messages for non-numeric inputs.
