/**
 * The `Deque` class represents a double-ended queue (deque) that allows adding and removing items
 * from both the front and the back. It uses a doubly linked list implementation.
 *
 * @param <Item> the type of items stored in the deque
 */

import edu.princeton.cs.algs4.StdOut;
import java.util.Iterator;

public class Deque<Item> implements Iterable<Item> {
    private class Node {
        Item item;
        Node next;
        Node prev;
    }

    private Node first, last; // Pointers to the first and last nodes
    private int size; // Number of items in the deque

    /**
     * Constructs an empty deque.
     */
    public Deque() {
        first = null;
        last = null;
    }

    /**
     * Checks if the deque is empty.
     *
     * @return true if the deque is empty, false otherwise
     */
    public boolean isEmpty() {
        return first == null && last == null;
    }

    /**
     * Returns the number of items in the deque.
     *
     * @return the number of items
     */
    public int size() {
        return size;
    }

    /**
     * Adds an item to the front of the deque.
     *
     * @param item the item to be added
     * @throws IllegalArgumentException if the input item is null
     */
    public void addFirst(Item item) {
        if (item == null) throw new IllegalArgumentException();
        size++;
        Node newNode = new Node();
        newNode.item = item;

        if (isEmpty()) {
            first = newNode;
            last = newNode;
        }
        else {
            newNode.next = first;
            first.prev = newNode;
            first = newNode;
        }
    }

    /**
     * Adds an item to the back of the deque.
     *
     * @param item the item to be added
     * @throws IllegalArgumentException if the input item is null
     */
    public void addLast(Item item) {
        if (item == null) throw new IllegalArgumentException();
        size++;
        Node newNode = new Node();
        newNode.item = item;

        if (isEmpty()) {
            first = newNode;
            last = newNode;
        }
        else {
            newNode.prev = last;
            last.next = newNode;
            last = newNode;
        }
    }

    /**
     * Removes and returns the item from the front of the deque.
     *
     * @return the removed item
     * @throws java.util.NoSuchElementException if the deque is empty
     */
    public Item removeFirst() {
        if (isEmpty()) {
            throw new java.util.NoSuchElementException();
        }
        size--;
        Item item = first.item;
        first = first.next;
        if (first == null) {
            last = null;
        }
        else {
            first.prev = null;
        }
        return item;
    }

    /**
     * Removes and returns the item from the back of the deque.
     *
     * @return the removed item
     * @throws java.util.NoSuchElementException if the deque is empty
     */
    public Item removeLast() {
        if (isEmpty()) {
            throw new java.util.NoSuchElementException();
        }
        size--;
        Item item = last.item;
        last = last.prev;
        if (last == null) {
            first = null;
        }
        else {
            last.next = null;
        }
        return item;
    }

    /**
     * Returns an iterator over items in order from front to back.
     *
     * @return an iterator
     */
    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    // Private inner class for the iterator
    private class ListIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }

        public Item next() {
            if (!hasNext()) throw new java.util.NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    // Unit Testing
    public static void main(String[] args) {
        Deque<Integer> deque = new Deque<>();
        deque.addFirst(2);
        deque.addFirst(1);
        deque.addLast(3);
        deque.addLast(4);
        deque.addLast(5);
        for (int i : deque) {
            StdOut.println("Item: " + i);
        }
        StdOut.println("Remove the first item: " + deque.removeFirst());
        StdOut.println("Remove the last item: " + deque.removeLast());
        StdOut.println("Deque is empty? " + deque.isEmpty());
        StdOut.println("Size = " + deque.size());
    }
}
