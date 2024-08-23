from UnionFind import WeightedQuickUnionUF

class Percolation:
    def __init__(self, n):
        """
        Initializes a Percolation system with an n-by-n grid.

        Args:
            n (int): Grid size.
        """

        # Create an n-by-n grid with all sites initially blocked (0 represents blocked sites)
        self.n = n
        self.grid = [0] * n ** 2

        # Define virtual top and bottom sites for percolation
        self.top = n ** 2  # Virtual top site
        self.bottom = n ** 2 + 1  # Virtual bottom site

        # Initialize union-find data structures
        self.uf = WeightedQuickUnionUF(n ** 2 + 2)  # 2 extra spaces for virtual nodes
        self.full = WeightedQuickUnionUF(n ** 2 + 2) # To track full sites and avoid backwash
        self.OpenSites = 0  # Counter for open sites


    def open(self, row, col):
        """
        Opens the site at (row, col) if it is not already open.

        Args:
            row (int): Row index.
            col (int): Column index.
        """

        if not self.isOpen(row, col):
            position = self.getIndex(row, col)
            self.grid[position] = 1  # Mark the site as open
            self.OpenSites += 1  # Update the count of open sites

            if row == 1:
                # Connect the top row to the second-to-last element (virtual top site)
                self.uf.union(self.top, self.getIndex(row, col))
                self.full.union(self.top, self.getIndex(row, col))

            if row == self.n:
                # Connect the lower row to the last element (virtual bottom site)
                self.uf.union(self.bottom, self.getIndex(row, col))

            # Check neighboring sites and connect if they are also open
            neighbours = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
            for i, j in neighbours:
                if 1 <= i <= self.n and 1 <= j <= self.n:
                    position_j = self.getIndex(i, j)
                    if self.isOpen(i, j):
                        self.uf.union(position, position_j)  # Connect neighboring open sites
                        self.full.union(position, position_j)


    def isOpen(self, row, col):
        """
        Checks whether a site at (row, col) is open (unblocked).

        Args:
            row (int): Row index.
            col (int): Column index.

        Returns:
            bool: True if the site is open, False otherwise.
        """

        position = self.getIndex(row, col)
        return self.grid[position] == 1

    def isFull(self, row, col):
        """
        Determines whether a site at (row, col) is full (connected to the top row).

        Args:
            row (int): Row index.
            col (int): Column index.

        Returns:
            bool: True if the site is full, False otherwise.
        """

        position = self.getIndex(row, col)
        return self.full.root(position) == self.full.root(self.top) and self.isOpen(row, col)

    def numberOfOpenSites(self):
        """
        Returns the total number of open sites.

        Returns:
            int: Number of open sites.
        """

        return self.OpenSites

    def percolates(self):
        """
        Checks if the system percolates (top and bottom virtual sites are connected).

        Returns:
            bool: True if the system percolates, False otherwise.
        """
        #if self.n == 1:
        #    return self.isOpen(self.n, self.n)

        return self.uf.root(self.top) == self.uf.root(self.bottom)  # Check if virtual top and bottom are connected

    def getIndex(self, row, col):
        """
        Calculates the index corresponding to a given row and column in a flattened grid.

        Args:
            row (int): Row number (1-based index).
            col (int): Column number (1-based index).

        Returns:
            int: The flattened index corresponding to the specified row and column.
        """

        return (row - 1) * self.n + col - 1
