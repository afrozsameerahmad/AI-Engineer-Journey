
# Day 30: lower_bound & upper_bound (notebook-based)

## Overview
This folder contains two Day 30 notebooks demonstrating inclusive-index binary-search implementations for finding a lower bound (first index with value >= target) and an upper bound (first index with value > target) on a sample array.

## Notebook / Practice Files
- `lower_bound.ipynb` — inclusive-index `lower_bound` example (uses `while low <= high`).
- `upper_bound.ipynb` — inclusive-index `upper_bound` example (uses `while low <= high`).

## What The Notebooks Contain
- Sample array used in both notebooks: `[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]` with `target = 7`.
- `lower_bound.ipynb` finds the first index where `nums[mid] >= target` by setting `lb = mid` and `high = mid-1` when true; otherwise `low = mid+1`.
- `upper_bound.ipynb` finds the first index where `nums[mid] > target` by setting `ub = mid` and `high = mid-1` when true; otherwise `low = mid+1`.

## Example (from notebooks)
- For `target = 7` with the sample array:
	- `lower_bound` finds the index of the first `7` (prints that index).
	- `upper_bound` finds the first index with value greater than `7` (prints that index, or `n` if none).

## Complexity
- Time: O(log n)
- Space: O(1)

---
Run the notebooks for the exact printed outputs and step-through examples.

