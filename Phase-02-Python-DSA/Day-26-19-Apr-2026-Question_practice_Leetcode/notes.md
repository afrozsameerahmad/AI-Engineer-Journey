# Day 26: LeetCode Question Practice

## Overview
This day focuses on practicing the "Set Matrix Zeroes" problem (LeetCode 73) with an emphasis on in-place matrix transformation and space optimization. The session follows the pattern used in Day 25: start with a straightforward approach, then implement an optimized solution.

## Notebook Files
- `set_matrix_zero.ipynb`: Notebook with worked solutions, explanations, and simple tests.

---

## 1) Set Matrix Zeroes

### Problem
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

### Approach A: Extra space (rows/cols sets)
Scan the matrix once to record which rows and columns contain zeros (use boolean arrays or sets). In a second pass, zero out any cell whose row or column is recorded.

```python
# high-level sketch
rows = set()
cols = set()
for i in range(m):
   for j in range(n):
      if matrix[i][j] == 0:
         rows.add(i)
         cols.add(j)

for i in range(m):
   for j in range(n):
      if i in rows or j in cols:
         matrix[i][j] = 0
```

Complexity:
- Time: O(m*n)
- Space: O(m + n)

### Approach B: Optimized in-place (first row/column as markers)
Use the first row and first column as marker storage: when matrix[i][j] == 0, set matrix[i][0] = 0 and matrix[0][j] = 0. Keep two boolean flags to remember whether the original first row or first column contained any zeros. Then zero cells based on markers and finally zero first row/column if required.

```python
# sketch for optimized in-place
first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

for i in range(1, m):
   for j in range(1, n):
      if matrix[i][j] == 0:
         matrix[i][0] = 0
         matrix[0][j] = 0

for i in range(1, m):
   for j in range(1, n):
      if matrix[i][0] == 0 or matrix[0][j] == 0:
         matrix[i][j] = 0

if first_row_has_zero:
   for j in range(n):
      matrix[0][j] = 0
if first_col_has_zero:
   for i in range(m):
      matrix[i][0] = 0
```

Complexity:
- Time: O(m*n)
- Space: O(1) extra (in-place)

---

## Practical Takeaways
1. Marker techniques using existing rows/columns reduce auxiliary space to O(1).
2. Always preserve information about the marker row/column before overwriting it (use flags).
3. Process matrix rows/cols carefully to avoid corrupting markers early — using separate passes helps.

## Next practice suggestions
- Try related matrix problems: rotate matrix, spiral order traversal, search in matrix.
- Add additional test cases (single-row, single-column, all-zero matrix) to the notebook.

