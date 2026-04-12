Day 21: Array Question Practice

## Check if Array Is Sorted
Problem practiced: determine whether an array is sorted in non-decreasing order.

### Approach Used
The notebook uses a single loop and compares adjacent elements:
1. Traverse from index `0` to `n-2`
2. If `nums[i] > nums[i+1]`, stop immediately and print "Array is not sorted"
3. If loop completes without break, print "Array is sorted"

This is an early-exit pattern, so it can finish quickly when disorder is found early.

- Time Complexity: $O(n)$
- Space Complexity: $O(1)$

## Find Second Largest Element
Problem practiced: return the second largest distinct element from an array.

### Approach 1: Sort and Pick
1. Sort the array
2. Return `nums[-2]`

- Time Complexity: $O(n \log n)$
- Space Complexity: depends on Python sort internals (conceptually in-place usage)

### Approach 2: One-Pass Tracking (Better)
Track two values while scanning once:
- `largest`
- `second_largest`

For each number:
1. If current number is greater than `largest`, shift `largest` to `second_largest`
2. Else if it is greater than `second_largest` and not equal to `largest`, update `second_largest`

This gives linear-time performance and handles duplicate-largest values correctly.

- Time Complexity: $O(n)$
- Space Complexity: $O(1)$

## Remove Duplicates from Array
Problem practiced: remove duplicates and keep unique values.

### Approach Used in Notebook
The solution builds a dictionary (`freq_map`) using array values as keys:
1. Insert each element as a key in dictionary
2. Iterate dictionary keys and write them back into the original list from index `0`
3. Print `nums[:j]` where `j` is number of unique elements

Because dictionary keys are unique, duplicates are removed. In modern Python, insertion order of keys is preserved, so first occurrence order is kept.

Note: The title says "sorted array", but this specific implementation works as a general "unique values with preserved first-seen order" approach.

- Time Complexity: $O(n)$ average
- Space Complexity: $O(n)$

## Right Rotate Array
Problem practiced: rotate an array to the right.

### Case 1: Right Rotate by 1 Step
1. Save last element in `temp`
2. Shift all elements one position right (from end to start)
3. Put `temp` at index `0`

- Time Complexity: $O(n)$
- Space Complexity: $O(1)$

### Case 2: Right Rotate by `k` Steps
Notebook implementation:
1. Normalize `k` using `k = k % len(nums)`
2. Store last `k` elements in `temp = nums[-k:]`
3. Shift remaining elements right by `k`
4. Place `temp` at the front using slice assignment `nums[:k] = temp`

This is efficient and avoids repeated one-step rotations.

- Time Complexity: $O(n)$
- Space Complexity: $O(k)$

## Key Takeaways
- Adjacent comparison is enough to check sorted order in linear time.
- For second largest, one-pass scanning is better than sorting when only one statistic is needed.
- Dictionaries are useful for deduplication with order retention.
- Always normalize rotation steps with modulo: `k % n`.
- Slice operations can make array rotation code clean and readable.
