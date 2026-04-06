# Day 17 Notes: Frequency Maps & Hashing

## 1) What is a Frequency Map?
- A frequency map (or dictionary) counts how many times each element appears in a collection (list, string, etc).
- In Python, this is typically implemented using a `dict`.

Example:
```python
nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
freq_map = {}
for num in nums:
    freq_map[num] = freq_map.get(num, 0) + 1
print(freq_map)
```

---

## 2) Why Use Hashing?
- Hashing allows for fast lookups, insertions, and deletions (average O(1) time).
- Useful for counting, membership checks, and pre-storing values for quick access.

---

## 3) Brute Force vs Hashing
- Brute force: For each query, scan the entire list (O(n*m) time).
- Hashing: Precompute frequencies, then answer each query in O(1) (total O(n+m) time).

---

## 4) Hashing with Lists vs Dictionaries
- If values are small integers in a known range, use a list for constant space.
- For arbitrary values (large numbers, strings), use a dictionary.

---

## 5) Character Frequency (String Hashing)
- Count occurrences of each character in a string using a dictionary.

Example:
```python
s = 'azyxyyzaaaa'
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
```

---

## 6) Time & Space Complexity
- Building a frequency map: O(n) time, O(k) space (k = unique elements)
- Querying: O(1) per query

---

## Key Takeaways
- Frequency maps and hashing are essential for efficient counting and lookup tasks.
- Use lists for small, fixed ranges; use dicts for general cases.
- Hashing reduces time complexity from O(n*m) to O(n+m) in many problems.
