# Day 24 Notes:

## 1) Max Consecutive Ones

### Problem
Given a binary array, return the maximum number of consecutive 1s.

Example from notebook:
- `nums = [1,1,0,1,0,1,1,1,1,0,1,1]`
- Output: `4`

### Core Idea
Track current streak of 1s and best streak seen so far:
1. If current element is 1, increase `count`.
2. If current element is 0, update `max_count` and reset `count`.
3. After loop, do one final update for a streak ending at the last index.

### Notebook Implementation Summary
```python
nums=[1,1,0,1,0,1,1,1,1,0,1,1]
count=0
max_count=0
for i in range(len(nums)):
    if nums[i]==1:
        count+=1
    else:
        max_count=max(max_count,count)
        count=0
max_count=max(max_count,count)
print(max_count)
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## 2) Missing Number

### Problem
Given an array containing distinct numbers in the range `0` to `n`, find the one missing number.

Notebook example:
- `nums = [9,6,4,3,2,5,7,0,1]`
- Missing number is `8`

### Approach A In Notebook: Brute Force (`i not in nums`)
For each value from `0` to `n`, check whether it exists in array.

```python
nums=[9,6,4,3,2,5,7,0,1]
n=len(nums)
for i in range(0,n+1):
    if i not in nums:
        print(i)
```

Complexity:
- Time: O(n^2)
- Space: O(1)

### Approach B In Notebook: Dictionary Marking
Use dictionary as presence map.

```python
nums=[9,6,4,3,2,5,7,0,1]
n=len(nums)
d={}
for i in range(0,n+1):
    d[i]=0
for i in nums:
    d[i]=1
for i in d:
    if d[i]==0:
        print(i)
```

Complexity:
- Time: O(n)
- Space: O(n)

### Approach C In Notebook: Mathematical Sum Formula
Compute expected sum minus actual sum.

```python
nums=[9,6,4,3,2,5,7,0,1]
n=10
total_sum=n*(n-1)//2
actual_sum=sum(nums)
missing_num=total_sum-actual_sum
print(missing_num)
```

Complexity:
- Time: O(n)
- Space: O(1)

---

## 3) Two Sum

### Problem
Given an array and a target, return indices of two numbers such that they add up to target.

Notebook setup:
- `nums = [5,9,1,2,4,15,6,3]`
- `target = 13`

### Approach A In Notebook: Brute Force (Nested Loops)
Try every pair and print first pair whose sum equals target.

```python
nums = [5,9,1,2,4,15,6,3]
n=len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j]==13:
            print(i,j)
```

Complexity:
- Time: O(n^2)
- Space: O(1)

### Approach B In Notebook: Optimal (Hash Map / Dictionary)
Store seen values with index. For each number:
- Compute `remaining = target - nums[i]`
- If `remaining` already exists in map, answer found.
- Otherwise store current number and index.

```python
nums = [5,9,1,2,4,15,6,3]
n=len(nums)
target = 13
num_dict = {}
for i in range(0,n):
    remaining = target - nums[i]
    if remaining in num_dict:
        print(num_dict[remaining],i)
    else:
        num_dict[nums[i]]=i
```

Complexity:
- Time: O(n)
- Space: O(n)

---

## Practical Takeaways
1. Many array interview problems can be solved first with brute force and then optimized with hashing.
2. Consecutive-counting pattern is useful for binary array streak problems.
3. Presence-tracking with dictionary/set often reduces time complexity from O(n^2) to O(n).
4. Always verify edge cases:
   - empty array
   - single element
   - no valid pair (for Two Sum variants)
   - missing value at start (`0`) or end (`n`) in Missing Number
