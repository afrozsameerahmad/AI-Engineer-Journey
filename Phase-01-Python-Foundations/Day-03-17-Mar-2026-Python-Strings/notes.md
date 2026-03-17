# Day 03 - Python Strings

Date: 17 March 2026

## What I Studied Today

Today I learned what strings are in Python, how to create them, how to access characters using indexing, how slicing works, why strings are immutable, and how common string methods help us solve real problems.

---

## 1. What Is a String?

A string is a sequence of characters.

In Python, strings are Unicode strings, which means they can store letters, symbols, and characters from different languages.

We can create strings using:

- Single quotes: `'hello'`
- Double quotes: `"hello"`
- Triple quotes: `'''hello'''`

Example:

```python
name = "Sameer"
message = 'hello'
paragraph = '''This is a string'''
```

If a sentence contains a single quote, it is often easier to use double quotes.

Example:

```python
text = "it's raining outside"
```

---

## 2. Indexing

Each character in a string has a position called an index.

- Positive indexing starts from left to right with `0`
- Negative indexing starts from right to left with `-1`

Example:

```python
s = "hello world"
print(s[0])   # h
print(s[1])   # e
print(s[-1])  # d
print(s[-2])  # l
```

Indexing is useful when we want to access only one character from a string.

---

## 3. Slicing

Slicing is used to take a part of a string.

Syntax:

```python
string[start:end:step]
```

Important rule:

- `start` is included
- `end` is excluded

Examples:

```python
s = "hello world"
print(s[0:5])   # hello
print(s[6:11])  # world
print(s[:5])    # hello
print(s[6:])    # world
```

### Step in slicing

We can also skip characters using the step value.

```python
s = "12345678"
print(s[0:6:2])   # 135
```

### Reverse a string

A very common and useful slicing trick is:

```python
s = "hello"
print(s[::-1])   # olleh
```

---

## 4. Strings Are Immutable

Strings are immutable in Python.

This means we cannot change a character directly after the string is created.

Example:

```python
s = "hello"
# s[0] = "H"   # not allowed
```

If we need a changed version, we create a new string instead.

---

## 5. Deleting a String Variable

We can delete a variable using `del`.

```python
s = "hello world"
del s
```

After deleting it, the variable no longer exists, so using it again will raise an error.

---

## 6. Operations on Strings

### Concatenation

We can join strings using `+`.

```python
print("delhi" + "mumbai")
```

### Repetition

We can repeat a string using `*`.

```python
print("hi" * 3)
```

### Comparison

Strings can be compared using:

- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

Python compares strings lexicographically, which means character by character.

### Logical behavior

- A non-empty string behaves like `True`
- An empty string behaves like `False`

Examples:

```python
print("delhi" and "mumbai")
print("delhi" or "mumbai")
print(not "")
```

### Membership

We can check whether a character or word is present in a string.

```python
s = "hello world"
print("h" in s)
print("z" in s)
print("hello" in s)
```

Membership checking is case-sensitive.

---

## 7. Looping Through a String

We can use a `for` loop to visit each character of a string one by one.

```python
for ch in "hello":
    print(ch)
```

This is useful in many practice problems like counting characters, finding vowels, or removing characters.

---

## 8. Common Functions Used with Strings

### `len()`

Returns the total number of characters in a string.

```python
len("Sameer")
```

### `max()`

Returns the character with the highest value.

### `min()`

Returns the character with the lowest value.

### `sorted()`

Returns the characters of the string in sorted order as a list.

```python
sorted("sameer")
sorted("sameer", reverse=True)
```

---

## 9. Common String Methods

### Case conversion methods

- `upper()` changes all letters to uppercase
- `lower()` changes all letters to lowercase
- `title()` capitalizes the first letter of each word
- `capitalize()` capitalizes the first character of the string
- `swapcase()` changes uppercase to lowercase and lowercase to uppercase

Example:

```python
s = "hello world"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
```

---

## 10. Searching in a String

### `count()`

Counts how many times a character or substring appears.

```python
"Sameer Ahmad".count("a")
```

### `find()`

Returns the index of the first occurrence.

If the value is not present, it returns `-1`.

### `index()`

Also returns the index of the first occurrence.

If the value is not present, it raises an error.

Important difference:

- `find()` is safer when we are not sure the value exists
- `index()` is used when we are sure it exists

---

## 11. Checking Start and End

- `startswith()`
- `endswith()`

Examples:

```python
"hello world".startswith("hello")
"hello world".endswith("world")
```

These are useful in validation and pattern checking.

---

## 12. String Formatting

The `format()` method is used to insert values inside a string.

Example:

```python
name = "Sameer"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
```

This makes output more readable.

---

## 13. Validation Methods

### `isalpha()`

Returns `True` if all characters are alphabets.

### `isdigit()`

Returns `True` if all characters are digits.

### `isalnum()`

Returns `True` if all characters are alphabets or digits.

### `isidentifier()`

Returns `True` if the string can be used as a valid Python variable name.

Examples:

```python
"sameer".isalpha()
"12345".isdigit()
"sameer123".isalnum()
"user_name".isidentifier()
```

---

## 14. Split and Join

### `split()`

Used to break a string into parts.

```python
"hi my name is Sameer".split()
```

This returns a list of words.

### `join()`

Used to combine a list of strings into one string.

```python
"-".join(["hi", "my", "name", "is", "Sameer"])
```

This is very useful when working with words and lists together.

---

## 15. Replace and Strip

### `replace()`

Used to replace one part of a string with another.

```python
"hi my name is Sameer".replace("Sameer", "Ahmad")
```

### `strip()`

Used to remove spaces from the beginning and end of a string.

```python
"   hello   ".strip()
```

It does not remove spaces between words.

---

## 16. Practice Done Today

Today I practiced:

- finding the length of a string without using `len()`
- extracting username and domain from an email
- counting frequency of a character
- removing all occurrences of a chosen character
- checking whether a word or sentence is a palindrome
- analyzing words inside a sentence
- generating a simple username from user details

These problems helped me understand how loops, conditions, slicing, and string methods work together.

---

## Key Takeaways

- Strings are sequences of characters
- Indexing gives a single character
- Slicing gives a part of the string
- Strings are immutable
- Many text problems become easy with methods like `find()`, `count()`, `split()`, `join()`, and `replace()`
- String practice improves logic building a lot in Python
