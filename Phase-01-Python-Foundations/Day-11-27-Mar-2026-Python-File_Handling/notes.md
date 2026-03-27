# Day 11 Notes - Python File Handling, Serialization and Deserialization

Date: 27 March 2026

These notes are based on:
- `exercises/file_handling.ipynb`
- `exercises/serialization_deserialization.ipynb`
- `tasks/task1.ipynb`
- `tasks/task_2.ipynb`
- `tasks/task_3.ipynb`
- `tasks/task_4.ipynb`
- `tasks/task_5.ipynb`

---

## What I Studied Today

Today I practiced Python file handling from basics to practical storage:

- text and binary files
- read/write/append operations
- context manager (`with open(...)`)
- moving file pointer using `seek()` and `tell()`
- chunk reading for big files
- JSON serialization/deserialization
- custom object serialization in JSON
- pickling/unpickling Python objects
- task-based file transformation and frequency counting

---

## 1. Text Files vs Binary Files

I revised that file I/O usually works in three steps:

1. open file
2. read/write data
3. close file

Two common file types:

1. Text file: characters (Unicode), like `.txt`, `.py`
2. Binary file: bytes, like image/audio/video/exe

---

## 2. Write Mode and Append Mode

From `file_handling.ipynb`:

- `w` mode creates file if not present
- if file exists, `w` mode overwrites old content
- `a` mode appends new content at end without deleting old content

Example idea used:

```python
f = open("sample.txt", "w")
f.write("Sameer Ahmad")
f.close()

f = open("sample.txt", "a")
f.write("\nthis is append mode")
f.close()
```

I also practiced writing multiple lines using `writelines()`.

---

## 3. Reading Data from File

I practiced these read styles:

1. `read()` -> full file
2. `read(n)` -> first `n` characters
3. `readline()` -> one line at a time
4. loop with `readline()` until empty string

Examples from outputs:

- `read(10)` gave partial text like `hello hi h`
- line-based reading printed all lines of `sample.txt`

---

## 4. Context Manager (`with`)

`with open(...)` automatically closes file after block ends, so it is cleaner
and safer than manual `close()` calls.

Example used:

```python
with open("sample.txt", "w") as f:
    f.write("this is with statement")

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
```

Output confirmed: `this is with statement`.

---

## 5. File Pointer: `tell()` and `seek()`

I practiced pointer movement in files:

- `tell()` returns current pointer index
- `seek(pos)` moves pointer to a specific position

Notebook example:

```python
with open("sample.txt", "r") as f:
    print(f.read(10))
    print(f.tell())   # pointer after reading 10 chars
    f.seek(15)
    print(f.read(10))
```

This made it clear that read position is stateful and can be controlled.

---

## 6. Working with Large Files in Chunks

I created `big_file.txt` (1000 repeated lines) and then read in chunks to avoid
loading everything at once.

This is useful for:

- memory efficiency
- processing very large files safely

---

## 7. Binary File Handling

I copied an image file using binary modes:

```python
with open("profile.jpeg", "rb") as f:
    with open("copy_profile.jpeg", "wb") as f1:
        f1.write(f.read())
```

So Day 11 also covered practical byte-level file handling.

---

## 8. JSON Serialization and Deserialization

From `serialization_deserialization.ipynb`, I practiced:

1. Python list/dict -> JSON (`json.dump`)
2. JSON -> Python (`json.load`)
3. tuple serialization behavior

Important observation:

- tuple is stored in JSON as array
- when loaded back, it becomes Python `list`

Example output:

```python
[1, 2, 3, 4, 5]
<class 'list'>
```

I also saved mixed datatype dictionary to `exercises/data.json`.

---

## 9. Custom Object to JSON

A `Person` class object cannot be directly dumped unless we provide conversion
logic. I used a `default` function:

```python
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def show_object(p):
    if isinstance(p, Person):
        return {"name": p.name, "age": p.age, "city": p.city}

json.dump(p, f, default=show_object, indent=4)
```

After load, output is dictionary:

```python
{'name': 'sameer', 'age': 25, 'city': 'LKO'}
<class 'dict'>
```

---

## 10. Pickle and Unpickle

I also practiced binary object persistence using `pickle`:

```python
pickle.dump(p, f)   # serialize to data.pkl
p = pickle.load(f)  # restore object
```

After unpickling, object method worked:

`hi my name is sameer and I am 25 years old and I live in LKO`

So pickle preserves Python object structure better than JSON for custom
instances.

---

## 11. Task Practice Summary

### Task 1 - Final line from file

- Function: `get_final_line(filename)`
- File used: `tasks/sample.txt`
- Output: `Ahmad`
- Empty file case handled using `None`

### Task 2 - Vowel frequency dictionary

- Function: `count_vowels(filename)`
- Counts both lowercase and uppercase vowels separately
- Output:
  `{'a': 3, 'e': 2, 'i': 1, 'o': 0, 'u': 0, 'A': 1, 'E': 0, 'I': 0, 'O': 0, 'U': 0}`

### Task 3 - Multiply columns and total

- Function: `process_file(filename)`
- Input format: two numbers per line
- Added product in third column
- Appended final total line
- `tasks/numbers.txt` now ends with `Total    70`

### Task 4 - Reverse + swap words

- Function: `transform_file(input_file, output_file)`
- `tasks/input.txt` content:
  - `abc def`
  - `ghi jkl`
- `tasks/output.txt` content:
  - `fed cba`
  - `lkj ihg`

### Task 5 - Serialized word frequency

- Functions:
  - `create_frequency_dict(text, filename)`
  - `get_word_counts(filename, word_list)`
- Serialized full frequency map into `tasks/freq.json`
- Query list: `['alice', 'wonder', 'natural']`
- Output: `{'alice': 4, 'wonder': 0, 'natural': 1}`

---

## 12. Key Takeaways

1. Use `with open(...)` as default file handling style
2. Choose file mode carefully (`w` overwrites, `a` appends)
3. `seek()` and `tell()` are useful when read/write position matters
4. JSON is great for readable data exchange
5. Pickle is useful for Python object persistence
6. Task practice improved confidence with real file input/output problems

---

## My Day 11 Summary

Day 11 gave me practical confidence in handling files and storing data in
different formats. I can now read, write, transform, and serialize data using
text files, JSON, and pickle, and I solved 5 notebook tasks using actual input
and output files.
