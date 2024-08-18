/**
 * This class represents a randomized queue, which allows adding and removing items in random order.
 * It uses an array-based implementation with resizing to efficiently manage the items.
 * The class provides methods for enqueueing, dequeuing, sampling, and iterating over the items.
 *
 * @param <Item> the type of items stored in the queue
 */

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

import java.util.Iterator;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] s; // Array to store items
    private int n = 0; // Number of items in the queue

    /**
     * Constructs an empty randomized queue.
     */
    public RandomizedQueue() {
        s = (Item[]) new Object[1];
    }

    /**
     * Checks if the randomized queue is empty.
     *
     * @return true if the queue is empty, false otherwise
     */
    public boolean isEmpty() {
        return n == 0;
    }

    /**
     * Returns the number of items in the randomized queue.
     *
     * @return the number of items
     */
    public int size() {
        return n;
    }

    /**
     * Adds an item to the randomized queue.
     *
     * @param item the item to be added
     * @throws IllegalArgumentException if the input item is null
     */
    public void enqueue(Item item) {
        if (item == null) throw new IllegalArgumentException();
        if (n == s.length) resize(2 * s.length);
        s[n++] = item;
    }

    // Private helper method to resize the array
    private void resize(int capacity) {
        Item[] copy = (Item[]) new Object[capacity];
        for (int i = 0; i < n; i++) copy[i] = s[i];
        s = copy;
    }

    /**
     * Removes and returns a random item from the queue.
     *
     * @return the removed item
     * @throws java.util.NoSuchElementException if the queue is empty
     */
    public Item dequeue() {
        if (isEmpty()) {
            throw new java.util.NoSuchElementException();
        }
        int index = StdRandom.uniformInt(0, n);
        Item item = s[index];
        s[index] = s[--n];
        s[n] = null;
        if (n > 0 && n == s.length / 4) resize(s.length / 2);
        return item;
    }

    /**
     * Returns a random item from the queue without removing it.
     *
     * @return a random item
     * @throws java.util.NoSuchElementException if the queue is empty
     */
    public Item sample() {
        if (isEmpty()) {
            throw new java.util.NoSuchElementException();
        }
        int index = StdRandom.uniformInt(0, n);
        Item item = s[index];
        return item;
    }

    /**
     * Returns an independent iterator over items in random order.
     *
     * @return an iterator
     */
    public Iterator<Item> iterator() {
        return new ReverseArrayIterator();
    }

    // Private inner class for the iterator
    private class ReverseArrayIterator implements Iterator<Item> {
        private int i = n;
        private Item[] copy;

        public ReverseArrayIterator() {
            copy = (Item[]) new Object[n];
            for (int j = 0; j < n; j++) {
                copy[j] = s[j];
            }
        }

        public boolean hasNext() {
            return i > 0;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }

        public Item next() {
            if (!hasNext()) throw new java.util.NoSuchElementException();
            int index = StdRandom.uniformInt(0, i);
            Item item = copy[index];
            copy[index] = copy[--i];
            copy[i] = item;
            return item;
        }
    }

    // Unit Testing
    public static void main(String[] args) {
        RandomizedQueue<Integer> randomQueue = new RandomizedQueue<>();
        randomQueue.enqueue(5);
        randomQueue.enqueue(4);
        randomQueue.enqueue(3);
        randomQueue.enqueue(2);
        randomQueue.enqueue(1);
        for (int i : randomQueue) {
            StdOut.println("Item: " + i);
        }
        StdOut.println("randomQueue is empty? " + randomQueue.isEmpty());
        StdOut.println("Size = " + randomQueue.size());
        StdOut.println("Show a random element: " + randomQueue.sample());
        StdOut.println("Remove a random element: " + randomQueue.dequeue());
        StdOut.println("Size = " + randomQueue.size());
    }
}