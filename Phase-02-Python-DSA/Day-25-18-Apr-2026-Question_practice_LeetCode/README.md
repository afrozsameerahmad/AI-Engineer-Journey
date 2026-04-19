# Day 25: LeetCode Question Practice

## Overview
This day focuses on three classic array interview problems practiced in notebooks:

- Best Time to Buy and Sell Stock
- Maximum Subarray
- Rearrange Array Elements by Sign

The practice follows a strong pattern: start with a straightforward/brute-force method, then improve to a more optimal approach.

## Notebook Files
- `buy_sell_stock.ipynb`: Brute force and one-pass minimum-price approach for maximum stock profit.
- `max_sub_arr.ipynb`: Brute force subarray summation and Kadane's algorithm.
- `rearrange_arr.ipynb`: Positive/negative separation method and indexed placement method.

## What Was Practiced
- Brute-force pair checking vs one-pass optimization
- Running sum and best-so-far tracking
- Kadane's algorithm for maximum subarray
- Sign-based indexing patterns for array rearrangement
- Time and space complexity comparison across approaches

## Complexity Snapshot

| Problem | Approach | Time | Space |
|---|---|---|---|
| Buy and Sell Stock | Brute force (all buy/sell pairs) | O(n^2) | O(1) |
| Buy and Sell Stock | One pass (track minimum price) | O(n) | O(1) |
| Maximum Subarray | Brute force (all subarrays) | O(n^2) | O(1) |
| Maximum Subarray | Kadane's Algorithm | O(n) | O(1) |
| Rearrange by Sign | Split positives/negatives + refill | O(n) | O(n) |
| Rearrange by Sign | Direct indexed placement | O(n) | O(n) |

## Key Patterns Practiced
1. Min/Max tracking in a single traversal
2. Prefix-like running total updates
3. Reset-on-negative strategy (Kadane)
4. Deterministic placement using even/odd indices
5. Refactoring from brute-force to optimal solution

## Difficulty Level
Easy to Medium interview-level array problems.

---
See `notes.md` for detailed per-problem explanations and notebook-level breakdowns.
