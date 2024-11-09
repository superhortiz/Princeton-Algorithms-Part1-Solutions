import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

import java.util.LinkedList;
import java.util.TreeSet;

public class PointSET {
    private TreeSet<Point2D> treeset;

    /**
     * Constructs an empty set of points.
     */
    public PointSET() {
        treeset = new TreeSet<>();
    }

    /**
     * Checks if the set is empty.
     *
     * @return {@code true} if the set is empty, {@code false} otherwise
     */
    public boolean isEmpty() {
        return treeset.isEmpty();
    }

    /**
     * Returns the number of points in the set.
     *
     * @return the number of points in the set
     */
    public int size() {
        return treeset.size();
    }

    /**
     * Adds the point to the set (if it is not already in the set).
     *
     * @param p the point to be added
     * @throws IllegalArgumentException if the point is null
     */
    public void insert(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        treeset.add(p);
    }

    /**
     * Checks if the set contains the specified point.
     *
     * @param p the point to be checked
     * @return {@code true} if the set contains the point, {@code false} otherwise
     * @throws IllegalArgumentException if the point is null
     */
    public boolean contains(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        return treeset.contains(p);
    }

    /**
     * Draws all points to standard draw.
     */
    public void draw() {
        StdDraw.setXscale(0, 1);
        StdDraw.setYscale(0, 1);
        // StdDraw.setPenRadius(0.01);
        StdDraw.setPenColor(StdDraw.BLACK);
        for (Point2D p : treeset) {
            p.draw();
        }
    }

    /**
     * Returns all points that are inside the rectangle (or on the boundary).
     *
     * @param rect the rectangle
     * @return an iterable of points inside the rectangle
     * @throws IllegalArgumentException if the rectangle is null
     */
    public Iterable<Point2D> range(RectHV rect) {
        if (rect == null) throw new IllegalArgumentException();
        LinkedList<Point2D> insideRect = new LinkedList<>();
        for (Point2D p : treeset) {
            if (rect.contains(p)) {
                insideRect.add(p);
            }
        }
        return insideRect;
    }

    /**
     * Finds a nearest neighbor in the set to point p; returns null if the set is empty.
     *
     * @param p the point to find the nearest neighbor to
     * @return the nearest neighbor in the set to point p, or null if the set is empty
     * @throws IllegalArgumentException if the point is null
     */
    public Point2D nearest(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        if (treeset.isEmpty()) return null;
        Point2D nearest = treeset.first();
        for (Point2D point : treeset) {
            if (p.distanceSquaredTo(point) < p.distanceSquaredTo(nearest)) {
                nearest = point;
            }
        }
        return nearest;
    }

    /**
     * Unit testing of the methods (optional).
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        PointSET set = new PointSET();

        // Insert points
        set.insert(new Point2D(0.7, 0.2));
        set.insert(new Point2D(0.5, 0.4));
        set.insert(new Point2D(0.2, 0.3));
        set.insert(new Point2D(0.4, 0.7));
        set.insert(new Point2D(0.9, 0.6));

        // Create a rectangle
        RectHV rect = new RectHV(0.15, 0.25, 0.5, 0.45);
        StdDraw.setPenColor(StdDraw.RED);
        rect.draw();

        // Draw all points in the set
        set.draw();

        // Print points inside the rectangle
        StdOut.println("Points inside the rectangle");
        for (Point2D p : set.range(rect)) {
            StdOut.println(p);
        }

        // Find and print the closest point to (0, 0)
        StdOut.println("Closest point to (0, 0):");
        Point2D closest = set.nearest(new Point2D(0, 0));
        StdOut.println(closest);
    }
}