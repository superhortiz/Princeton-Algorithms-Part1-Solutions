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


import random
from copy import deepcopy

class RandomizedQueue:
    def __init__(self):
        """
        Initializes an empty randomized queue.
        """
        self.s = [] # Internal list to store elements
        self.n = 0 # Number of elements in the queue

    def is_empty(self):
        """
        Checks if the randomized queue is empty.

        Returns:
            True if empty, False otherwise.
        """
        return self.n == 0

    def size(self):
        """
        Returns the number of elements in the randomized queue.

        Returns:
            Number of elements.
        """
        return self.n

    def enqueue(self, item):
        """
        Adds an item to the randomized queue.

        Args:
            item: The item to enqueue.

        Raises:
            ValueError: If the item is None.
        """
        if item is None:
            raise ValueError("Cannot enqueue None")

        self.s.append(item)
        self.n += 1

    def dequeue(self):
        """
        Removes and returns a random item from the randomized queue.

        Returns:
            The dequeued item.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        index = random.randint(0, self.n - 1)
        item = self.s[index]
        self.s[index] = self.s[self.n - 1]
        self.s.pop()
        self.n -= 1
        return item

    def sample(self):
        """
        Returns a random item from the randomized queue without removing it.

        Returns:
            A randomly sampled item.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        index = random.randint(0, self.n - 1)
        return self.s[index]

    def iterator(self):
        """
        Returns an iterator over a shuffled copy of the elements in the randomized queue.
        The original queue remains unchanged.

        Returns:
            An iterator.
        """
        copy = deepcopy(self.s)
        random.shuffle(copy)
        return iter(copy)


# Example usage
if __name__ == "__main__":
    random_queue = RandomizedQueue()
    random_queue.enqueue(5)
    random_queue.enqueue(4)
    random_queue.enqueue(3)
    random_queue.enqueue(2)
    random_queue.enqueue(1)
    for item in random_queue.iterator():
        print(f"Item: {item}")
    print(f"random_queue is empty? {random_queue.is_empty()}")
    print(f"Size = {random_queue.size()}")
    print(f"Show a random element: {random_queue.sample()}")
    print(f"Remove a random element: {random_queue.dequeue()}")
    print(f"Size = {random_queue.size()}")
