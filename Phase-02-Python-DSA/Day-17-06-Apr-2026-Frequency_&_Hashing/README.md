# Day 17: Frequency Maps & Hashing

## Overview
This day focuses on using frequency maps (dictionaries) and hashing techniques to efficiently count and query occurrences in lists and strings.

- What is a frequency map?
- Why and how to use hashing
- Brute force vs hashing for queries
- Hashing with lists (for small integer ranges) vs dictionaries (for general cases)
- Character frequency (string hashing)
- Time and space complexity analysis

## Folder Structure & Practice Files

- `frequency_map_&_Dict/store_freq.ipynb`  
    - Building frequency maps for lists (multiple methods)

- `hashing/hashing.ipynb`  
    - Brute force vs hashing for queries
    - Integer hashing with lists (fixed range)
    - Dictionary hashing for general cases
    - Character frequency (string hashing)
    - Complexity analysis

- `practice/array.ipynb`  
    - Frequency map for arrays
- `practice/count_char.ipynb`  
    - Character frequency in strings (brute force & optimal)
- `practice/count_distinct_element.ipynb`  
    - Count distinct elements (set & hashmap)
- `practice/most_freq_elem.ipynb`  
    - Find most frequent element
- `practice/non_rep_elem.ipynb`  
    - First non-repeating and first repeating element
- `practice/query_freq.ipynb`  
    - Query element frequencies efficiently
- `practice/skill_map.ipynb`  
    - Skill matching system using frequency map
- `practice/anagram.ipynb`  
    - Anagram check (sorting & hashmap)

## Key Learning Outcomes
After completing Day 17, you should be able to:
- Build and use frequency maps for counting elements in lists and strings.
- Understand brute force vs hashing approaches for queries.
- Use lists for hashing when the value range is small and known.
- Use dictionaries for general-purpose hashing and string/character frequency.
- Analyze time and space complexity for frequency counting and query problems.

## Quick Revision
- Frequency maps (dicts) allow O(1) average time for counting and lookups.
- Hashing reduces time complexity from O(n*m) to O(n+m) in many query problems.
- Use lists for hashing only when the value range is small and fixed.
- Character frequency is a direct application of hashing in strings.

# Tomorrow
- Recursion
