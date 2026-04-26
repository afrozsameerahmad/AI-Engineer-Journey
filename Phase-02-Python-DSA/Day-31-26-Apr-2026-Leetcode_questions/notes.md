# Day 31 Notes — Search Insert Position and Floor/Ceil

## Problem 1 — Search Insert Position (LeetCode 35)

Problem: Given a sorted array of distinct integers and a target, return the index if the target is found. If not, return the index where it would be inserted to keep the array sorted.

Examples:
- nums = [1,3,5,6], target = 5 -> 2
- nums = [1,3,5,6], target = 2 -> 1
- nums = [1,3,5,6], target = 7 -> 4

Approaches:

- Brute/Utility: check membership and use `list.insert()` to demonstrate insertion index (not optimal because insert is O(n)). Example from the notebook:

```python
nums = [1,3,4,5,8,9,14]
target = 16
if target in nums:
	print(nums.index(target))
else:
	low, high = 0, len(nums)-1
	while low <= high:
		mid = low + (high-low)//2
		if nums[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	print(low)
	# nums.insert(low, target)  # demonstrates where insertion would occur
```

- Optimal (binary search): standard binary search variant that returns `low` as the insertion position when the loop exits. Example:

```python
def searchInsert(nums, target):
	low, high = 0, len(nums)-1
	while low <= high:
		mid = (low + high)//2
		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return low

print(searchInsert([1,3,4,5,8], 11))
```

Complexity:
- Binary-search approach: Time O(log n), Space O(1).

Edge cases and notes:
- If target < nums[0], `low` becomes 0 and function returns 0.
- If target > nums[-1], `low` becomes `len(nums)` and function returns append index.
- Works for arrays of unique elements as assumed here.

---

## Problem 2 — Floor & Ceil

Problem: Given a sorted array (may contain duplicates) and a target, compute:
- Floor: largest number <= target (or -1 / None if none exists)
- Ceil: smallest number >= target (or -1 / None if none exists)

Example from notebook:

```python
nums = [3,4,4,4,8,9,9,10,12,12,14,15]
target = 6
floor = -1
ceil = -1
low = 0
high = len(nums)-1
while low <= high:
	mid = low + (high-low)//2
	if nums[mid] == target:
		floor = nums[mid]
		ceil = nums[mid]
		break
	elif nums[mid] > target:
		ceil = nums[mid]
		high = mid - 1
	else:
		floor = nums[mid]
		low = mid + 1
print(floor, ceil)
```

Explanation:
- Maintain two variables `floor` and `ceil` initialized to a sentinel (e.g., -1) or `None`.
- When `nums[mid] > target` move `high` left and update `ceil` to `nums[mid]` (candidate).
- When `nums[mid] < target` move `low` right and update `floor` to `nums[mid]` (candidate).
- If exact match found, both `floor` and `ceil` are that value.

Complexity:
- Time O(log n), Space O(1).

Edge cases and notes:
- Duplicates: algorithm naturally handles duplicates because it tracks the nearest candidate each side.
- If the array has no elements <= target, `floor` remains the sentinel.
- If the array has no elements >= target, `ceil` remains the sentinel.

---

## Takeaways & Patterns

1. Many index/position problems reduce to returning `low` or tracking candidates while binary-searching.
2. Carefully choose sentinels for absent values (`-1`, `None`, or `float('inf')`/`-inf`) depending on downstream usage.
3. Keep the loop invariant clear: when using `while low <= high`, exit case `low` is the insertion point.

## Next steps (suggested practice)

- Try converting `floor/ceil` into helper functions that return indexes instead of values.
- Test the `searchInsert` implementation on small arrays, duplicates, and boundary targets.

Files used in these notes:
- [search_insert_position.ipynb](search_insert_position.ipynb)
- [floor_&_Ceil.ipynb](floor_&_Ceil.ipynb)

