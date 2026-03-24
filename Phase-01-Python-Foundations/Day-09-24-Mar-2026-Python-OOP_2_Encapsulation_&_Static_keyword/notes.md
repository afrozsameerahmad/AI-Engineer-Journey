# Day 09 Notes - Python OOP 2 (Encapsulation and Static Keyword)

Date: 24 March 2026

These notes are based on:
- `exercises/encapsulation.ipynb`
- `exercises/static_variables.ipynb`
- `practice/coordinates_geometry.ipynb`
- Day 08 OOP basics for revision connection

---

## What I Studied Today

Today I studied the next layer of OOP in Python, especially:

- how objects access attributes
- what happens when an attribute does not exist
- creating attributes outside the class
- reference variables and how multiple variables can point to one object
- passing objects to functions
- encapsulation as controlled access to object data
- static variables (class variables) shared by all objects
- class-based practice with `Point` and `Line`

---

## 1. How Objects Access Attributes

In Python, object data is usually accessed with dot notation:

```python
p1.name
p1.country
```

From `encapsulation.ipynb`, the `Person` class stores `name` and `country`
inside `__init__`, and those values are later accessed using the object.

Example:

```python
class Person:
    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input

p1 = Person("Sameer", "India")
print(p1.name)
print(p1.country)
```

Important point:
- If an attribute exists, Python returns its value.
- If an attribute does not exist, Python raises `AttributeError`.

Example idea:

```python
print(p1.gender)   # error if gender was not created yet
```

So object attributes are not magic. They must exist before we can use them.

---

## 2. Attribute Creation Outside the Class

One interesting Python feature is that we can create a new attribute for an
object outside the class as well.

Example from notebook idea:

```python
p1.gender = "male"
print(p1.gender)
```

This means Python objects can be flexible, but this flexibility can also become
dangerous in larger programs because:

1. Different objects may end up with different sets of attributes.
2. Data can be changed from anywhere.
3. Bugs become harder to track.

This is one reason why encapsulation is important.

---

## 3. Reference Variables

Reference variables store the address/reference of an object.

Key ideas from `encapsulation.ipynb`:

1. We can create an object without storing it in a variable.
2. But without a reference variable, we cannot easily use that object later.
3. One object can have multiple reference variables.
4. Assigning one variable to another does not create a new object.

Example:

```python
class Person:
    def __init__(self):
        self.name = "Sameer"

p = Person()
q = p

print(id(p))
print(id(q))
```

If `id(p)` and `id(q)` are same, both variables point to the same object.

So when we do:

```python
q.name = "Sameer Ahmad"
print(p.name)
```

the change is visible through `p` as well, because both are references to the
same object.

---

## 4. Pass By Reference Behavior with Objects

When we pass an object to a function, Python passes the reference to that
object, so the function can work with the same underlying object.

Example:

```python
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(person):
    print(f"Hi my name is {person.name} and I am a {person.gender}")
```

Calling `greet(p)` allows the function to use the object's attributes.

This is important because object methods and external helper functions can both
work with the same object state.

---

## 5. Encapsulation

Encapsulation means wrapping data and the methods that operate on that data into
one unit: the class.

In simple words:
- Data should belong to the object.
- Operations on that data should also be inside the class.
- Direct outside access should be limited when needed.

Even before using private variables, the `Person`, `Atm`, `Point`, and `Line`
examples already show the basic idea of bundling data and behavior together.

### Why Encapsulation Is Needed

If we freely access or modify everything from outside:

1. object data can become invalid
2. program behavior becomes less predictable
3. sensitive values like PIN or balance become unsafe

For example, in an ATM program it is not a good idea to allow direct access like:

```python
atm.balance = 999999
atm.pin = "0000"
```

Instead, we should control updates through methods such as:

- `create_pin()`
- `change_pin()`
- `check_balance()`
- `withdraw_money()`
- `deposit_money()`

### Private Members in Python

Python uses double underscore naming for private-style access:

```python
class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
```

This is name mangling, which means direct access is discouraged.

So Day 09 helps me understand that encapsulation is not only definition.
It is a design habit:

1. keep related data + methods together
2. hide sensitive state when needed
3. allow controlled access through class methods

---

## 6. Static Variable vs Instance Variable

From `static_variables.ipynb`, the `Atm` class uses:

```python
class Atm:
    __total_atms = 0
```

This is a static variable (also called class variable).

### Static Variable

- Belongs to the class, not a single object
- Shared among all objects
- Used for common data

In the notebook:

```python
Atm.__total_atms += 1
```

Each time a new ATM object is created, the total ATM count increases.

### Instance Variable

Instance variables are created with `self` and belong to each object
separately.

Example:

```python
self.pin = ""
self.balance = 0
```

Different ATM objects can have different `pin` and `balance`, but all ATM
objects share the same class-level total count.

### Main Difference

1. Instance variable -> unique for each object
2. Static variable -> same/shared for all objects

This is a very important interview question in OOP.

---

## 7. Practice: `Point` and `Line` Classes

From `practice/coordinates_geometry.ipynb`, I practiced OOP design using
geometry.

### `Point` Class

The `Point` class stores:

1. `x`
2. `y`

Methods used:

1. `__str__()` -> printable coordinate format
2. `euler_distance(other)` -> distance between two points
3. `distance_from_origin()` -> distance from `(0, 0)`

### `Line` Class

The `Line` class is used with line equation form and supports:

1. checking whether a point lies on a line
2. finding shortest distance from point to line

This practice helped me understand:

- data + behavior together in classes
- object interaction (`Point` with another `Point`)
- one class using another class conceptually
- why OOP is useful for math/real-world modeling

---

## 8. Revision Bridge from Day 08

Day 08 taught the base of OOP:

- class and object
- `self`
- constructor
- magic methods
- ATM and custom datatype examples

Day 09 extends that base:

1. Day 08 taught how to create objects.
2. Day 09 taught how object data is accessed and shared.
3. Day 08 introduced ATM design.
4. Day 09 made me think about hiding ATM data using encapsulation.
5. Day 08 taught instance attributes.
6. Day 09 added static/class variables.

So Day 09 is a continuation of Day 08, not a separate topic.

---

## 9. Interview-Focused Takeaways

1. An object can have attributes created inside or outside the class.
2. Accessing missing attribute gives `AttributeError`.
3. Two variables can point to the same object.
4. Passing object to function means function can use that object's data.
5. Encapsulation means controlled access to object state.
6. Static variable is shared across all instances.
7. Instance variable belongs to each object separately.

---

## My Day 09 Summary

Now I understand how Python objects store and expose data, why reference
variables matter, how encapsulation improves safety, and how static variables
help store class-level shared information.

I also practiced OOP modeling through `Point` and `Line`, which made the Day 09
concepts more practical and easier to remember.
