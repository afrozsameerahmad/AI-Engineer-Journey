(# Day 28 Notes:\n)

## 1) 4-Sum

### Problem
Given an integer array `nums` and an integer `target`, return all unique quadruplets `[a,b,c,d]` such that `a + b + c + d == target`.

Notebook example:
- `nums = [1,0,-1,0,-2,2]`, `target = 0`
- Output: `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

### Approach A: Brute Force
Check every quadruple `(i,j,k,l)` with `i<j<k<l` and collect quadruplets summing to `target`, then deduplicate (e.g., using set of tuples).

```python
nums = [1,0,-1,0,-2,2]
target = 0
n = len(nums)
res = set()
for i in range(n):
	for j in range(i+1, n):
		for k in range(j+1, n):
			for l in range(k+1, n):
				if nums[i] + nums[j] + nums[k] + nums[l] == target:
					quad = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
					res.add(quad)
print([list(t) for t in res])
```

Complexity:
- Time: O(n^4)
- Space: O(m) for storing unique quadruplets

### Approach B: Sort + Two Pointers (reduce to 2-sum) — Common optimal approach
Sort the array, fix two indices `i` and `j`, then use two pointers `l` and `r` to find pairs where `nums[i] + nums[j] + nums[l] + nums[r] == target`. Skip duplicates at each fixed position.

```python
def four_sum(nums, target):
	nums.sort()
	n = len(nums)
	res = []
	for i in range(n-3):
		if i > 0 and nums[i] == nums[i-1]:
			continue
		for j in range(i+1, n-2):
			if j > i+1 and nums[j] == nums[j-1]:
				continue
			l, r = j+1, n-1
			while l < r:
				s = nums[i] + nums[j] + nums[l] + nums[r]
				if s == target:
					res.append([nums[i], nums[j], nums[l], nums[r]])
					l += 1
					r -= 1
					while l < r and nums[l] == nums[l-1]:
						l += 1
					while l < r and nums[r] == nums[r+1]:
						r -= 1
				elif s < target:
					l += 1
				else:
					r -= 1
	return res

print(four_sum([1,0,-1,0,-2,2], 0))
```

Complexity:
- Time: O(n^3) after sorting (for 4-sum)
- Space: O(1) extra (output excluded)

### Approach C: k-Sum Generalization (recursive)
Write a recursive `k_sum` that reduces k-sum to (k-1)-sum until `k==2` where you apply two-sum with two pointers. This is cleaner for reuse (3-sum, 4-sum, etc.).

```python
def k_sum(nums, target, k):
	res = []
	if not nums:
		return res
	if k == 2:
		l, r = 0, len(nums)-1
		while l < r:
			s = nums[l] + nums[r]
			if s == target:
				res.append([nums[l], nums[r]])
				l += 1; r -= 1
				while l < r and nums[l] == nums[l-1]:
					l += 1
				while l < r and nums[r] == nums[r+1]:
					r -= 1
			elif s < target:
				l += 1
			else:
				r -= 1
		return res

	for i in range(len(nums)):
		if i == 0 or nums[i] != nums[i-1]:
			for subset in k_sum(nums[i+1:], target-nums[i], k-1):
				res.append([nums[i]] + subset)
	return res

def four_sum_recursive(nums, target):
	nums.sort()
	return k_sum(nums, target, 4)

print(four_sum_recursive([1,0,-1,0,-2,2], 0))
```

Complexity:
- Time: O(n^{k-1}) for k-sum (so O(n^3) for 4-sum) after sorting

---

## Practical Takeaways
1. Sort + two-pointer with careful duplicate skipping brings 4-sum down from O(n^4) to O(n^3).
2. The recursive k-sum implementation provides a neat, reusable pattern for 2/3/4-sum problems.
3. Always handle duplicates at each fixed level (`i`, `j`, etc.) to avoid repeated results.
4. Test edge cases: small arrays, many duplicates, and arrays where `n < k`.
5. For interview answers, state both brute-force and optimized approaches, with time/space complexity.

