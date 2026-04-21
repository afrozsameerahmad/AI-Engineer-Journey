# Day 28: LeetCode Question Practice

## Overview
This day focuses on the 4-Sum problem (finding unique quadruplets that sum to a given target) and explores multiple solution patterns:

- Brute-force enumeration (clear but inefficient)
- Sort + two-pointer reduction (fix two indices, two-pointer for the remaining pair)
- Generalized `k-sum` recursive approach that reduces to `2-sum` for reusability

The practice notebook demonstrates these approaches, discusses duplicate handling, and compares time/space tradeoffs.

## Notebook Files
- `4_sum_problem.ipynb`: Brute-force and optimized sort+two-pointer approaches, plus a k-sum generalization.

**Notebook implementation note (4-Sum):**
- The optimized approach sorts the array and fixes two indices before applying two pointers; ensure duplicate skipping at each fixed level (`i`, `j`) to avoid repeated quadruplets.

## What Was Practiced
- Designing an efficient reduction from combinatorial brute-force to two-pointer techniques.
- Implementing duplicate skipping correctly at multiple levels.
- Generalizing `k-sum` solutions to reuse the same idea for 2/3/4-sum problems.
- Edge-case testing: small arrays, lots of duplicates, and cases where `n < 4`.

## Complexity Snapshot

| Problem | Approach | Time | Space |
|---|---|---:|---:|
| 4-Sum | Brute force (all quadruples) | O(n^4) | O(m) |
| 4-Sum | Sort + two pointers (fix 2) | O(n^3) | O(1) |
| 4-Sum | k-sum (generalized) | O(n^{k-1}) | O(1) |

## Key Patterns Practiced
1. Reduce a k-sum to repeated two-sum applications using sorting and recursion.
2. Skip duplicates at every fixed-position level to produce unique results.
3. Evaluate in-place and extra-space options and choose based on constraints.

## Difficulty Level
Medium (classic interview problem requiring careful duplicate handling and a good reduction strategy).

---
See `notes.md` for detailed explanations, code examples, and practical takeaways.

