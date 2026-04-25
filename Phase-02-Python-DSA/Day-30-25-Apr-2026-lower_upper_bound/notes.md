# Day 30 Notes — lower_bound & upper_bound

# Day 30 Notes — lower_bound & upper_bound

## Definitions
## Definitions
- `lower_bound(arr, target)`: first index `i` such that `arr[i] >= target`. If none, returns `len(arr)` (insertion point at end).
- `upper_bound(arr, target)`: first index `i` such that `arr[i] > target`. If none, returns `len(arr)`.

These correspond to `bisect_left` and `bisect_right` in Python's `bisect` module respectively.

## Index-based templates (Python)

```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

Notes:
- Use `hi = len(arr)` (half-open interval) to make insertion-point semantics natural.
- Midpoint `lo + (hi-lo)//2` avoids overflow (not critical in Python but a good habit).

## Notebook-style (inclusive `low..high`) implementations — from Day 30 notebooks

The Day 30 notebooks use the inclusive-index pattern (`low = 0`, `high = n-1`, `while low <= high`) and sample array `nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]` with `target = 7`.

```python
# lower_bound inclusive-style (matches lower_bound.ipynb)
nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
n = len(nums)
lb = -1
low = 0
high = n - 1
target = 7
while low <= high:
    mid = low + (high - low) // 2
    if nums[mid] >= target:
        lb = mid
        high = mid - 1
    else:
        low = mid + 1
print(lb)

# upper_bound inclusive-style (matches upper_bound.ipynb)
ub = n
low = 0
high = n - 1
while low <= high:
    mid = low + (high - low) // 2
    if nums[mid] > target:
        ub = mid
        high = mid - 1
    else:
        low = mid + 1
print(ub)
```

Notes on notebook variants:
- `lower_bound` notebook initializes `lb = -1` and prints `-1` if not found; `upper_bound` initializes `ub = n` as an insertion-point sentinel.
- These inclusive implementations return sentinel values (`-1` or `n`) when no qualifying index exists; adapt callers accordingly.

## Predicate-based pattern

Binary search can be expressed as "find first index where predicate(i) is True". Example predicate for `lower_bound`:

- predicate(i): `arr[i] >= target`
- Search domain: `i in [0, len(arr))`, answer in `[0, len(arr)]` using half-open logic.

This pattern generalizes to many decision problems (e.g., minimum feasible value).

## Using Python's `bisect`

```python
import bisect
# bisect_left == lower_bound, bisect_right == upper_bound
i = bisect.bisect_left(arr, target)
j = bisect.bisect_right(arr, target)
occurrences = j - i
```

## Common Uses
- Count occurrences of `target`: `upper_bound - lower_bound`.
- First/last occurrence of a value (check bounds and equality after lower_bound).
- Insertion index for maintaining sorted order.

## Examples

Given `arr = [1,2,2,2,3,5]` and `target = 2`:
- `lower_bound(arr,2)` -> 1
- `upper_bound(arr,2)` -> 4
- occurrences -> `4 - 1 = 3`

Given `arr = [1,3,5]` and `target = 4`:
- `lower_bound(arr,4)` -> 2 (insertion point)
- `upper_bound(arr,4)` -> 2

Edge results:
- If result == `len(arr)`, target is greater than all elements (insertion at end).
- If result == 0 and `arr[0] >= target`, insertion at start.

## Common Pitfalls
- Mixing inclusive/exclusive bounds causes off-by-one errors.
- Using `hi = len(arr)-1` with `while lo <= hi` gives index-finding (must adjust return semantics).
- Forgetting to check equality after `lower_bound` when searching for existence.

## Complexity
- Time: O(log n) per query
- Space: O(1)

---
See `README.md` for the day's overview and `lower_upper_bound/lower_upper.py` for implementations used in practice notebooks.
