(# Day 32: LeetCode Questions — Rotated Array & First/Last Occurrence)

## Overview
This day covers two common interview problems that build on binary-search variants applied to ordered arrays:

- `Search in Rotated Sorted Array` (find a target's index when the sorted array has been rotated)
- `First & Last Occurrence` (find the starting and ending index of a target in a sorted array, duplicates allowed)

Each notebook demonstrates both straightforward and optimized approaches, with edge-case handling and complexity notes.

## Notebook Files
- [search_in_rotated_arr.ipynb](search_in_rotated_arr.ipynb)
- [first_occur_&_last.ipynb](first_occur_&_last.ipynb)

## What Was Practiced

- Adapting binary-search to rotated arrays by identifying which half is sorted.
- Using binary search to find leftmost and rightmost occurrences (index boundaries) in presence of duplicates.
- Handling edge cases: empty arrays, all elements equal, target outside range, and full rotation.

## Complexity Snapshot

| Problem | Approach | Time | Space |
|---|---|---:|---:|
| Search in Rotated Sorted Array | Modified binary search checking sorted half | O(log n) | O(1) |
| First & Last Occurrence | Two binary searches (leftmost + rightmost) | O(log n) | O(1) |

## Key Patterns Practiced
1. Determine which side (left/right) of mid is sorted to decide where to continue searching in rotated arrays.
2. To find first/last occurrence, run binary search twice with inclusive/exclusive adjustments to locate boundaries.
3. Use `mid = low + (high-low)//2` for clarity and to avoid overflow in other languages.

## Difficulty Level
Easy–Medium — good practice for interview-style variations on binary search.

---
See `notes.md` for detailed explanations, example runs, and code snippets extracted from the notebooks.

## Notebook Examples (actual inputs shown in the notebooks)

- `search_in_rotated_arr.ipynb` sample arrays/targets used:
	- brute force: `nums = [11,15,20,1,4,5,6,8,9,10]`, `target = 8` (prints index)
	- optimized: `nums = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]`, `target = 4` (returns index or -1)
- `first_occur_&_last.ipynb` sample array used:
	- `nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]`, `target = 3` (first and last occurrence indexes)

Note: The README gives canonical LeetCode examples; the notebooks include the specific sample arrays used during the live session.

