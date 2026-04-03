# Day 15 Notes: Introduction to Time Complexity

## 1) What Is Time Complexity
- Time complexity describes how the number of operations grows as input size grows.
- It helps compare algorithm efficiency independent of machine speed.

Core idea:
- We focus on growth trend, not exact runtime in seconds.

## 2) Why It Matters in DSA
- In Data Structures and Algorithms, choosing the right approach is critical.
- A slow-growing algorithm scales better for large input sizes.

Example thinking:
- An algorithm with linear growth is usually better than one with quadratic growth for big inputs.

## 3) Input Size (`n`)
- `n` usually means the size of input.
- Complexity is written as a function of `n`.

Examples:
- Array length
- Number of nodes in a tree
- Number of elements to search/sort

## 4) Big-O Notation
- Big-O gives an upper bound on growth rate.
- It describes worst-case growth behavior.

Common forms:
- `O(1)` constant
- `O(log n)` logarithmic
- `O(n)` linear
- `O(n log n)` linearithmic
- `O(n^2)` quadratic

## 5) Dropping Constants and Lower Terms
- In Big-O, constants are ignored.
- Lower-order terms are ignored for large `n`.

Rules:
- `O(3n + 5)` becomes `O(n)`
- `O(n^2 + n)` becomes `O(n^2)`

## 6) Best, Average, Worst Case
- Best case: minimum operations.
- Average case: expected operations.
- Worst case: maximum operations.

Practical focus:
- Most DSA analysis starts with worst-case complexity.

## 7) Basic Loop Analysis
- Single loop over `n` items -> `O(n)`
- Nested loop over `n x n` -> `O(n^2)`
- Loop reducing input by half each step -> `O(log n)`

## 8) Common Examples Studied
- Access element by index in list: `O(1)`
- Linear search: `O(n)`
- Binary search (sorted data): `O(log n)`
- Simple double-loop comparisons: `O(n^2)`

## 9) Time vs Space Tradeoff
- Faster algorithms can use extra memory.
- Memory-efficient approaches may take more time.

Takeaway:
- Good solutions balance both time and space based on problem constraints.

## 10) Practical Complexity Comparison
- For small `n`, many approaches feel similar.
- For large `n`, growth rate dominates performance.

Quick intuition:
- `O(log n)` and `O(n)` scale much better than `O(n^2)` as `n` increases.

## 11) Day 15 Summary
- Time complexity is about scalability.
- Big-O helps communicate algorithm behavior clearly.
- Loop structure gives a strong first estimate of complexity.
- Learning complexity early improves problem-solving decisions in DSA.
- Start solving DSA questions by writing complexity after each approach.

## 12) Practice Checklist for Complexity
- Identify loop boundaries before counting steps.
- Check loop updates carefully (`+1`, `*2`, `/2`) to detect `O(n)` vs `O(log n)`.
- For nested loops, multiply dominant costs.
- Ignore constants and lower terms in final Big-O form.
