import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BruteCollinearPoints {
    private List<LineSegment> segments = new ArrayList<>();

    /**
     * Finds all line segments containing 4 points using the brute-force approach.
     * Checks all combinations of 4 points and identifies collinear segments.
     *
     * @param points an array of points
     * @throws IllegalArgumentException if the input array or any point in it is null
     */
    public BruteCollinearPoints(Point[] points) {
        if (points == null) {
            throw new IllegalArgumentException();
        }

        int n = points.length;

        for (int p = 0; p < n; p++) {
            if (points[p] == null) throw new IllegalArgumentException();
            for (int q = p + 1; q < n; q++) {
                if (points[q] == null || points[p].slopeTo(points[q]) == Double.NEGATIVE_INFINITY) {
                    throw new IllegalArgumentException();
                }
                for (int r = q + 1; r < n; r++) {
                    if (points[r] == null
                            || points[q].slopeTo(points[r]) == Double.NEGATIVE_INFINITY) {
                        throw new IllegalArgumentException();
                    }
                    if (points[p].slopeTo(points[q]) == points[p].slopeTo(points[r])) {
                        for (int s = r + 1; s < n; s++) {
                            if (points[s] == null
                                    || points[r].slopeTo(points[s]) == Double.NEGATIVE_INFINITY) {
                                throw new IllegalArgumentException();
                            }
                            if (points[p].slopeTo(points[q]) == points[p].slopeTo(points[s])) {
                                Point[] segment = { points[p], points[q], points[r], points[s] };
                                Arrays.sort(segment);
                                segments.add(new LineSegment(segment[0], segment[3]));
                            }
                        }
                    }
                }
            }
        }
    }

    /**
     * Returns the number of line segments found.
     *
     * @return the number of line segments
     */
    public int numberOfSegments() {
        return segments.size();
    }

    /**
     * Returns an array of line segments found.
     *
     * @return an array of line segments
     */
    public LineSegment[] segments() {
        return segments.toArray(new LineSegment[0]);
    }

    /**
     * Reads points from a file, finds collinear segments, and displays them.
     *
     * @param args command-line arguments (input file containing points)
     */
    public static void main(String[] args) {

        // read the n points from a file
        In in = new In(args[0]);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        // draw the points
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        for (Point p : points) {
            p.draw();
        }
        StdDraw.show();

        // print and draw the line segments
        FastCollinearPoints collinear = new FastCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
        StdDraw.show();
    }
}
