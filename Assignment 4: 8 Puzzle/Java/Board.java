import edu.princeton.cs.algs4.StdOut;

import java.util.Arrays;
import java.util.LinkedList;

/**
 * Board class to represent an n-by-n board of tiles.
 */
public class Board {
    private final int n; // Dimension of the board
    private final int[][] board; // 2D array to store the tiles

    /**
     * Creates a board from an n-by-n array of tiles,
     * where tiles[row][col] = tile at (row, col).
     *
     * @param tiles an n-by-n array of tiles
     */
    public Board(int[][] tiles) {
        this.n = tiles.length; // Initialize the dimension of the board
        this.board = new int[n][n]; // Initialize the board array
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                this.board[i][j] = tiles[i][j]; // Copy the tiles to the board array
            }
        }
    }

    /**
     * Returns a string representation of this board.
     *
     * @return a string representation of the board
     */
    public String toString() {
        StringBuilder stringBoard = new StringBuilder();
        stringBoard.append(n).append("\n"); // Append the dimension of the board
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                stringBoard.append(" ").append(board[i][j]).append(" "); // Append each tile
            }
            stringBoard.append("\n"); // New line after each row
        }
        return stringBoard.toString();
    }

    /**
     * Returns the dimension of the board.
     *
     * @return the dimension of the board
     */
    public int dimension() {
        return n;
    }

    /**
     * Returns the number of tiles out of place.
     *
     * @return the Hamming distance
     */
    public int hamming() {
        int distance = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != n * i + j + 1 && board[i][j] != 0)
                    distance++;
            }
        }
        return distance;
    }

    /**
     * Returns the sum of Manhattan distances between tiles and the goal.
     *
     * @return the Manhattan distance
     */
    public int manhattan() {
        int distance = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != 0) {
                    int value = board[i][j];
                    int row = (value - 1) / n;
                    int col = (value - 1) % n;
                    distance += Math.abs(row - i) + Math.abs(col - j);
                }
            }
        }
        return distance;
    }

    /**
     * Checks if this board is the goal board.
     *
     * @return true if this board is the goal board, false otherwise
     */
    public boolean isGoal() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == n - 1 && j == n - 1) {
                    if (board[i][j] != 0) return false;
                }
                else if (board[i][j] != n * i + j + 1) return false;
            }
        }
        return true;
    }

    /**
     * Checks if this board is equal to another board.
     *
     * @param y the other board to compare to
     * @return true if this board is equal to the other board, false otherwise
     */
    public boolean equals(Object y) {
        if (this == y) {
            return true;
        }
        if (y == null || getClass() != y.getClass()) {
            return false;
        }
        Board other = (Board) y;
        return n == other.n && Arrays.deepEquals(board, other.board);
    }

    /**
     * Returns all neighboring boards.
     *
     * @return an iterable of neighboring boards
     */
    public Iterable<Board> neighbors() {
        LinkedList<Board> neighbors = new LinkedList<>();
        int[] indices = findIndices();
        int i = indices[0];
        int j = indices[1];

        int[][] candidates = new int[][] {
                { i - 1, j },
                { i + 1, j },
                { i, j - 1 },
                { i, j + 1 }
        };

        for (int[] candidate : candidates) {
            int x = candidate[0];
            int y = candidate[1];
            if (0 <= x && x < n && 0 <= y && y < n) {
                int[][] newBoard = new int[n][];
                for (int k = 0; k < n; k++) {
                    newBoard[k] = board[k].clone();
                }
                int temp = newBoard[i][j];
                newBoard[i][j] = newBoard[x][y];
                newBoard[x][y] = temp;
                neighbors.add(new Board(newBoard));
            }
        }
        return neighbors;
    }

    /**
     * Returns a board that is obtained by exchanging any pair of tiles.
     *
     * @return a twin board
     */
    public Board twin() {
        int[][] newBoard = new int[n][];
        int x1 = 0, y1 = 0, x2 = 0, y2 = 1;
        for (int k = 0; k < n; k++) {
            newBoard[k] = board[k].clone();
        }
        int[] indices = findIndices();
        int i = indices[0];
        int j = indices[1];
        if ((i == x1 && j == y1) || (i == x2 && j == y2)) {
            x1 = n - 1;
            x2 = n - 1;
            y1 = n - 1;
            y2 = n - 2;
        }

        int temp = newBoard[x1][y1];
        newBoard[x1][y1] = newBoard[x2][y2];
        newBoard[x2][y2] = temp;

        return new Board(newBoard);
    }

    private int[] findIndices() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] { -1, -1 };
    }


    /**
     * Unit testing for the Board class.
     * Creates a board, prints its string representation, Hamming and Manhattan distances,
     * checks if it is the goal board, prints all neighboring boards, and prints the twin board.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        int[][] tiles = {
                { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 0 }
        };
        Board b = new Board(tiles);

        // Print the string representation of the board
        StdOut.println(b.toString());

        // Print the Hamming distance of the board
        StdOut.println("Hamming distance = " + b.hamming());

        // Print the Manhattan distance of the board
        StdOut.println("Manhattan distance = " + b.manhattan());

        // Check if the board is the goal board and print the result
        StdOut.println("Is the goal? " + b.isGoal());

        // Print all neighboring boards
        for (Board neighbor : b.neighbors()) {
            StdOut.println(neighbor.toString());
        }

        // Print the twin board
        StdOut.println("Twin =\n" + b.twin());
    }
}