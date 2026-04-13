# Day 22: Array Practice - Sorted Check & Remove Duplicates

## Problem 1: Check if Array is Sorted

This is a warm-up problem to check if an array is sorted in ascending order.

### Approach
1. Iterate through the array from index 0 to n-2.
2. Compare each element with the next element.
3. If any element is greater than the next element, the array is not sorted.
4. If the loop completes without finding such a pair, the array is sorted.

### Code Example
```python
nums = [3,5,6,7,8,9,12,15,18,21,24,27,30]
n = len(nums)
is_sorted = True
for i in range(0, n-1):
    if nums[i] > nums[i+1]:
        is_sorted = False
        break
if is_sorted:
    print("sorted")
else:
    print("not sorted")
```

### Complexity Analysis
- **Time Complexity**: $O(n)$ — We iterate through the array once. In the best case (array is not sorted from the beginning), we may break early, but worst case is still $O(n)$.
- **Space Complexity**: $O(1)$ — We only use a constant amount of extra space for the `is_sorted` boolean variable.

### Key Points
- Simple linear scan approach
- Break early if we find a violation of sorted order (optimization)
- Works for both ascending and descending checks (just swap the comparison operator)

---

## Problem 2: Remove Duplicates from Sorted Array (In-Place)

This is a classic two-pointer technique problem where we must remove duplicates in-place and return the count of unique elements.

### Constraint
- The array is **already sorted**
- We must modify the array **in-place** (no extra array allowed for the main logic)
- Return the count of unique elements

### Approach 1: Brute Force (Extra Space)
Create a new list with unique elements.

```python
nums = [1,2,3,4,5,7,9,11,11,12,34,34,56,56,56]
unique = [nums[0]]

for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        unique.append(nums[i])

print(len(unique))  # Output: 11
```

#### Complexity
- **Time Complexity**: $O(n)$ — Single pass through the array
- **Space Complexity**: $O(n)$ — We store unique elements in a new list

### Approach 2: Optimal Solution (Two-Pointer, In-Place)
Use two pointers:
- Pointer `i`: tracks the position where the next unique element should go
- Pointer `j`: scans through the array to find unique elements

```python
nums = [1,1,1,2,3,4,4,7,9,9,9,10]
n = len(nums)
if n == 1:
    print(1)

i = 0
j = i + 1
while j < n:
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]
    j += 1

print(i + 1)  # Output: count of unique elements
```

#### How It Works
1. Start with `i = 0` (first element is always unique)
2. `j` scans from index 1 onwards
3. When `nums[j]` is different from `nums[i]`, we've found a new unique element:
   - Increment `i`
   - Place `nums[j]` at position `i`
4. Always increment `j`
5. The count of unique elements is `i + 1`

#### Example Trace
```
Array: [1,1,1,2,3,4,4,7,9,9,9,10]

Step 1: i=0, j=1
   nums[1]=1 == nums[0]=1, so j++

Step 2: i=0, j=2
   nums[2]=1 == nums[0]=1, so j++

Step 3: i=0, j=3
   nums[3]=2 != nums[0]=1, so i++, nums[1]=2, j++
   Array becomes: [1,2,1,2,3,4,4,7,9,9,9,10]

Step 4: i=1, j=4
   nums[4]=3 != nums[1]=2, so i++, nums[2]=3, j++
   Array becomes: [1,2,3,2,3,4,4,7,9,9,9,10]

... continue until j reaches end

Final: i=7, so count = i+1 = 8 unique elements
First 8 elements are: [1,2,3,4,7,9,10, ...]
```

#### Complexity
- **Time Complexity**: $O(n)$ — Single pass with two pointers
- **Space Complexity**: $O(1)$ — Only two pointers, no extra data structure

### Why Two-Pointer Works
Because the array is **sorted**:
- All duplicates are consecutive
- When we find a new unique value (different from the previous), we can safely place it at position `i+1`

If the array was not sorted, this wouldn't work; we'd need a hash set approach.

---

## Key Takeaways

1. **Sorted Check**: Simple linear scan, useful warm-up for more complex array problems
2. **Remove Duplicates In-Place**: Classic two-pointer technique
   - Only works because input is sorted
   - Modifies the array in-place (front portion contains unique elements)
   - Much more efficient than brute force
3. **Two-Pointer Pattern**: Remember this pattern; it's useful for many array problems:
   - Partition problems
   - Container with most water
   - Trapping rain water
   - Three-sum problems

---

## Practice Notes
- Try implement the solutions without looking at notes first
- Understand why two-pointer works (sorted property is key)
- Try removing duplicates from an **unsorted** array using a hash set
- Consider edge cases: empty array, single element, all duplicates
