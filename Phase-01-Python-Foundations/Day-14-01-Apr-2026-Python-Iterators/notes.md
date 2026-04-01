# Day 14 Notes: Iterators and Generators

## 1) Iteration
- Iteration means visiting items one by one in a collection.
- A `for` loop performs iteration internally.

Example idea:
- Looping over `[1, 2, 3, 4, 5]` prints each element in order.

## 2) Iterable vs Iterator
- Iterable: an object that can return an iterator using `iter()`.
- Iterator: an object that keeps state and gives next value using `next()`.

Rule to remember:
- Every iterator is iterable.
- Not every iterable is an iterator.

Practical check:
- Iterable usually has `__iter__`.
- Iterator has both `__iter__` and `__next__`.

## 3) Why Iterators Matter
- They allow lazy access to data.
- They can be memory efficient.

From class examples:
- List comprehension for many numbers takes more memory.
- `range(...)` object takes much less memory compared to a large list.

## 4) How `for` Loop Works Internally
Conceptually, this is what `for` does:
1. Create iterator from iterable using `iter(iterable)`.
2. Repeatedly call `next(iterator)`.
3. Stop when `StopIteration` is raised.

Manual example learning:
- Calling `next()` one extra time after items are finished raises `StopIteration`.

## 5) Custom Loop Implementation
Function created in exercise:
- `own_loop(iterable)`
- Uses `while True`, `next()`, and catches `StopIteration`.

It was tested with:
- list, range, tuple, set, and dictionary.

## 6) Important Iterator Behavior
- `iter(iterator_object)` returns the same iterator object.
- Identity check with `id(...)` confirms this behavior.

## 7) Generators
- Generator is an easy way to create iterators.
- A function with `yield` becomes a generator function.

`yield` vs `return`:
- `return` ends function execution.
- `yield` pauses execution and resumes from same state next time.

## 8) Generator Examples Practiced
- Simple `gen_demo()` yielding three statements.
- `square_gen(n)` yielding squares.
- `my_range(start, end)` as generator version of range-like behavior.
- Generator expression: `(i**2 for i in range(10))`.

## 9) Benefits of Generators
- Memory efficient (values generated on demand).
- Easy to write and use.
- Useful for infinite streams.
- Good for pipeline/chaining style processing.

Memory comparison done with `sys.getsizeof`:
- Large list size is much bigger than generator size.

## 10) Infinite Stream and Chaining
- Infinite even-number generator (`all_even`) using `while True`.
- Fibonacci generator (`fibonacci_gen`) and consuming first N values with `next()`.

## 11) Practice: Build Range from Scratch
Custom classes implemented:
- `MyRange` (iterable)
- `MyRange_iterator` (iterator)

`MyRange_iterator.__next__` logic:
- Raises `StopIteration` when start reaches end.
- Otherwise returns current value and increments state.

This reinforces how Python iteration protocol works under the hood.
