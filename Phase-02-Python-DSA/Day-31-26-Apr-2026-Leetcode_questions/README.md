(# Day 31: LeetCode Questions — Search & Floor/Ceil)

## Overview
This day covers two common binary-search-related problems from LeetCode:

- `Search Insert Position` (find the index to insert a target into a sorted array)
- `Floor & Ceil` (compute the floor and ceil values relative to a target in a sorted array)

Both notebooks show a straightforward approach and an optimal binary-search variant with complexity notes and small examples.

## Notebook Files
- [search_insert_position.ipynb](search_insert_position.ipynb)
- [floor_&_Ceil.ipynb](floor_&_Ceil.ipynb)

## What Was Practiced

- Converting linear/brute-force logic into efficient binary-search solutions.
- Handling edge cases for insertion points, duplicates, and targets outside the array range.
- Writing compact, correct binary-search loops that return indexes or values rather than booleans.

## Complexity Snapshot

| Problem | Approach | Time | Space |
|---|---|---:|---:|
| Search Insert Position | Linear insert / membership + insert | O(n) | O(1) |
| Search Insert Position | Binary search | O(log n) | O(1) |
| Floor & Ceil | Binary search tracking floor/ceil | O(log n) | O(1) |

## Key Patterns Practiced
1. Use binary search to find an insertion point (return `low` after search loop).
2. Track candidate floor/ceil values while moving `low`/`high` pointers.
3. Prefer index math `mid = low + (high-low)//2` to avoid overflow and for clarity.

## Difficulty Level
Easy — fundamentals of binary search and index arithmetic; good practice for interview basics.

---
See `notes.md` for detailed explanations, example runs, and code snippets extracted from the notebooks.

