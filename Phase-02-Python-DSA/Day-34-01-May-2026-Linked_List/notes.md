# Day 34 Notes — Linked List

## Definitions
- A linked list is a linear data structure made of nodes, where each node stores data and a reference to the next node.
- The first node is reached through the head reference.
- If the list is empty, the head is `None`.

## Where to use Linked List?
- Use a linked list when you expect frequent insertions and deletions.
- It is dynamic in nature, so it can grow or shrink as needed.
- It is useful when contiguous memory allocation is not ideal.

## Types of Linked List
- Singly linked list: each node points to the next node.
- Doubly linked list: each node points to both next and previous nodes.
- Circular linked list: the last node points back to the first node.

## Singly Linked List Operations
- Insert at end: traverse to the last node and append the new node.
- Insert at specified position: move to the required index and link the new node.
- Traverse: visit each node and print or process its value.
- Delete: remove a node by value and reconnect the surrounding nodes.

## Example (from the notebook)
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traverse(self):
        if not self.head:
            print("SLL IS EMPTY")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next
            print()

    def insert_at_specified_position(self, val, pos):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            count = 0
            while curr is not None and count < pos - 1:
                curr = curr.next
                count += 1

            if curr is None:
                print("Position out of bounds")
            else:
                new_node.next = curr.next
                curr.next = new_node

    def delete(self, val):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        if temp.val == val:
            self.head = temp.next
            return

        prev = None
        while temp is not None:
            if temp.val == val:
                break
            prev = temp
            temp = temp.next

        if temp is not None:
            prev.next = temp.next
        else:
            print("Value not found")
```

## Notes
- Keep a tail reference if you need frequent O(1) appends.
- For many index-based accesses, arrays are usually a better choice.
- Keep a previous pointer while deleting nodes in the middle of the list.

## Example Output Flow
- Insert `10`, `20`, `30` and traverse -> `10 20 30`
- Insert `15` at position `1` and traverse -> `10 15 20 30`
- Delete `20` and traverse -> `10 15 30`

## Complexity
- Insert at head: O(1)
- Insert at end: O(n)
- Insert at position: O(n)
- Delete: O(n)
- Traverse: O(n)

---
See `README.md` for the day's overview and notebook references.

