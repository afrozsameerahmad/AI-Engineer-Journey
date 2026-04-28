# Day 32 Notes — Search in Rotated Array and First/Last Occurrence

## Problem 1 — Search in Rotated Sorted Array (LeetCode 33)

Problem: Given a rotated sorted array (ascending order originally, then rotated at some pivot) and a target, return the index of the target if found, otherwise return -1.

Examples:
- nums = [4,5,6,7,0,1,2], target = 0 -> 4
- nums = [4,5,6,7,0,1,2], target = 3 -> -1

Approach (modified binary search):

- At each step compute `mid`. One of the halves [low..mid] or [mid..high] must be sorted.
- Determine which half is sorted by comparing `nums[low]` and `nums[mid]`.
- If the sorted half contains the target, narrow to that half; otherwise search the other half.

Example implementation from notebook:

```python
def search_rotated(nums, target):
	if not nums:
		return -1
	low, high = 0, len(nums)-1
	while low <= high:
		mid = low + (high-low)//2
		if nums[mid] == target:
			return mid
		# left half sorted
		if nums[low] <= nums[mid]:
			if nums[low] <= target < nums[mid]:
				high = mid - 1
			else:
				low = mid + 1
		# right half sorted
		else:
			if nums[mid] < target <= nums[high]:
				low = mid + 1
			else:
				high = mid - 1
	return -1

print(search_rotated([4,5,6,7,0,1,2], 0))
```

Complexity:
- Time O(log n), Space O(1).

Edge cases and notes:
- If array is not rotated (fully sorted), algorithm still works because left half will appear sorted initially.
- If duplicates exist, the simple comparisons `nums[low] <= nums[mid]` can be ambiguous; consider linear fallback or adjusted logic when duplicates are allowed.

Notebook examples (actual inputs used in the session):

- Brute-force cell:

```python
nums = [11,15,20,1,4,5,6,8,9,10]
target = 8
# prints index where target found (brute-force loop)
```

- Optimized cell:

```python
nums = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]
target = 4
result = search_rotated(nums, target)  # returns index or -1
```

---

## Problem 2 — First & Last Occurrence (LeetCode 34)

Problem: Given a sorted array (may contain duplicates) and a target value, return the starting and ending position of the target in the array. If the target is not found, return [-1, -1].

Examples:
- nums = [5,7,7,8,8,10], target = 8 -> [3,4]
- nums = [5,7,7,8,8,10], target = 6 -> [-1,-1]

Approach (two binary searches):

- Use a helper binary search to find the leftmost (first) index of `target`:
  - When `nums[mid] < target` move `low = mid + 1`.
  - When `nums[mid] >= target` move `high = mid - 1` and keep candidate.
- Use a similar binary search to find the rightmost (last) index of `target`:
  - When `nums[mid] <= target` move `low = mid + 1`.
  - When `nums[mid] > target` move `high = mid - 1` and keep candidate.

Example implementation from notebook:

```python
def find_first_last(nums, target):
	def find_left():
		low, high = 0, len(nums)-1
		idx = -1
		while low <= high:
			mid = low + (high-low)//2
			if nums[mid] < target:
				low = mid + 1
			else:
				if nums[mid] == target:
					idx = mid
				high = mid - 1
		return idx

	def find_right():
		low, high = 0, len(nums)-1
		idx = -1
		while low <= high:
			mid = low + (high-low)//2
			if nums[mid] > target:
				high = mid - 1
			else:
				if nums[mid] == target:
					idx = mid
				low = mid + 1
		return idx

	return [find_left(), find_right()]

print(find_first_last([5,7,7,8,8,10], 8))
```

Complexity:
- Two binary searches → Time O(log n), Space O(1).

Edge cases and notes:
- If the array is empty return `[-1, -1]` immediately.
- Returning indexes vs values: these helpers return indexes; adapt if you need values.

Notebook examples (actual inputs used in the session):

```python
nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target = 3
# brute-force cell prints: first and last indexes (e.g., 2 and 6)

first = find_bound(nums, target, True)
last = find_bound(nums, target, False)
print(first, last)
```

---

## Takeaways & Patterns

1. Many array index problems reduce to binary-search templates; small invariants change (which half to choose, whether to update candidate index) but structure is similar.
2. For rotated arrays: determine the sorted half each iteration.
3. For boundary searches: run binary search twice (left and right) with slightly different loop invariants.

## Suggested Practice

- Implement repeatable helpers: `binary_search_left(nums, target)` and `binary_search_right(nums, target)` and reuse them in problems.
- Experiment with arrays containing duplicates to see where comparison checks need to be adjusted.

Files used in these notes:
- [search_in_rotated_arr.ipynb](search_in_rotated_arr.ipynb)
- [first_occur_&_last.ipynb](first_occur_&_last.ipynb)

