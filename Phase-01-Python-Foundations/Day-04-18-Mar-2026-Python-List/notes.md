''' 
----All Content of this file is written by me based on my understanding of the topic
at some places you will find real world examples for better understanding
---

## What I Studied Today

Today I learned about Python Lists: what they are, how they differ from arrays, their characteristics, how to create and access them, how to add and delete items, operations and functions on lists, and list comprehensions.

---

## 1. What are Lists?

Lists are a datatype where you can store multiple items in a single variable. Lists act like dynamic arrays, so you can add more items on the fly. Lists are ordered, mutable, and allow duplicate values.

Example: storing movie reviews in a single variable as a list is more efficient and easy to manage than using separate variables.

Lists are created using square brackets `[]` and items are separated by commas.

```python
a = [1, 2, 3, "hello", True]
```

---

## 2. List vs Arrays

Arrays have a fixed length and must be homogenous (same datatype). Lists are dynamic and can store items of different datatypes.

**Advantage:** Lists are flexible and memory efficient compared to arrays.

**Disadvantage:** Lists are slower than arrays due to their dynamic nature.

To know the address of list items, use the `id()` function:

```python
my_list = [1, 2, 3]
print(id(my_list[0]))  # memory address of first item
```

---

## 3. Characteristics of Lists

1. **Ordered:** Items have a defined order.
2. **Mutable:** Items can be changed after creation.
3. **Allow Duplicates:** Multiple items with the same value are allowed.
4. **Heterogeneous:** Can store different datatypes.
5. **Dynamic:** Can add/remove items on the fly.
6. **Indexing & Slicing:** Access items by index or get subsets.
7. **Methods:** Built-in methods for adding, removing, sorting, etc.
8. **Can contain any object:** Including other lists, dicts, etc.

---

## 4. How to Create a List

```python
# Empty list
l = []
# 1D list
l1 = [1, 2, 3, 4, 5]
# 2D list
l2 = [[1,2,3],[4,5,6],[7,8,9]]
# 3D list
l3 = [[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]
# Using type conversion
l4 = list((1,2,3,4,5))
```

---

## 5. Accessing Items from a List

### Indexing
```python
l = [1,2,3,4,5]
print(l[0])   # 1
print(l[-1])  # 5
```

### Slicing
```python
print(l[1:4])   # [2, 3, 4]
print(l[:3])    # [1, 2, 3]
print(l[0:5:2]) # [1, 3, 5]
```

---

## 6. Adding Items to a List

```python
l.append(5)         # Add to end
l.insert(2, 10)     # Insert at index
l.extend([6,7,8])   # Add multiple
l2 = l + [9,10]     # Concatenate
l3 = l * 2          # Repeat
l4 = [x*2 for x in l] # List comprehension
```

---

## 7. Editing and Deleting Items

```python
l[2] = 10           # Edit
del l[2]            # Delete by index
l.remove(4)         # Remove by value
l.pop(1)            # Remove by index
l.clear()           # Remove all
```

---

## 8. List Functions

```python
len(l)              # Number of items
sum(l)              # Sum (numeric lists)
max(l), min(l)      # Max/Min
sorted(l)           # New sorted list
list(reversed(l))   # New reversed list
l.count(3)          # Count occurrences
l.index(4)          # Index of value
l.sort()            # Sort in place
l1 = l.copy()       # Copy list
```

---

## 9. List Comprehension

List comprehension is a concise way to create lists:

```python
squares = [x**2 for x in range(10) if x%2==0]
print(squares)  # [0, 4, 16, 36, 64]
```

---

## 10. Traversing a List

### Itemwise
```python
for item in l:
	print(item)
```
### Indexwise
```python
for i in range(len(l)):
	print(l[i])
```

---

## Practice and Mini Projects

- Practice problems and mini projects using lists are in the respective folders.
'''
