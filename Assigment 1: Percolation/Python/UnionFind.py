class WeightedQuickUnionUF:
    def __init__(self, n):
        """
        Initializes a Weighted Quick Union data structure.

        Args:
            n (int): The number of sites in the system.
        """
        # Initialize the id array: Each site is initially its own root.
        self.id = [i for i in range(n)]
        self.size = [1] * (n) # Initialize component sizes

    def root(self, i):
        """
        Finds the root (representative) of the component containing site i.

        Args:
            i (int): Site index.

        Returns:
            int: Root of the component.
        """

        # Chase parent pointers until reach root (path compression)
        while self.id[i] != i:
            # Path compression: Flatten the tree by updating parent pointers
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        return i

    def connected(self, p, q):
        """
        Checks if sites p and q are in the same component.

        Args:
            p (int): Site index.
            q (int): Site index.

        Returns:
            bool: True if p and q are connected, False otherwise.
        """

        return self.root(p) == self.root(q)

    def union(self, p, q):
        """
        Merges the components containing sites p and q.

        Args:
            p (int): Site index.
            q (int): Site index.
        """

        # Change root of p to point to root of q (weighted union)
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return

        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]

        else:
            self.id[j] = i
            self.size[i] += self.size[j]
