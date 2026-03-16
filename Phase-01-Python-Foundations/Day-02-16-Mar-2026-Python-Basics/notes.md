# Notes are written by Copilot using all files data 

# Day 02 - Operators, Conditions, Loops, Modules, and Mini Projects

Date: 16 March 2026

## Day 02 Summary

Today covered practical Python logic building through:

1. Operators (`exercises/operators.py`)
2. Conditional branching (`exercises/if_else.py`)
3. Loops and pattern printing (`exercises/loops.py`)
4. Loop control statements and prime range logic (`exercises/loop_control_stat.py`)
5. Standard modules (`exercises/modules.py`)
6. Practice set in `practice.py`
7. Mini projects in `mini_projects/`

---

## 1. Operators (`exercises/operators.py`)

### Arithmetic

- `+`, `-`, `*`, `/`, `//`, `%`, `**`

### Assignment

- `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

### Comparison

- `==`, `!=`, `>`, `<`, `>=`, `<=`

### Logical

- `and`, `or`, `not`

### Bitwise

- `&`, `|`, `^`, `~`, `<<`, `>>`

### Membership

- `in`, `not in`

### Identity

- `is`, `is not`

---

## 2. IF-ELSE Practice (`exercises/if_else.py`)

Main implementation:

- Email/password login check
- Nested condition for retrying password
- Multiple `elif` decision paths

Concept used:

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

---

## 3. Loops and Patterns (`exercises/loops.py`)

Implemented items:

- `while` loop table printing
- `while ... else` example
- `for` loops with `range(start, stop, step)`
- Nested loops (`for i` inside `for j`)
- Star pattern (increasing and reverse)
- Number palindrome-style pattern:

```text
1
121
12321
1234321
...
```

---

## 4. Loop Control Statements (`exercises/loop_control_stat.py`)

- `break` to terminate loop early
- `continue` to skip current iteration
- `pass` as placeholder statement
- Prime numbers in a user-given range using `for ... else`

---

## 5. Modules (`exercises/modules.py`)

Used modules:

- `math` (`floor` example)
- `keyword` (`kwlist`)
- `random` (`random`, `randint`)
- `datetime` (`datetime.now()`)
- `help('modules')` exploration

---

## 6. Practice File (`practice.py`)

Problems solved:

1. Sum of digits of a 3-digit number
2. Minimum of three numbers
3. Calculator with operators `+ - * / % //` and divide-by-zero checks
4. Menu-based ATM-style choice using `if-elif-else`
5. Multiplication table using `while`
6. Series: $1/1! + 1/2! + ... + 1/n!$

---

## 7. Mini Projects

### `mini_projects/guessing_game.py`

- Jackpot number generated using `random.randint(1, 100)`
- User keeps guessing until correct
- Program gives hints: too high / too low
- Attempts counter displayed at end

### `mini_projects/population_problem.py`

- Initial population: `1000`
- Annual growth rate: `10%`
- Prints population at end of each of 10 years

---

## Files Covered in Day 02

```text
notes.md
README.md
practice.py
exercises/operators.py
exercises/if_else.py
exercises/loops.py
exercises/loop_control_stat.py
exercises/modules.py
mini_projects/guessing_game.py
mini_projects/population_problem.py
```

---

## Day 02 Outcome

- Better command over decision making (`if-elif-else`)
- Practical use of all major Python operators
- Solid understanding of loops and loop controls
- Intro to Python standard modules
- Real practice through small problem statements and mini projects
