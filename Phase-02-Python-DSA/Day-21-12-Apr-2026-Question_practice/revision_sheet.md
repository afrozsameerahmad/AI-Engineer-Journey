# Day 21 Quick Revision Sheet (Arrays)

## 1-Minute Pattern Map
- Sorted Check: adjacent comparison (`nums[i] <= nums[i+1]` for all `i`)
- Second Largest: maintain two trackers (`largest`, `second_largest`)
- Remove Duplicates: use hash/dictionary for uniqueness
- Right Rotation: use modulo + shifting/slicing

## Must-Remember Complexity
- Sorted Check: Time $O(n)$, Space $O(1)$
- Second Largest (sort): Time $O(n \log n)$
- Second Largest (one pass): Time $O(n)$, Space $O(1)$
- Remove Duplicates (dict-based): Time $O(n)$ average, Space $O(n)$
- Right Rotate by `k`: Time $O(n)$, Space $O(k)$

## Core Interview Templates

### Check if Array Is Sorted
```python
is_sorted = True
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break
```

### Second Largest (Distinct) in One Pass
```python
largest = float('-inf')
second_largest = float('-inf')

for x in nums:
    if x > largest:
        second_largest = largest
        largest = x
    elif x > second_largest and x != largest:
        second_largest = x
```

### Remove Duplicates (Order Preserved)
```python
seen = {}
for x in nums:
    seen[x] = 1

unique = list(seen.keys())
```

### Right Rotate by k
```python
k = k % len(nums)
temp = nums[-k:]
for i in range(len(nums) - 1, k - 1, -1):
    nums[i] = nums[i - k]
nums[:k] = temp
```

## Top Edge Cases to Mention
- Empty array
- Single element array
- All elements same (second largest may not exist)
- `k = 0`, `k > n`, and very large `k`
- Negative numbers and mixed values

## Fast Interview Answers
1. Why use `k % n` in rotation?
It converts large rotations into equivalent minimal rotations.

2. Why is one-pass second largest better than sorting?
Sorting solves more than needed; one-pass gives answer in linear time.

3. Why dictionary/set for duplicates?
Membership and uniqueness handling are average $O(1)$ per operation.

4. Is your dedup logic stable in order?
Yes, dictionary insertion order is preserved in modern Python.

## Quick Self-Test
- Can I explain sorted-check early exit in one sentence?
- Can I derive one-pass second largest without seeing code?
- Can I rotate array by `k` on paper for 6 elements?
- Can I state both time and space complexity confidently?
