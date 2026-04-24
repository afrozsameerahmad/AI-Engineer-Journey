# Day 29 Notes:

## 1) Practice Focus

This day focused on core search patterns and common LeetCode practice problems implemented in the `practice/` notebooks and the `binary_search` notebook:
- Binary Search (iterative & recursive)
- Binary-search variants (lower/upper bound ideas)
 - Binary Search (iterative & recursive)
 - Binary search variants (lower/upper bound ideas)
- Two-pointer patterns
- Sliding-window and frequency/hashmap approaches
- Typical problem hygiene: edge cases, duplicates, and complexity reasoning

See the `practice/` notebooks for worked examples (1st.ipynb – 4th.ipynb) and `binary_search/binary_search.ipynb` for binary search basics.

---

## 2) Binary Search — core idea

### Problem
Given a sorted array `nums` and `target`, return index of `target` or `-1` if not found.

### Iterative approach (common template)

```python
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

Time: O(log n), Space: O(1)

### Recursive approach

```python
def binary_search_rec(nums, target, low, high):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search_rec(nums, target, mid + 1, high)
    return binary_search_rec(nums, target, low, mid - 1)

# call: binary_search_rec(nums, target, 0, len(nums)-1)
```

Space: O(log n) due to recursion stack (worst case), Time: O(log n)

---

## 3) Common variations and usage patterns

- Search insert position / lower-bound / upper-bound: adapt comparisons and return `low`/`high` correctly.
- First-bad-version style problems: binary search on predicate (bool) rather than direct equality.
- Find peak / rotated-array search: combine binary-search ideas with problem-specific checks.

Example lower-bound template:

```python
def lower_bound(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low
```

---

## 4) Patterns seen in `practice/` notebooks

- Two pointers: sorted-array pair-sum, partitioning, and window expansion/contraction.
- Sliding window: dynamic windows for substring/array sum problems.
- Hash maps/frequency arrays: counting and index lookups (O(1) expected) for complement-based problems.
- Sorting + two-pointer: reduce n^2 problems using ordering and pointer movement.

---

## 5) Practical takeaways

1. Use the iterative binary-search template for most index-finding tasks; switch to predicate-based binary search for decision problems.
2. Always test edge cases: empty array, single element, duplicates, and extremes (all equal elements).
3. When implementing lower/upper bounds, prefer the `low < high` half-open interval pattern to avoid off-by-one bugs.
4. Combine binary search with problem-specific checks (e.g., rotated arrays or predicate functions) for non-trivial variants.
5. Write quick asserts for small examples to validate templates before using them in larger solutions.

---

## 6) Complexity snapshot

| Problem | Approach | Time | Space |
|---|---|---:|---:|
| Binary Search | Iterative | O(log n) | O(1) |
| Binary Search | Recursive | O(log n) | O(log n) stack |

---

## 7) Next steps / practice suggestions

- Convert binary-search templates into reusable utilities (`lower_bound`, `upper_bound`, `predicate_search`).
- Apply these templates to common LeetCode problems: `search_insert`, `first_bad_version`, `find_peak_element`, rotated `search`.
- Continue solving problems in `practice/` notebooks and record micro-notes per problem (approach, pitfalls, complexity).

End of Day 29 notes.
