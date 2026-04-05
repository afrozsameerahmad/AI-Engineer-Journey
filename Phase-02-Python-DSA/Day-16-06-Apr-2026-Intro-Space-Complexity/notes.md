# Day 16 Notes: Introduction to Space Complexity

## 1) What Is Space Complexity
- Space complexity describes how the amount of memory grows as input size grows.
- It helps compare algorithm memory efficiency independent of machine.

Core idea:
- We focus on memory growth trend, not exact bytes consumed.

---

## 2) Why It Matters in DSA
- Not all systems have unlimited memory availability.
- A space-efficient algorithm is better for resource-constrained systems.

Example thinking:
- An algorithm with O(1) space is usually better than one with O(n) space when both have same time complexity.

## 3) Input Space vs Auxiliary Space
- Input space: Memory required to store the input data.
- Auxiliary space: Extra/temporary memory used during algorithm execution.

Examples:
```
x = 10      # Input space
y = 5       # Input space
total = x + y + z   # Auxiliary space: O(1)
```

Total space complexity = Input space + Auxiliary space

## 4) Big-O Space Notation
- Uses same Big-O notation as time complexity.
- Describes worst-case memory growth behavior.

Common forms:
- `O(1)` constant space (fixed variables only)
- `O(log n)` logarithmic (recursion depth)
- `O(n)` linear (array/list storage)
- `O(n²)` quadratic (2D structures)
- `O(2^n)` exponential (exponential recursion)

## 5) Space Complexity of Common Operations
- Single variable: `O(1)`
- Array of size n: `O(n)`
- 2D matrix n×n: `O(n²)`
- Hash table with n items: `O(n)`
- Recursion depth: `O(recursion_depth)`

Practical insight:
- Digit operations (like Armstrong, palindrome) typically use `O(1)` space.

## 6) TLE (Time Limit Error)
- Error when code takes longer than expected to execute.
- Related to both time complexity and space complexity efficiency.

Cause:
- Inefficient algorithms or unnecessary operations
- Poor space usage leading to memory swaps

## 7) Digit-Based Algorithm Patterns
- Extract digit: Use modulo `% 10`
- Remove digit: Use integer division `// 10`
- Process digits: Use while loop until number becomes 0

Pattern template:
```python
n = some_number
while n > 0:
    digit = n % 10      # Extract last digit
    # Process digit
    n //= 10            # Remove last digit
```

Time complexity: `O(log n)` (loop runs for number of digits)
Space complexity: `O(1)` (only fixed variables)

## 8) Armstrong Number Problem
- Definition: Number equals sum of its digits each raised to power of digit count.
- Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

Algorithm:
1. Count number of digits
2. Extract each digit using modulo
3. Raise digit to power of digit count
4. Sum all powered digits
5. Compare with original number

Time: `O(log n)` | Space: `O(1)`

## 9) Factor Finding - Optimization Insight
- Brute force: Check all numbers from 1 to n -> `O(n)`
- Optimized: Check only from 1 to √n -> `O(√n)`

Key insight:
- Factors come in pairs: if `i` divides `n`, then `n/i` also divides `n`
- Only need to check up to √n to find all factor pairs
- Example: For n=36, check 1 to 6 and automatically find pairs (1,36), (2,18), (3,12), (4,9), (6,6)

Optimization result:
- For n=10,000: Check only 1-100 instead of 1-10,000 (100x faster!)

## 10) Digit Extraction and Manipulation
- Sum of digits: Extract each digit and add to sum
- Reverse number: Build reversed number using extracted digits
- Both use same modulo/division pattern

Examples:
- 5873 -> digits 5,8,7,3 -> sum = 23
- 1234 -> reversed = 4321

Time: `O(log n)` | Space: `O(1)`

## 11) Palindrome Number Check
- Definition: Number reads same forwards and backwards
- Examples: 121 ✓, 1221 ✓, 1234 ✗

Algorithm:
1. Extract digits one by one
2. Build reversed number using modulo and multiplication
3. Compare original with reversed

Time: `O(log n)` | Space: `O(1)`

## 12) Day 16 Summary
- Space complexity measures memory usage as function of input size.
- Distinguish between input space and auxiliary space.
- Digit operations follow a predictable pattern with O(log n) time and O(1) space.
- √n optimization can dramatically improve efficiency.
- TLE errors indicate need for algorithm optimization.
- Most number problems have elegant O(1) space solutions.

## 13) Practice Checklist for Space Complexity
- Identify all variables used and count their space contribution.
- For loops and recursion, determine depth/iterations.
- Check if you can solve without extra arrays/lists.
- For digit problems, use modulo/division pattern.
- For factor problems, always check √n optimization.
- Analyze both time AND space for complete picture.
- Compare brute force with optimized approaches' space complexity.
