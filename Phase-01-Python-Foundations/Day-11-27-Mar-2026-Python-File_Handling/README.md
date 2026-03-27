# Day 11 - Python File Handling, Serialization and Deserialization

**Date:** 27 March 2026

This folder contains Day 11 work focused on file operations in Python:
reading/writing text files, working with binary files, JSON based data storage,
and pickle based object serialization.

---

# Day 11 Coverage

1. Text files vs binary files
2. File lifecycle: open, read/write, close
3. File modes: `r`, `w`, `a`, `rb`, `wb`
4. `write()` and `writelines()`
5. Reading patterns: `read()`, `read(n)`, `readline()`
6. Context manager with `with open(...)`
7. File pointer methods: `seek()` and `tell()`
8. Chunk based read for large files
9. Binary copy of image files
10. JSON serialization and deserialization
11. Custom object serialization using `json.dump(..., default=...)`
12. Pickling and unpickling (`pickle.dump`, `pickle.load`)

---

# Exercise Notebooks

1. `exercises/file_handling.ipynb`
   - Practiced text file creation and update
   - Compared overwrite (`w`) vs append (`a`)
   - Read files in full, partial, and line-by-line style
   - Used `with` block for auto-close
   - Used `seek()` and `tell()` for file pointer control
   - Created and processed `big_file.txt`
   - Copied `profile.jpeg` to `copy_profile.jpeg` in binary mode

2. `exercises/serialization_deserialization.ipynb`
   - Serialized list/dict/tuple using JSON
   - Deserialized JSON back to Python data
   - Observed tuple becomes list after JSON load
   - Serialized a custom `Person` object using `default` handler
   - Pickled and unpickled `Person` object to/from `data.pkl`

---

# Task Notebooks (`tasks/`)

1. `task1.ipynb`
   - Implemented `get_final_line(filename)`
   - Returned last line from file, or `None` if file is empty
   - Example output from `sample.txt`: `Ahmad`

2. `task_2.ipynb`
   - Implemented `count_vowels(filename)`
   - Counted uppercase and lowercase vowels using dictionary
   - Example output on `sample.txt`:
     `{'a': 3, 'e': 2, 'i': 1, 'o': 0, 'u': 0, 'A': 1, 'E': 0, 'I': 0, 'O': 0, 'U': 0}`

3. `task_3.ipynb`
   - Implemented `process_file(filename)`
   - Read two numbers per line, wrote product as third column
   - Added final `Total` row
   - Updated `numbers.txt` now contains product column and `Total 70`

4. `task_4.ipynb`
   - Implemented `transform_file(input_file, output_file)`
   - Reversed each word and swapped order per line
   - `input.txt` -> `output.txt`
   - Example:
     - `abc def` -> `fed cba`
     - `ghi jkl` -> `lkj ihg`

5. `task_5.ipynb`
   - Built word-frequency dictionary from Alice text
   - Serialized frequency dictionary to `freq.json`
   - Queried given word list `['alice', 'wonder', 'natural']`
   - Result: `{'alice': 4, 'wonder': 0, 'natural': 1}`

---

# Important Day 11 Files

- `tasks/sample.txt`
- `tasks/input.txt`
- `tasks/output.txt`
- `tasks/numbers.txt`
- `tasks/freq.json`
- `exercises/data.json`
- `exercises/data.pkl`
- `exercises/profile.jpeg`
- `exercises/copy_profile.jpeg`
- `exercises/big_file.txt`

---

# Folder Structure

```text
notes.md
README.md
exercises/
    file_handling.ipynb
    serialization_deserialization.ipynb
    big_file.txt
    data.json
    data.pkl
    profile.jpeg
    copy_profile.jpeg
tasks/
    task1.ipynb
    task_2.ipynb
    task_3.ipynb
    task_4.ipynb
    task_5.ipynb
    sample.txt
    input.txt
    output.txt
    numbers.txt
    freq.json
```

---

# Learning Outcome

- Understood practical text file operations in Python
- Learned safe file handling using context manager
- Practiced file-pointer navigation with `seek()` and `tell()`
- Learned binary file handling by copying image files
- Understood JSON and pickle workflows for data persistence
- Solved 5 file-handling tasks with real input/output files

# Day 12 Plan

Topics I can continue with next:

- Exception handling with file operations
- CSV handling and structured tabular data
