(Day 19: Selection, Bubble, and Insertion Sort)

## Bubble Sort
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted. The name comes from the way smaller elements "bubble" to the top of the list.

- **Time Complexity:** $O(n^2)$ (worst/average), $O(n)$ (best, already sorted)
- **Space Complexity:** $O(1)$ (in-place)
- **Stable:** Yes

## Insertion Sort
Insertion Sort builds the final sorted array one item at a time. It works by repeatedly taking the next unsorted element and inserting it into the correct position in the already sorted part of the array.

- **Time Complexity:** $O(n^2)$ (worst/average), $O(n)$ (best, already sorted)
- **Space Complexity:** $O(1)$ (in-place)
- **Stable:** Yes

## Selection Sort
Selection Sort repeatedly selects the smallest (or largest) element from the unsorted portion and swaps it with the first unsorted element. The sorted part grows from the beginning of the list.

- **Time Complexity:** $O(n^2)$ (all cases)
- **Space Complexity:** $O(1)$ (in-place)
- **Stable:** No (unless implemented carefully)

### Selection Sort Variants
- **Ascending Order:** Select the minimum element each time.
- **Descending Order:** Select the maximum element each time.

---
These algorithms are fundamental for understanding sorting and algorithmic thinking. While not efficient for large datasets, they are useful for small lists and educational purposes.
