import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

import java.util.Arrays;
import java.util.Comparator;

public class Point implements Comparable<Point> {

    private final int x;     // x-coordinate of this point
    private final int y;     // y-coordinate of this point

    /**
     * Initializes a new point.
     *
     * @param x the <em>x</em>-coordinate of the point
     * @param y the <em>y</em>-coordinate of the point
     */
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Draws this point to standard draw.
     */
    public void draw() {
        StdDraw.point(x, y);
    }

    /**
     * Draws the line segment between this point and the specified point
     * to standard draw.
     *
     * @param that the other point
     */
    public void drawTo(Point that) {
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    /**
     * Returns the slope between this point and the specified point.
     * The slope is defined as (y1 - y0) / (x1 - x0).
     * If the line segment connecting the two points is horizontal, the slope is +0.0.
     * If the line segment is vertical, the slope is Double.POSITIVE_INFINITY.
     * If the points are equal, the slope is Double.NEGATIVE_INFINITY.
     *
     * @param that the other point
     * @return the slope between this point and the specified point
     */
    public double slopeTo(Point that) {
        /* YOUR CODE HERE */
        if (this.x == that.x && this.y == that.y) {
            return Double.NEGATIVE_INFINITY;
        }
        if (this.x == that.x) {
            return Double.POSITIVE_INFINITY;
        }
        if (this.y == that.y) {
            return 0;
        }
        else {
            return (double) (that.y - this.y) / (that.x - this.x);
        }
    }

    /**
     * Compares two points by y-coordinate, breaking ties by x-coordinate.
     * Formally, the invoking point (x0, y0) is less than the argument point
     * (x1, y1) if and only if either y0 < y1 or if y0 = y1 and x0 < x1.
     *
     * @param that the other point
     * @return the value <tt>0</tt> if this point is equal to the argument
     * point (x0 = x1 and y0 = y1);
     * a negative integer if this point is less than the argument
     * point; and a positive integer if this point is greater than the
     * argument point
     */
    public int compareTo(Point that) {
        if (this.y < that.y || (this.y == that.y && this.x < that.x)) {
            return -1;
        }
        else if (this.y > that.y || (this.y == that.y && this.x > that.x)) {
            return 1;
        }
        return 0;
    }

    /**
     * Compares two points by the slope they make with this point.
     * The slope is defined as in the slopeTo() method.
     *
     * @return the Comparator that defines this ordering on points
     */
    public Comparator<Point> slopeOrder() {
        return new Comparator<Point>() {
            public int compare(Point a, Point b) {
                double slopeA = slopeTo(a);
                double slopeB = slopeTo(b);
                if (slopeA < slopeB) return -1;
                else if (slopeA > slopeB) return 1;
                return 0;
            }
        };
    }

    /**
     * Returns a string representation of this point.
     * This method is provide for debugging;
     * your program should not rely on the format of the string representation.
     *
     * @return a string representation of this point
     */
    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    /**
     * Unit tests the Point data type.
     */
    public static void main(String[] args) {
        Point[] points = {
                new Point(0, 0),
                new Point(7, 6),
                new Point(7, 1),
                new Point(0, 6)
        };

        // Sort by y-coordinate first
        Arrays.sort(points);
        StdOut.println("Points sorted by y-coordinate:");
        for (Point p : points) {
            StdOut.println(p.toString());
        }

        // Then sort by slope
        Arrays.sort(points, points[0].slopeOrder());
        StdOut.println("Points sorted by slopes:");
        for (Point p : points) {
            StdOut.println(p.toString());
        }
    }
}