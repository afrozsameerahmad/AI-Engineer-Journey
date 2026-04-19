# Day 26: LeetCode Question Practice

## Overview
This day focuses on practicing the "Set Matrix Zeroes" problem (LeetCode 73). The exercises follow the same pattern used on Day 25: present a simple/brute-force solution, then refactor to an optimized approach and compare complexities.

## Notebook Files
- `set_matrix_zero.ipynb`: Notebook with brute-force and optimized in-place solutions, plus test cells.

## What Was Practiced
- Brute-force recording of rows/columns to zero.
- In-place marker technique using first row/first column to achieve O(1) extra space.
- Edge-case reasoning for single-row/single-column and all-zero matrices.

## Complexity Snapshot

| Problem | Approach | Time | Space |
|---|---|---:|---:|
| Set Matrix Zeroes | Extra-space (rows/cols sets) | O(m*n) | O(m + n) |
| Set Matrix Zeroes | In-place markers (first row/col) | O(m*n) | O(1) |

## Key Patterns Practiced
1. Use of existing data structure space for markers (first row/column).
2. Two-pass processing to avoid early corruption of marker data.
3. Explicit flagging for marker rows/columns when they overlap with data.

## Difficulty Level
Medium (matrix manipulation, careful in-place updates)

---
See `notes.md` for detailed explanation, code sketches, and testing suggestions.

