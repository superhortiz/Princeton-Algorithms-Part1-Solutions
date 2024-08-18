/**
 * The `Permutation` class reads strings from standard input, enqueues them into a randomized queue,
 * and then dequeues and prints `k` random strings.
 * <p>
 * Usage:
 * - Run: java Permutation k < input.txt
 * (where `k` is the number of random strings to print)
 */

import edu.princeton.cs.algs4.StdIn;

public class Permutation {
    public static void main(String[] args) {
        // Create a randomized queue to store strings
        RandomizedQueue<String> randQueue = new RandomizedQueue<>();

        // Read the integer k from the command-line argument
        int k = Integer.parseInt(args[0]);

        // Read strings from standard input and enqueue them
        while (!StdIn.isEmpty()) {
            randQueue.enqueue(StdIn.readString());
        }

        // Dequeue and print k random strings
        for (int i = 0; i < k; i++) {
            System.out.println(randQueue.dequeue());
        }
    }
}