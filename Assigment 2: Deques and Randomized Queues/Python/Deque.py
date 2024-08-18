"""
The `Deque` class represents a double-ended queue (deque) that allows adding and removing items
from both ends of the collection. It uses a doubly linked list implementation for efficient
operations at both ends.

Usage:
- Create a deque: `my_deque = Deque()`
- Add items to the front: `my_deque.addFirst(item)`
- Add items to the back: `my_deque.addLast(item)`
- Remove an item from the front: `my_deque.removeFirst()`
- Remove an item from the back: `my_deque.removeLast()`
- Iterate over items: `for item in my_deque.Iterator(): ...`

Note: The `Deque` class includes an inner `Node` class for representing nodes in the linked list.
"""

class Deque:
    def __init__(self):
        """
        Initializes an empty deque.
        """
        self.first = None
        self.last = None
        self.size = 0

    class Node:
        def __init__(self, val, next = None, prev = None):
            """
            Represents a node in the doubly linked list.

            Args:
                val: The value stored in the node.
                next: Reference to the next node.
                prev: Reference to the previous node.
            """
            self.val = val
            self.next = next
            self.prev = prev

    class IteratorClass:
        def __init__(self, head):
            """
            Initializes an iterator for the deque.

            Args:
                head: The starting node for iteration.
            """
            self.head = head

        def __iter__(self):
            return self

        def __next__(self):
            """
            Returns the next item during iteration.

            Raises:
                StopIteration: When there are no more items to iterate.

            Returns:
                The value of the current node.
            """
            curr = self.head
            if curr:
                item = curr.val
                self.head = curr.next
                return item
            else:
                raise StopIteration

    def isEmpty(self):
        """
        Checks if the deque is empty.

        Returns:
            True if the deque is empty, False otherwise.
        """
        return self.first == None

    def size(self):
        """
        Returns the number of items in the deque.

        Returns:
            The number of items.
        """
        return self.size

    def addFirst(self, val):
        """
        Adds an item to the front of the deque.

        Args:
            val: The item to be added.

        Raises:
            ValueError: If the input item is None.
        """
        self.size += 1
        if self.isEmpty():
            self.first = self.last = self.Node(val)
        else:
            new_node = self.Node(val, next = self.first)
            self.first.prev = new_node
            self.first = new_node

    def addLast(self, val):
        """
        Adds an item to the back of the deque.

        Args:
            val: The item to be added.

        Raises:
            ValueError: If the input item is None.
        """
        self.size += 1
        if self.isEmpty():
            self.first = self.last = self.Node(val)
        else:
            new_node = self.Node(val, prev = self.last)
            self.last.next = new_node
            self.last = new_node

    def removeFirst(self):
        """
        Removes and returns the item from the front of the deque.

        Returns:
            The removed item.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.isEmpty():
            print('The list is empty')
        else:
            self.size -= 1
            item = self.first.val
            self.first = self.first.next
            if self.first == None:
                self.last = None
            else:
                self.first.prev = None
            return item

    def removeLast(self):
        """
        Removes and returns the item from the back of the deque.

        Returns:
            The removed item.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.isEmpty():
            print('The list is empty')
        else:
            self.size -= 1
            item = self.last.val
            self.last = self.last.prev
            if self.last == None:
                self.first = None
            else:
                self.last.next = None
            return item

    def Iterator(self):
        """
        Returns an iterator over items in order from front to back.

        Returns:
            An iterator.
        """
        return self.IteratorClass(self.first)

    def __str__(self):
        """
        Returns a string representation of the deque.

        Returns:
            A string showing the items in the deque.
        """
        curr = self.first
        sequence = []
        while curr:
            sequence.append(str(curr.val))
            curr = curr.next
        return ' <-> '.join(sequence)

    def reversed(self):
        """
        Returns a string representation of the deque in reverse order.

        Returns:
            A string showing the items in reverse order.
        """
        curr = self.last
        sequence = []
        while curr:
            sequence.append(str(curr.val))
            curr = curr.prev
        return ' <-> '.join(sequence)


# Example usage
a = Deque()
a.addFirst(1)
a.addFirst(2)
a.addFirst(3)
a.addLast(53)
print(a)

for element in a.Iterator():
    print(element)