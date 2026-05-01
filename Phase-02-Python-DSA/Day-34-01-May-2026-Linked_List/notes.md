# Day 34 — Linked List Notes

## What is a Linked List?
A linked list is a linear data structure where each element is a node that contains data and a reference (link) to the next node. The head is a reference to the first node; an empty list has a null head.

## When to use
- When you need frequent insertions/deletions (dynamic size).
- Good when you want constant-time insertions at head or when memory for contiguous array allocation is not feasible.

## Types
- Singly linked list — nodes have a `next` pointer (one direction).
- Doubly linked list — nodes have `next` and `prev` pointers (two directions).
- Circular linked list — last node links back to the first node.

## Singly Linked List — Key operations
- Insert at end: traverse to tail and append (O(n)) unless tail pointer maintained.
- Insert at head: O(1).
- Insert at position: O(n) to reach position.
- Delete by value/position: O(n) to find node.
- Traverse / print: O(n).

## Complexity (Singly Linked List)
- Access (by index): O(n)
- Search: O(n)
- Insert at head: O(1)
- Insert at tail: O(n) (O(1) with tail pointer)
- Deletion: O(n)

## Example (Node + SinglyLinkedList)
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

## Notes / Tips
- Keep a `tail` reference when you need frequent O(1) appends.
- For many index-based accesses, arrays (lists) are a better choice.
- When deleting nodes while traversing, keep a reference to `prev`.

## Practice exercises
1. Implement `reverse()` to reverse a singly linked list in-place.
2. Detect a cycle (Floyd's Tortoise and Hare algorithm).
3. Merge two sorted linked lists into a single sorted list.
4. Find middle node (fast/slow pointer).
5. Remove the N-th node from the end in one pass.

## References / Examples
- See `Linked_list/Singly.ipynb` for a runnable example of insertion, traversal and deletion.

