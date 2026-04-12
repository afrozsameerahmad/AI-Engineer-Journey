# Day 21: Question Practice (Arrays)

## Overview
This day focuses on common array interview-style questions and optimized thinking for each problem.

Problems practiced:
- Check whether an array is sorted
- Find the second largest element
- Remove duplicates from an array
- Right rotate an array (by 1 and by `k` steps)

## Practice Files
- `ele_sort.ipynb`: Check if array is sorted using adjacent comparison
- `second_largest_ele.ipynb`: Two methods for second largest (sort-based and one-pass)
- `remove_dup.ipynb`: Deduplication using dictionary keys and write-back
- `rotate.ipynb`: Right rotation by one step and by `k` steps
- `revision_sheet.md`: Quick interview revision (patterns, templates, edge cases)

## Learning Objectives
- Build strong loop-based reasoning for array traversals
- Compare brute-force vs better approaches using complexity
- Use tracking variables to avoid unnecessary sorting
- Understand when hash-based structures help in deduplication
- Apply index-shifting and slicing for rotation problems

## Complexity Snapshot
- Sorted Check: Time $O(n)$, Space $O(1)$
- Second Largest (sort): Time $O(n \log n)$
- Second Largest (one-pass): Time $O(n)$, Space $O(1)$
- Remove Duplicates (dict-based): Time $O(n)$ average, Space $O(n)$
- Right Rotate by `k`: Time $O(n)$, Space $O(k)$

---
See `notes.md` for detailed explanation of each approach and implementation logic.
