import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private int n; // Grid size (n-by-n)
    private boolean[] grid; // Tracks open/closed sites
    private WeightedQuickUnionUF uf; // Union-find data structure
    private WeightedQuickUnionUF full; // For tracking full sites (avoiding backwash)
    private int openSites; // Counter for open sites
    private int top; // Virtual top site
    private int bottom; // Virtual bottom site

    /**
     * Initializes a Percolation system with an n-by-n grid.
     *
     * @param n The size of the grid.
     * @throws IllegalArgumentException if n is less than or equal to 0.
     */
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("Grid size must be positive.");
        }

        // Create an n-by-n grid with all sites initially blocked
        this.n = n;
        grid = new boolean[n * n];

        // Define virtual top and bottom sites for percolation
        top = n * n; // Virtual top site
        bottom = n * n + 1; // Virtual bottom site

        // Initialize union-find data structures
        uf = new WeightedQuickUnionUF(n * n + 2); // 2 extra spaces for virtual nodes
        full = new WeightedQuickUnionUF(n * n + 2); // To track full sites and avoid backwash
        openSites = 0; // Counter for open sites
    }

    /**
     * Opens the site at (row, col) if it is not already open.
     *
     * @param row The row index (1-based).
     * @param col The column index (1-based).
     */
    public void open(int row, int col) {
        checkException(row, col);

        if (!isOpen(row, col)) {
            int position = getIndex(row, col);
            grid[position] = true; // Mark the site as open
            openSites++; // Update the count of open sites

            if (row == 1) {
                // Connect the top row to the second-to-last element (virtual top site)
                uf.union(top, getIndex(row, col));
                full.union(top, getIndex(row, col));
            }

            if (row == n) {
                // Connect the lower row to the last element (virtual bottom site)
                uf.union(bottom, getIndex(row, col));
            }

            // Check neighboring sites and connect if they are also open
            int[][] neighbours = {
                    { row - 1, col }, { row + 1, col }, { row, col - 1 }, { row, col + 1 }
            };
            for (int[] neighbor : neighbours) {
                int i = neighbor[0];
                int j = neighbor[1];
                if (i >= 1 && i <= n && j >= 1 && j <= n && isOpen(i, j)) {
                    int position2 = getIndex(i, j);
                    uf.union(position, position2); // Connect neighboring open sites
                    full.union(position, position2); // Connect neighboring open sites
                }
            }
        }
    }

    /**
     * Checks whether a site at (row, col) is open (unblocked).
     *
     * @param row The row index (1-based).
     * @param col The column index (1-based).
     * @return true if the site is open, false otherwise.
     */
    public boolean isOpen(int row, int col) {
        checkException(row, col);

        int position = getIndex(row, col);
        return grid[position];
    }

    /**
     * Determines whether a site at (row, col) is full (connected to the top row).
     *
     * @param row The row index (1-based).
     * @param col The column index (1-based).
     * @return true if the site is full, false otherwise.
     */
    public boolean isFull(int row, int col) {
        checkException(row, col);

        int position = getIndex(row, col);
        return (full.find(position) == full.find(top)) && isOpen(row, col);
    }

    /**
     * Returns the total number of open sites.
     *
     * @return The count of open sites.
     */
    public int numberOfOpenSites() {
        return openSites;
    }

    /**
     * Checks if the system percolates (top and bottom virtual sites are connected).
     *
     * @return true if the system percolates, false otherwise.
     */
    public boolean percolates() {
        if (this.n == 1) {
            return isOpen(1, 1);
        }
        return uf.find(top) == uf.find(bottom);
    }

    /**
     * Validates whether the given row and column indices are within bounds.
     *
     * @param row The row index.
     * @param col The column index.
     * @throws IllegalArgumentException if indices are out of bounds.
     */
    private void checkException(int row, int col) {
        if (row <= 0 || row > this.n || col <= 0 || col > this.n) {
            throw new IllegalArgumentException();
        }
    }

    /**
     * Calculates the index corresponding to a given row and column in a flattened grid.
     *
     * @param row The row index.
     * @param col The column index.
     * @return The flattened index.
     */
    private int getIndex(int row, int col) {
        // Calculates the index corresponding to a given row and column in a flattened grid.
        return this.n * (row - 1) + col - 1;
    }

    /**
     * Example usage demonstrating the Percolation class.
     */
    public static void main(String[] args) {
        int gridSize = 5;
        Percolation percolation = new Percolation(gridSize);
        percolation.open(1, 1);
        percolation.open(2, 1);
        System.out.println("Percolates? " + percolation.percolates()); // Should print false
    }
}
