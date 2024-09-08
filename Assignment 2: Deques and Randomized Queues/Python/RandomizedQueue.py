"""
The `RandomizedQueue` class represents a queue where the item removed is chosen uniformly at random
from items in the data structure. It uses a dynamic array (Python list) for efficient operations.

Usage:
- Create a randomized queue: `random_queue = RandomizedQueue()`
- Add an item: `random_queue.enqueue(item)`
- Remove a random item: `random_queue.dequeue()`
- Sample a random item without removing: `random_queue.sample()`
- Check if the queue is empty: `random_queue.is_empty()`
- Get the number of items: `random_queue.size()`
- Iterate over items in random order: `for item in random_queue.iterator(): ...`

Note: The `RandomizedQueue` class ensures that each iterator returns the items in uniformly random order.
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
