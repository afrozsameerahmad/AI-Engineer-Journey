(The file `c:\Users\samee\AI_Engineer_Journey\Phase-02-Python-DSA\Day-27-20-Apr-2026-Question_practice_Leetcode\README.md` exists, but is empty)
# Day 27: LeetCode Question Practice

## Overview
This day focuses on two fundamental array/matrix interview problems practiced in notebooks:

- 3-Sum (find unique triplets summing to zero)
- Rotate Matrix 90° (in-place matrix rotation)

The practice follows the pattern used earlier: present a brute-force or straightforward method, then work to an optimal/commonly accepted approach and discuss complexity.

## Notebook Files
- `3_sum_problem.ipynb`: Brute-force and sort+two-pointer approaches for 3-sum, with duplicate handling.
- `rotate_matrix_90_deg.ipynb`: Extra-matrix mapping and in-place transpose+reverse methods for rotating an n x n matrix.

**Notebook implementation note (3-Sum):**
- The notebook contains an inline two-pointer snippet that assumes the input array is sorted and `n` has been (re)computed. If you run the inline cell directly, make sure to call `arr.sort()` and `n = len(arr)` before the two-pointer loop to ensure correct results and proper duplicate handling.

## What Was Practiced
- Sorting + two-pointer technique for reducing combinatorial checks.
- Duplicate skipping and result deduplication strategies.
- Coordinate mapping for matrix transforms and in-place matrix operations (transpose + reverse).
- Time vs space tradeoffs for array and matrix manipulations.

## Complexity Snapshot

| Problem | Approach | Time | Space |
|---|---|---:|---:|
| 3-Sum | Brute force (all triples) | O(n^3) | O(m) |
| 3-Sum | Sort + two pointers | O(n^2) | O(1) |
| Rotate Matrix | Extra matrix mapping | O(n^2) | O(n^2) |
| Rotate Matrix | In-place transpose + reverse | O(n^2) | O(1) |

## Key Patterns Practiced
1. Fix-one + two-pointer to cut one dimension in combinatorial problems.
2. Careful duplicate handling after sorting to avoid repeated results.
3. Use geometric/coordinate transforms (transpose + reflect) for in-place matrix rotation.

## Difficulty Level
Medium (common interview-level problems requiring careful edge-case handling).

---
See `notes.md` for detailed explanations, code examples, and practical takeaways.
