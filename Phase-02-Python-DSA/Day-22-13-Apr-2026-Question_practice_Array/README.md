# Day 22: Array Practice - Question Practice

## Overview
This day focuses on fundamental array problems that build intuition for array manipulation and two-pointer techniques:

- Check if Array is Sorted
- Remove Duplicates from Sorted Array (In-Place)

These are classic array problems commonly asked in interviews and essential for mastering array-based algorithms.

## Exercises
The files in this folder are:

- `if_array_is_sorted_or_not.ipynb`: Linear scan to verify if an array is sorted in ascending order
- `remove_duplicates_from_sorted_arr.ipynb`: Two-pointer technique to remove duplicates in-place

## Learning Objectives
- Understand basic linear scan patterns on arrays
- Master the **two-pointer technique** for in-place array modifications
- Learn why the sorted property of an array enables efficient algorithms
- Compare brute force vs. optimal approaches for array problems
- Practice analyzing both time and space complexity

## Complexity Snapshot

| Problem | Approach | Time | Space |
|---------|----------|------|-------|
| Check if Sorted | Linear Scan | $O(n)$ | $O(1)$ |
| Remove Duplicates (Brute) | Extra List | $O(n)$ | $O(n)$ |
| Remove Duplicates (Optimal) | Two-Pointer | $O(n)$ | $O(1)$ |

## Key Concepts
1. **Linear Scan**: Iterate once through the array to check a property
2. **Two-Pointer Technique**: Use two pointers moving at different speeds or in different directions to solve in-place modification problems
3. **Leveraging Sorted Property**: Sorted arrays enable optimizations that don't work on unsorted data

## Difficulty Level
⭐ **Easy** — Good warm-up problems for DSA practice and interview prep

---
See `notes.md` for detailed explanations, code walkthroughs, and complexity analysis.
