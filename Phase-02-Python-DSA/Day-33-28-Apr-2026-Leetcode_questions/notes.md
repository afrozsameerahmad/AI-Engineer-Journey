# Day 33 Notes — Rotated-sorted array problems

## Problems covered
- `search_in_rotated_arr_2`: Search a target in a rotated sorted array that may contain duplicates (LeetCode: Search in Rotated Sorted Array II).
- `min_in_sorted_array`: Find the minimum element in a rotated sorted array (find rotation pivot / smallest value).

## Key ideas
- Rotated sorted arrays are sorted arrays shifted by a pivot; binary search variants use comparisons to determine which side is sorted and where the target/minimum lies.
- Duplicates break strict-order guarantees and can make comparisons ambiguous; when `nums[low] == nums[mid] == nums[high]`, shrink the window (`low += 1`, `high -= 1`) to skip duplicates.

## Search in rotated array (with duplicates) — template

```python
# Example adapted from search_in_rotated_arr_2.ipynb
nums = [7,7,7,7,7,7,7,1,2,3,4,5,7,7]
target = 1
n = len(nums)
low, high = 0, n - 1
found = False
while low <= high:
	mid = (low + high) // 2
	if nums[mid] == target:
		print("target found at index", mid)
		found = True
		break
	# handle duplicates around mid
	if nums[low] == nums[mid] and nums[high] == nums[mid]:
		low += 1
		high -= 1
		continue
	# left half is sorted
	if nums[low] <= nums[mid]:
		if nums[low] <= target < nums[mid]:
			high = mid - 1
		else:
			low = mid + 1
	else:
		# right half is sorted
		if nums[mid] < target <= nums[high]:
			low = mid + 1
		else:
			high = mid - 1
if not found:
	print("target not found")
```

Notes:
- Worst-case time is O(n) when many duplicates force repeated shrinking. Average-case O(log n).

## Find minimum in rotated sorted array — templates

Brute force (O(n)):

```python
nums = [4,5,6,7,0,1,2]
mini = float('inf')
for x in nums:
	mini = min(mini, x)
print(mini)
```

Binary-search optimized (average O(log n)):

```python
nums = [4,5,6,7,0,1,2]
n = len(nums)
low, high = 0, n - 1
mini = float('inf')
while low <= high:
	mid = low + (high - low) // 2
	if nums[mid] <= nums[high]:
		mini = min(mini, nums[mid])
		high = mid - 1
	else:
		mini = min(mini, nums[low])
		low = mid + 1
print(mini)
```

Notes:
- Compare `nums[mid]` with `nums[high]` (or `nums[low]`) to decide which side contains the minimum.

## Complexity
- `search_in_rotated_arr_2`: Best/average O(log n), worst-case O(n) when duplicates cause linear behavior; Space O(1).
- `min_in_sorted_array` (binary-search): Average O(log n), Space O(1).

## Common pitfalls
- Forgetting to handle the `nums[low] == nums[mid] == nums[high]` case leads to incorrect branching with duplicates.
- Off-by-one errors when updating `low`/`high` in inclusive `while low <= high` loops.

## Examples
- `search_in_rotated_arr_2` sample: `nums = [7,7,7,7,7,7,7,1,2,3,4,5,7,7]`, `target = 1` -> found at index 7.
- `min_in_sorted_array` sample: `nums = [4,5,6,7,0,1,2]` -> returns `0`.

---
See the notebooks for runnable cells and step-through demonstration.
