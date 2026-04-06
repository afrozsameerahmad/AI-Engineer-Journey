# Day 16: Intro to Space Complexity

## Overview
This day focuses on understanding how algorithm memory usage scales with input size.

- Meaning of space complexity
- Why space complexity matters in DSA
- Big-O notation for memory usage
- Common space complexity patterns
- Digit-based algorithm optimization
- TLE errors and memory efficiency

## Folder Structure
- `exercise/space.ipynb`
	- Understanding space complexity basics
	- Input space vs auxiliary space
	- Why memory efficiency matters

- `practice/`
	- `armstrong.ipynb` - Armstrong number detection
	- `extraction_of_digits.ipynb` - Extract and sum digits
	- `factors.ipynb` - Find all divisors (with optimization)
	- `palindrom.ipynb` - Check palindrome numbers
	- Real-world number problems using space-efficient solutions

- `notes.md`
	- Consolidated theory and key takeaways for revision

## Key Learning Outcomes
After completing Day 16, i should be able to:
1. Explain what space complexity means and how to measure it.
2. Use Big-O notation for analyzing memory usage of algorithms.
3. Distinguish between input space and auxiliary space.
4. Understand digit-based algorithms and their O(log n) time, O(1) space patterns.
5. Recognize √n optimization opportunities in factor/divisor problems.

## Quick Revision
- Space complexity measures growth of memory with input size.
- Big-O communicates asymptotic upper-bound memory behavior.
- Most digit operations use O(log n) time and O(1) space.
- √n optimization can reduce iterations from O(n) to O(√n).
- TLE errors happen when algorithms use time or space inefficiently.

## Suggested Practice
1. Trace through each digit algorithm and verify O(1) space claim.
2. Compare brute force and √n approach for finding factors.
3. Analyze why digit extraction always uses O(log n) time.
4. Implement the palindrome check and count memory used.
5. Test Armstrong number with different digit counts.

## Date
06-Apr-2026
