# Day 25 Notes:

## 1) Best Time to Buy and Sell Stock

### Problem
Given stock prices where `prices[i]` is the price on day `i`, find the maximum profit possible by buying once and selling once later.

Notebook example:
- `prices = [7,2,5,1,6,4,8]`
- Output: `7` (buy at `1`, sell at `8`)

### Approach A In Notebook: Brute Force
Try every buy day `i` with every sell day `j > i`, and keep the best profit.

```python
prices=[7,2,5,1,6,4,8]
n=len(prices)
max_profit=0
for i in range(0,n):
    for j in range(i+1,n):
        if prices[j]>prices[i]:
            p=prices[j]-prices[i]
            max_profit=max(max_profit,p)
print(max_profit)
```

Complexity:
- Time: O(n^2)
- Space: O(1)

### Approach B In Notebook: One Pass (Optimal)
Track the minimum price seen so far. At each day, compute current profit as `price - min_price`, then update maximum profit.

```python
prices=[7,2,5,1,6,4,8]
n=len(prices)
max_profit=0
min_price=float('inf')
for i in range(0,n):
    min_price=min(min_price,prices[i])
    profit=prices[i]-min_price
    max_profit=max(max_profit,profit)
print(max_profit)
```

Complexity:
- Time: O(n)
- Space: O(1)

---

## 2) Maximum Subarray

### Problem
Given an integer array, find the contiguous subarray with the largest sum.

Notebook example:
- `nums = [-2,1,-3,4,-1,2,1,-5,4]`
- Output: `6` from subarray `[4,-1,2,1]`

### Approach A In Notebook: Brute Force (All Subarrays)
For each starting index, keep extending the subarray and update the maximum sum.

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]

n = len(nums)
maxi = float('-inf')

for i in range(n):
    total = 0
    for j in range(i, n):
        total += nums[j]
        maxi = max(maxi, total)

print(maxi)
```

Complexity:
- Time: O(n^2)
- Space: O(1)

### Approach B In Notebook: Kadane's Algorithm
Maintain a running sum. If running sum becomes negative, reset it to 0 because it will only hurt future subarrays.

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]

n = len(nums)
maxi = float('-inf')
total = 0
for i in range(0,n):
    total += nums[i]
    maxi = max(maxi, total)
    if total < 0:
        total = 0
print(maxi)
```

Complexity:
- Time: O(n)
- Space: O(1)

---

## 3) Rearrange Array Elements by Sign

### Problem
Rearrange array so positive and negative numbers appear alternately (starting from positive), assuming balanced counts in this notebook example.

Notebook example:
- `nums = [5,10,-2,-1,-10,6]`
- Possible output: `[5,-2,10,-1,6,-10]`

### Approach A In Notebook: Split Lists + Merge Back
Store positives and negatives separately, then place them at even and odd indices.

```python
nums = [5,10,-2,-1,-10,6]

pos = []
neg = []
for num in nums:
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)
for i in range(len(pos)):
    nums[2*i] = pos[i]
    nums[2*i + 1] = neg[i]

print(nums)
```

Complexity:
- Time: O(n)
- Space: O(n)

### Approach B In Notebook: Direct Indexed Placement
Create result array and place positives at `0,2,4,...` and negatives at `1,3,5,...` in one pass.

```python
nums = [5,10,-2,-1,-10,6]
n=len(nums)
result=[0]*n
pos_index,neg_index=0,1
for i in range(0,n):
    if nums[i]>0:
        result[pos_index]=nums[i]
        pos_index+=2
    else:
        result[neg_index]=nums[i]
        neg_index+=2
print(result)
```

Complexity:
- Time: O(n)
- Space: O(n)

---

## Practical Takeaways
1. Stock profit problems often reduce to tracking minimum-so-far and best-difference-so-far.
2. Maximum subarray brute force can be optimized to Kadane's algorithm with a simple reset rule.
3. Rearrangement problems are easier when you map positions first (even/odd index strategy).
4. Comparing brute-force vs optimal each time builds strong interview intuition.
5. Always test edge cases:
   - all decreasing stock prices (profit should be `0`)
   - all negative numbers in max-subarray (Kadane variant must still return maximum element)
   - unequal positive/negative counts for rearrangement variants
