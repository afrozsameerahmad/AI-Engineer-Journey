# Day 35: Linked List — Cycle Detection

## Overview
This day focuses on detecting cycles in a singly linked list. The notebook demonstrates two common approaches:

- Floyd's Tortoise and Hare (fast/slow pointers) — O(n) time, O(1) space
- Hashing visited nodes — O(n) time, O(n) space

The practice notebook shows implementations, tests that create cycles, and explains why the fast/slow approach finds a cycle.

## Notebook Files
- `linked_list_cycle.ipynb`: Implements cycle detection using both hashing and Floyd's algorithm. Includes a simple test that creates a cycle and checks detection.

**Notebook implementation note (Floyd's algorithm):**
- Initialize `slow` and `fast` at the head. Move `slow` by one and `fast` by two steps. If they ever meet, a cycle exists. If `fast` reaches `None`, there is no cycle.

## What Was Practiced
- Two-pointer (fast/slow) technique and loop invariants
- Using auxiliary data structures (set) to track seen nodes
- Constructing and testing cyclic linked lists safely
- (Optional) Finding the entry node of the cycle using pointer resetting

## Complexity Snapshot

| Problem | Approach | Time | Space |
|---|---|---:|---:|
| Linked List Cycle Detection | Hashing (visited set) | O(n) | O(n) |
| Linked List Cycle Detection | Floyd's Tortoise & Hare | O(n) | O(1) |

## Key Patterns Practiced
- Fast/slow pointer pattern for cycle detection and related problems
- Building robust tests that intentionally create cycles
- Reasoning about pointer movement and termination conditions

## Difficulty Level
Easy — common interview question; foundational pointer technique.

---
See `notes.md` for detailed explanations, code examples, and practical takeaways.
