(The file `c:\Users\samee\AI_Engineer_Journey\Phase-02-Python-DSA\Day-33-28-Apr-2026-Leetcode_questions\README.md` exists, but is empty)
# Day 33: Rotated-sorted array problems (notebook-based)

## Overview
This folder contains Day 33 notebooks covering two common LeetCode patterns on rotated sorted arrays:
- `search_in_rotated_arr_2.ipynb` — search for a target in a rotated sorted array that may contain duplicates (LeetCode: Search in Rotated Sorted Array II).
- `min_in_sorted_array.ipynb` — find the minimum element in a rotated sorted array (handles rotation pivot detection).

## Notebook / Practice Files
- `search_in_rotated_arr_2.ipynb` — demonstrates an optimized binary-search-style approach that handles duplicates by shrinking the search window when endpoints equal the middle element.
- `min_in_sorted_array.ipynb` — shows a brute-force and an optimized binary-search approach to locate the minimum element in a rotated array.

## What The Notebooks Contain
- `search_in_rotated_arr_2.ipynb` explains handling duplicates (when `nums[low] == nums[mid] == nums[high]`) by incrementing `low` and decrementing `high` to avoid ambiguous mid positions, then uses half-interval logic to decide which side is sorted and move `low`/`high` accordingly.
- `min_in_sorted_array.ipynb` contains both:
	- A brute-force O(n) scan to find the minimum.
	- An optimized binary-search variant that compares `nums[mid]` with `nums[high]` to move towards the minimum while maintaining O(log n) average time.

## Complexity
- `search_in_rotated_arr_2`: Best/average time O(log n), worst-case O(n) when many duplicates force linear shrinking; Space O(1).
- `min_in_sorted_array` (binary-search variant): Time O(log n) average, Space O(1).

## Example (conceptual)
- For `nums = [7,7,7,7,7,7,7,1,2,3,4,5,7,7]` and `target = 1`, the search notebook demonstrates finding index `7` by handling duplicates around the midpoint.
- For `nums = [4,5,6,7,0,1,2]`, the min-in-rotation notebook returns `0`.

---
Run the notebooks for the exact printed outputs and step-through examples.

