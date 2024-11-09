import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.StdOut;

import java.util.LinkedList;

/**
 * Solver class to find a solution to the initial board using the A* algorithm.
 */
public class Solver {
    private LinkedList<Board> solution; // Stores the solution path

    /**
     * Constructor to find a solution to the initial board.
     *
     * @param initial the initial board
     * @throws IllegalArgumentException if the initial board is null
     */
    public Solver(Board initial) {
        // Throw an exception if the initial board is null
        if (initial == null) {
            throw new java.lang.IllegalArgumentException();
        }

        // Priority queues for the main board and its twin
        MinPQ<SearchNode> pq = new MinPQ<>();
        MinPQ<SearchNode> pqTwin = new MinPQ<>();

        // Insert the initial board and its twin into their respective priority queues
        pq.insert(new SearchNode(initial, 0, null));
        pqTwin.insert(new SearchNode(initial.twin(), 0, null));

        // Process the boards until a solution is found or both queues are empty
        while (!pq.isEmpty() && !pqTwin.isEmpty()) {
            // Get the board with the lowest priority from both queues
            SearchNode currentNode = pq.delMin();
            SearchNode currentNodeTwin = pqTwin.delMin();

            // Check if the current board is the goal
            if (currentNode.board.isGoal()) {
                buildPath(currentNode); // Build the solution path
                return;
            }

            // Check if the twin board is the goal
            if (currentNodeTwin.board.isGoal()) {
                solution = null; // No solution exists
                return;
            }

            // Add neighbors of the current board to the priority queue
            for (Board neighbor : currentNode.board.neighbors()) {
                if (currentNode.prevNode == null || !neighbor.equals(currentNode.prevNode.board)) {
                    pq.insert(
                            new SearchNode(neighbor, currentNode.g + 1, currentNode));
                }
            }

            // Add neighbors of the twin board to the priority queue
            for (Board neighbor : currentNodeTwin.board.neighbors()) {
                if (currentNodeTwin.prevNode == null || !neighbor.equals(
                        currentNodeTwin.prevNode.board)) {
                    pqTwin.insert(
                            new SearchNode(neighbor, currentNodeTwin.g + 1, currentNodeTwin));
                }
            }
        }

    }

    /**
     * Builds the solution path from the goal node to the initial node.
     *
     * @param node the goal node from which to build the path
     */
    private void buildPath(SearchNode node) {
        solution = new LinkedList<>(); // Initialize the solution path
        while (node != null) {
            solution.addFirst(
                    node.board); // Add the current board to the front of the solution path
            node = node.prevNode; // Move to the previous node
        }
    }

    /**
     * Checks if the initial board is solvable.
     *
     * @return true if the initial board is solvable, false otherwise
     */
    public boolean isSolvable() {
        return solution != null; // Returns true if a solution exists, false otherwise
    }

    /**
     * Returns the minimum number of moves to solve the initial board.
     *
     * @return the number of moves to solve the initial board, or -1 if unsolvable
     */
    public int moves() {
        if (!isSolvable()) return -1; // Return -1 if the board is unsolvable
        return solution.size()
                - 1; // Return the number of moves, which is the size of the solution path minus one
    }


    /**
     * Returns the sequence of boards in the shortest solution.
     *
     * @return an iterable of boards in the solution sequence; null if unsolvable
     */
    public Iterable<Board> solution() {
        return solution;
    }

    /**
     * SearchNode class used in the A* algorithm to represent a state in the search tree.
     */
    private class SearchNode implements Comparable<SearchNode> {
        private int f, g; // f is the total cost (g + heuristic), g is the cost from the start node
        private Board board; // The current board state
        private SearchNode prevNode; // The previous node in the search path

        /**
         * Constructs a SearchNode with the given board, cost, and previous node.
         *
         * @param board    the current board state
         * @param g        the cost from the start node to this node
         * @param prevNode the previous node in the search path
         */
        public SearchNode(Board board, int g, SearchNode prevNode) {
            this.board = board;
            this.g = g;
            this.f = g + board.manhattan();
            this.prevNode = prevNode;
        }

        /**
         * Compares this search node with another based on their total cost f.
         *
         * @param other the other search node to compare to
         * @return a negative integer, zero, or a positive integer as this node's f is less than,
         * equal to, or greater than the other node's f
         */
        public int compareTo(SearchNode other) {
            return Integer.compare(this.f, other.f);
        }
    }

    /**
     * Main method to solve the puzzle using the A* algorithm.
     * Reads the initial board configuration from a file, solves the puzzle,
     * and prints the solution to standard output.
     *
     * @param args command-line arguments, where args[0] is the path to the input file
     */
    public static void main(String[] args) {

        // Create initial board from file
        In in = new In(args[0]);
        int n = in.readInt();
        int[][] tiles = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                tiles[i][j] = in.readInt();
        Board initial = new Board(tiles);

        // Solve the puzzle
        Solver solver = new Solver(initial);

        // Print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }
}