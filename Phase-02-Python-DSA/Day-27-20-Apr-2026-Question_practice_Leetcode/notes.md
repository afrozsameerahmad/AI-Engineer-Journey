# Day 27 Notes:

## 1) 3-Sum

### Problem
Given an integer array `nums`, return all unique triplets `[a,b,c]` such that `a + b + c == 0`.

Notebook example:
- `nums = [-1,0,1,2,-1,-4]`
- Output: `[[-1,-1,2],[-1,0,1]]`

### Approach A: Brute Force
Try every triple `(i,j,k)` with `i<j<k` and collect triplets summing to zero, then deduplicate.

```python
nums = [-1,0,1,2,-1,-4]
n = len(nums)
res = set()
for i in range(n):
	for j in range(i+1, n):
		for k in range(j+1, n):
			if nums[i] + nums[j] + nums[k] == 0:
				trip = tuple(sorted([nums[i], nums[j], nums[k]]))
				res.add(trip)
print([list(t) for t in res])
```

Complexity:
- Time: O(n^3)
- Space: O(m) for storing unique triplets

### Approach B: Sort + Two Pointers (Optimal common approach)
Sort the array, fix one element `nums[i]` and use two pointers `l` and `r` to find pairs where `nums[i]+nums[l]+nums[r]==0`. Skip duplicates as you go.

```python
def three_sum(nums):
	nums.sort()
	n = len(nums)
	ans = []
	for i in range(n-2):
		if i>0 and nums[i]==nums[i-1]:
			continue
		l, r = i+1, n-1
		while l<r:
			s = nums[i] + nums[l] + nums[r]
			if s==0:
				ans.append([nums[i], nums[l], nums[r]])
				l += 1; r -= 1
				while l<r and nums[l]==nums[l-1]:
					l += 1
				while l<r and nums[r]==nums[r+1]:
					r -= 1
			elif s<0:
				l += 1
			else:
				r -= 1
	return ans

print(three_sum([-1,0,1,2,-1,-4]))
```

Complexity:
- Time: O(n^2) after sorting
- Space: O(1) extra (output excluded)

**Note about the notebook's inline implementation:**
- If you use the inline two-pointer snippet (not the `three_sum` function above), ensure the input array is sorted and `n` is recalculated before the loop. Example:

```python
arr = [-1,0,1,2,-1,-4]
arr.sort()
n = len(arr)
res = []
for i in range(n):
	if i > 0 and arr[i] == arr[i-1]:
		continue
	left, right = i+1, n-1
	# two-pointer loop...
```

This mirrors the notebook cell behavior: if `arr` isn't sorted first, the two-pointer technique will produce incorrect results or miss duplicate-handling optimizations.

---

## 2) Rotate Matrix (90° clockwise)

### Problem
Given an `n x n` matrix, rotate it 90 degrees clockwise in-place.

Notebook example:
- `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[[7,4,1],[8,5,2],[9,6,3]]`

### Approach A: Use extra matrix (simple)
Create a new matrix and map element `(i,j)` to `(j, n-1-i)`.

```python
def rotate_extra(matrix):
	n = len(matrix)
	res = [[0]*n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			res[j][n-1-i] = matrix[i][j]
	return res

print(rotate_extra([[1,2,3],[4,5,6],[7,8,9]]))
```

Complexity:
- Time: O(n^2)
- Space: O(n^2)

### Approach B: In-place — Transpose then Reverse Rows (Optimal)
Transpose the matrix (swap `matrix[i][j]` with `matrix[j][i]`) then reverse each row to achieve the rotation in-place.

```python
def rotate_inplace(matrix):
	n = len(matrix)
	# transpose
	for i in range(n):
		for j in range(i+1, n):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	# reverse each row
	for i in range(n):
		matrix[i].reverse()

m = [[1,2,3],[4,5,6],[7,8,9]]
rotate_inplace(m)
print(m)
```

Complexity:
- Time: O(n^2)
- Space: O(1) extra

---

## Practical Takeaways
1. Sorting + two-pointer reduces 3-sum from O(n^3) to O(n^2); watch duplicates carefully.
2. For matrix transforms, think in terms of coordinate mapping or algebraic transforms (transpose + reflect).
3. Always reason about in-place vs extra-space tradeoffs for matrices.
4. Test edge cases: empty arrays, arrays with many duplicates, 1x1 or 2x2 matrices.
5. When writing interview solutions, state the complexity and mention duplicate-handling explicitly.

