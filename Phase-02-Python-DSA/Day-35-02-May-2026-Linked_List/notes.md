# Day 35 Notes: Linked List Cycle Detection

## 1) Problem
Given the head of a singly linked list, determine if the list has a cycle in it. Return `True` if a cycle exists, otherwise `False`.

Example:
- List nodes: 10 -> 20 -> 30 -> 40
- If `40.next = 20`, the list contains a cycle and the answer is `True`.

## 2) Approaches

### Approach A: Hashing (visited set)
Keep a set of visited node references. Iterate through the list; if a node is already in the set, a cycle exists.

```python
def hasCycle_hash(head):
    seen = set()
    curr = head
    while curr is not None:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False
```

- Complexity: Time O(n), Space O(n)
- Notes: Simple and reliable; uses extra memory to track nodes by identity.

### Approach B: Floyd's Tortoise and Hare (two pointers)
Use two pointers `slow` and `fast` starting at `head`. Move `slow` one step and `fast` two steps each loop. If they meet, a cycle exists. If `fast` reaches `None`, there is no cycle.

```python
def hasCycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

- Complexity: Time O(n), Space O(1)
- Why it works: In a cycle, the fast pointer gains on the slow pointer by one step per iteration (relative speed), guaranteeing a meeting within O(n) steps.

### (Optional) Find cycle start node
Once `slow` and `fast` meet, to find the start of the cycle reset one pointer to `head` and move both one step at a time; their meeting point is the cycle entry.

```python
def findCycleStart(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
```

- Usefulness: Useful for problems that require removing the cycle or returning the entry node.

## 3) Notebook Example (from `linked_list_cycle.ipynb`)
- The notebook defines a simple `Node` class and two detection functions (hash and Floyd).
- A small test constructs a 4-node list and links the last node back to the second to create a cycle, then prints `True` when detection runs.

## 4) Complexity Snapshot

| Variant | Time | Space |
|---|---:|---:|
| Hashing visited nodes | O(n) | O(n) |
| Floyd's algorithm | O(n) | O(1) |

## 5) Practical Takeaways
- Prefer Floyd's algorithm in interviews due to O(1) space and elegance.
- Hashing is straightforward and acceptable when memory is not constrained or when rapid prototyping.
- When creating tests that form cycles, be careful to avoid infinite traversal when printing — use detection first or limit traversal steps.
- Remember the trick to find the cycle start — reset pointer to head and advance both pointers in tandem.

---

Happy practicing — ask if you want a short runnable script or extra tests added to the notebook.
