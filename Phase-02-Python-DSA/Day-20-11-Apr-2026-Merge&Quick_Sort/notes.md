Day 20: Merge Sort and Quick Sort

## Merge Sort
Merge Sort is a divide-and-conquer algorithm.
It keeps splitting the list into halves until sublists of size 1 remain, then merges those sublists back in sorted order.

### Core Steps
1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the two sorted halves.

### Merge Helper Idea
The `merge(left, right)` helper compares the current element of both lists and appends the smaller one to a new list. After one side is exhausted, it appends the remaining elements from the other side.

- Time Complexity: $O(n \log n)$
- Space Complexity: $O(n)$
- Stable: Yes

## Quick Sort
Quick Sort also uses divide-and-conquer, but around a pivot element.
Elements smaller than the pivot go left, and greater (or equal) go right. Then both sides are sorted recursively.

### Version 1: Simple Recursive (Creates New Lists)
In the notebook, one implementation uses:
- Pivot = last element
- `left = [x for x in arr[:-1] if x < pivot]`
- `right = [x for x in arr[:-1] if x >= pivot]`

This is clean and easy to understand, but uses extra memory for `left` and `right`.

- Average Time Complexity: $O(n \log n)$
- Worst Time Complexity: $O(n^2)$ (bad pivot choices repeatedly)
- Extra Space (this version): around $O(n)$ plus recursion stack

### Version 2: In-Place Quick Sort with Partition
The second implementation uses:
- `partition(nums, low, high)`
- Pivot = `nums[high]`
- Pointer `i` tracks the boundary for elements smaller than pivot
- Final swap places pivot at its correct index

Then recursion happens on left and right partitions:
- `quick_sort(nums, low, pivot_index - 1)`
- `quick_sort(nums, pivot_index + 1, high)`

This version avoids creating new sublists and is closer to interview-style quick sort.

- Average Time Complexity: $O(n \log n)$
- Worst Time Complexity: $O(n^2)$
- Space Complexity: $O(\log n)$ average recursion stack, $O(n)$ worst stack depth

## Largest Element in an Array
Also practiced a basic linear scan problem:

1. Assume first element is largest.
2. Traverse all elements.
3. Update `largest` whenever a bigger value is found.

- Time Complexity: $O(n)$
- Space Complexity: $O(1)$

## Key Takeaways
- Merge Sort gives guaranteed $O(n \log n)$ time but uses extra memory.
- Quick Sort is usually fast in practice and can be in-place, but worst-case is $O(n^2)$.
- Pivot choice strongly affects Quick Sort performance.
- Keep practicing both conceptual and in-place implementations.
