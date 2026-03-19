'''
----All Content of this file is written by me based on my understanding of the topic
at some places you will find real world examples for better understanding
---

## What I Studied Today

Today I learned Python Tuple, Set, and Dictionary. I studied their characteristics, creation, access, operations, methods, and practical usage patterns through exercises and practice files.

---

## 1. Tuple

A tuple is an ordered collection like a list, but immutable (cannot be changed after creation).

### Tuple Characteristics

1. Ordered
2. Immutable
3. Allows duplicate values
4. Can store mixed datatypes
5. Faster and memory efficient compared to list in many cases

### Tuple Creation

```python
empty_tuple = ()
single_item = (10,)   # comma is required
mixed = (1, "hello", True, 3.14)
```

### Accessing Tuple Items

```python
t = ("python", "ai", "ml", "data")
print(t[0])      # python
print(t[-1])     # data
print(t[1:3])    # ('ai', 'ml')
```

### Tuple Methods

```python
t = (1, 2, 2, 3, 4)
print(t.count(2))   # 2
print(t.index(3))   # 3
```

### Tuple Unpacking

```python
point = (10, 20, 30)
x, y, z = point

data = (1, 2, 3, 4, 5)
first, *middle, last = data
```

### Tuple Immutability

```python
t = (1, 2, 3)
# t[0] = 100  -> TypeError
```

Tuple can be used as dictionary key because it is hashable:

```python
locations = {(28.61, 77.20): "Delhi"}
```

---

## 2. Set

A set is an unordered collection of unique elements (no duplicates).

### Set Characteristics

1. Unordered
2. Mutable (set itself can be changed)
3. No duplicate values
4. Elements must be immutable

### Set Creation

```python
s1 = {1, 2, 3}
s2 = set([1, 2, 2, 3])  # {1, 2, 3}
empty_set = set()       # {} is dict, not set
```

### Add / Remove in Set

```python
fruits = {"apple", "banana"}
fruits.add("mango")
fruits.update(["orange", "grapes"])
fruits.remove("banana")      # error if missing
fruits.discard("pineapple")  # no error if missing
item = fruits.pop()          # removes random item
```

### Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # union
print(a & b)   # intersection
print(a - b)   # difference
print(a ^ b)   # symmetric difference
```

### Membership and Relation Checks

```python
print(2 in a)
print({1, 2}.issubset(a))
print(a.issuperset({1, 2}))
print({1, 2}.isdisjoint({5, 6}))
```

### Set Comprehension

```python
squares = {x*x for x in range(1, 6)}
even = {x for x in range(10) if x % 2 == 0}
```

### Frozenset

`frozenset` is immutable set:

```python
f = frozenset([1, 2, 3])
```

---

## 3. Dictionary

Dictionary stores data in key-value pairs.

### Dictionary Characteristics

1. Mutable
2. Keys are unique and immutable
3. Values can be any datatype
4. Fast lookup by key

### Dictionary Basics

```python
student = {"name": "Samee", "age": 21}
print(student["name"])
print(student.get("city", "Not found"))
```

### Update and Delete

```python
student["age"] = 22
student["city"] = "Delhi"
student.update({"course": "Python"})
student.pop("city")
del student["course"]
```

### Dictionary Iteration

```python
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)
```

### Dictionary Comprehension

```python
squares = {x: x*x for x in range(1, 6)}
```

### Frequency Counter Pattern

```python
text = "python"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
```

### Merge Dictionaries

```python
a = {"x": 1, "y": 2}
b = {"y": 20, "z": 3}
merged = {**a, **b}
```

---

## Practice Work Done

- Tuple practice: basics, methods, unpacking, immutability, tuple vs list
- Set practice: operations, manipulation, membership, comprehension, duplicates, common elements
- Dictionary practice: operations, iteration, comprehension, frequency, merge

---

## My Day 05 Summary

I now understand the main difference between tuple, set, and dictionary and when to use each one:

- Use **tuple** for fixed/constant data
- Use **set** for unique values and mathematical set operations
- Use **dictionary** for key-value mapping and fast lookup
'''
