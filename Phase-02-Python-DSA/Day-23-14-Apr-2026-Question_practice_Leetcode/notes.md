# Day 23 Notes:  

## 1) Linear Search

### Problem
Given an unsorted array and a target value, return the index of target if found, otherwise return -1.

### Core Idea
Check each element one by one until:
- target is found, or
- array ends

### Notebook Implementation Summary
```python
nums = [1, 0, 2, 4, 3, 0, 0, 5, 1]
target = 5

ans = -1
for i in range(len(nums)):
    if nums[i] == target:
        ans = i
        break

print(ans)
```

### Observation From Notebook
The current code prints match index and then prints -1 unconditionally. This means output can contain both values when target exists.

### Complexity
- Time: O(n)
- Space: O(1)

---

## 2) Move Zeroes To End

### Problem
Move all zeroes to the end while maintaining the relative order of non-zero elements.

## Approach A In Notebook: Brute Force (Extra Array)
1. Collect all non-zero elements in a temp array.
2. Copy temp values back to start of original array.
3. Fill the remaining positions with 0.

```python
nums = [1, 0, 2, 4, 3, 0, 0, 5, 1]
n = len(nums)

temp = []
for x in nums:
    if x != 0:
        temp.append(x)

for i in range(len(temp)):
    nums[i] = temp[i]

for i in range(len(temp), n):
    nums[i] = 0

print(nums)
```

Complexity:
- Time: O(n)
- Space: O(n)

## Approach B In Notebook: Optimized (Two Pointers, In-Place)
### Notebook Logic
- Find first zero index `i`
- Use `j` to scan ahead
- Whenever `nums[j] != 0`, swap with `nums[i]`, then increment `i`

```python
nums = [1, 0, 2, 4, 3, 0, 0, 5, 1]

i = 0
while i < len(nums) and nums[i] != 0:
    i += 1

j = i + 1
while j < len(nums):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    j += 1

print(nums)
```

Complexity:
- Time: O(n)
- Space: O(1)

---

## 3) Merge Two Sorted Arrays (Unique Elements)

### Problem
Given two sorted arrays, merge them into one sorted result without duplicates.

### Notebook Logic
- Pointer `i` for first array, `j` for second array
- Push smaller element to result
- Before appending, avoid duplicate by checking last inserted value
- Finish remaining elements from either array

```python
nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 2, 3, 6, 7, 8, 9, 10]

i, j = 0, 0
n, m = len(nums1), len(nums2)
result = []

while i < n and j < m:
    if nums1[i] <= nums2[j]:
        if not result or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    else:
        if not result or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

while i < n:
    if not result or result[-1] != nums1[i]:
        result.append(nums1[i])
    i += 1

while j < m:
    if not result or result[-1] != nums2[j]:
        result.append(nums2[j])
    j += 1

print(result)
```

### Complexity (Notebook)
- Time: O(n + m)
- Space: O(n + m) for output array

---

## Practical Takeaways
1. Start with brute force, then write optimized version in the same notebook.
2. Two-pointer pattern appears in both move-zeroes and merge problems.
3. Sorted input allows linear-time merge traversal.
4. Test edge cases for all three implementations:
   - empty input
   - single element
   - all zeroes
   - all duplicates
   - target not found

