import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FastCollinearPoints {
    private List<LineSegment> segments = new ArrayList<>();

    /**
     * Finds all line segments containing 4 or more collinear points using the fast algorithm.
     * The algorithm sorts the points by natural order and then examines slopes
     * to identify collinear segments.
     *
     * @param points an array of points
     * @throws IllegalArgumentException if the input array or any point in it is null,
     * or if the array contains duplicate points
     */
    public FastCollinearPoints(Point[] points) {
        if (points == null) {
            throw new IllegalArgumentException();
        }

        int n = points.length;
        Point[] clone = new Point[n];

        for (int i = 0; i < n; i++) {
            if (points[i] == null) {
                throw new IllegalArgumentException();
            }
            else {
                for (int j = i + 1; j < n; j++) {
                    if (points[j] == null || points[i].compareTo(points[j]) == 0) {
                        throw new IllegalArgumentException();
                    }
                }
                clone[i] = points[i];
            }
        }

        Arrays.sort(clone);

        for (int p = 0; p < n; p++) {
            Point[] copy = clone.clone();
            Arrays.sort(copy, points[p].slopeOrder());
            int q = 1;
            while (q < n) {
                int start = q;
                while (q < n && points[p].slopeTo(copy[q - 1]) == points[p].slopeTo(copy[q])) {
                    q++;
                }
                if (q - start >= 2 && points[p].compareTo(copy[start - 1]) < 0) {
                    segments.add(new LineSegment(points[p], copy[q - 1]));
                }
                q++;
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
