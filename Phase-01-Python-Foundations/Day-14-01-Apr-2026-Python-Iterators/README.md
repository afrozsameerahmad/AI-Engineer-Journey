# Day 14: Python Iterators and Generators

## Overview
This day focuses on how Python processes data one item at a time using the iteration protocol.

You covered:
- Iteration basics
- Iterable vs iterator
- Internal behavior of `for` loop
- Manual iteration with `next()` and `StopIteration`
- Generator functions and generator expressions
- Infinite generators
- Building a custom range-like iterable and iterator

## Folder Structure
- `exercise/iterators.ipynb`
	- Iterator fundamentals
	- `iter()` and `next()` usage
	- Custom loop implementation (`own_loop`)
	- Identity behavior of iterator objects

- `exercise/generators.ipynb`
	- `yield` basics
	- Generator examples (`gen_demo`, `square_gen`, `my_range`)
	- Generator expression
	- Memory comparison list vs generator
	- Infinite even stream and Fibonacci generator

- `practice/range_fn_own.ipynb`
	- Custom iterable class: `MyRange`
	- Custom iterator class: `MyRange_iterator`
	- Manual implementation of `__iter__` and `__next__`

- `notes.md`
	- Consolidated theory and key takeaways for revision

## Key Learning Outcomes
After completing Day 14, you should be able to:
1. Explain the difference between iterable and iterator.
2. Use `iter()` and `next()` confidently.
3. Understand why and where `StopIteration` happens.
4. Write simple generator functions with `yield`.
5. Use generator expressions for memory-efficient iteration.
6. Build custom iterable/iterator classes.

## Quick Revision
- Iterable gives an iterator via `iter(...)`.
- Iterator gives next item via `next(...)`.
- Generator is a concise iterator creator.
- `yield` pauses and resumes function state.
- Lazy iteration usually saves memory.

## Suggested Practice
1. Add step support to `MyRange` (like `range(start, end, step)`).
2. Create an infinite odd-number generator.
3. Build a generator that yields prime numbers.
4. Chain two generators for filtering then transformation.

## Date
01-Apr-2026
