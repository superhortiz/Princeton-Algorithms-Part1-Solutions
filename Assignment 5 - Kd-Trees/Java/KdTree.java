import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

import java.util.LinkedList;

public class KdTree {
    private TreeNode root;

    /**
     * Initializes an empty K-D Tree.
     */
    public KdTree() {
        root = null;
    }

    /**
     * Nested class representing a node in the KD Tree.
     */
    private class TreeNode {
        private Point2D point; // The point stored in this node
        private int count; // Number of nodes in the subtree rooted at this node
        private TreeNode left, right; // Left and right children

        /**
         * Constructs a TreeNode with the specified point and count.
         *
         * @param point the point to be stored in this node
         * @param count the number of nodes in the subtree rooted at this node
         */
        public TreeNode(Point2D point, int count) {
            this.point = point;
            this.count = count;
            this.left = null;
            this.right = null;
        }
    }

    /**
     * Checks if the set is empty.
     *
     * @return {@code true} if the set is empty, {@code false} otherwise
     */
    public boolean isEmpty() {
        return root == null;
    }

    /**
     * Returns the number of points in the set.
     *
     * @return the number of points in the set
     */
    public int size() {
        return size(root);
    }

    /**
     * Recursively calculates the size of the subtree rooted at {@code node}.
     *
     * @param node the root of the subtree
     * @return the total number of nodes in the subtree
     */
    private int size(TreeNode node) {
        if (node == null) return 0;
        return node.count;
    }

    /**
     * Adds the point to the set (if it is not already in the set).
     *
     * @param p the point to be added
     * @throws IllegalArgumentException if the point is null
     */
    public void insert(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        root = insert(root, p, 0);
    }

    /**
     * Helper method to insert a point into the subtree rooted at a given node.
     *
     * @param node  the root of the subtree
     * @param p     the point to be added
     * @param level the current level in the tree
     * @return the updated root of the subtree
     */
    private TreeNode insert(TreeNode node, Point2D p, int level) {
        if (node == null) return new TreeNode(p, 1);
        double key, keyNode, secondKey, secondKeyNode;
        if (level % 2 == 0) {
            key = p.x();
            keyNode = node.point.x();
            secondKey = p.y();
            secondKeyNode = node.point.y();
        }
        else {
            key = p.y();
            keyNode = node.point.y();
            secondKey = p.x();
            secondKeyNode = node.point.x();
        }
        if (key < keyNode || key == keyNode && secondKey != secondKeyNode) {
            node.left = insert(node.left, p, level + 1);
        }
        else if (key > keyNode) {
            node.right = insert(node.right, p, level + 1);
        }

        else if (key == keyNode && secondKey == secondKeyNode) {
            node.point = p;
        }

        node.count = 1 + size(node.left) + size(node.right);
        return node;
    }

    /**
     * Searches for a point in the K-D Tree and returns it if found.
     *
     * @param p the point to search for
     * @return the point if found, null otherwise
     */
    private Point2D get(Point2D p) {
        TreeNode node = root;
        int level = 0;

        while (node != null) {
            double key, keyNode, secondKey, secondKeyNode;
            if (level % 2 == 0) {
                key = p.x();
                keyNode = node.point.x();
                secondKey = p.y();
                secondKeyNode = node.point.y();
            }
            else {
                key = p.y();
                keyNode = node.point.y();
                secondKey = p.x();
                secondKeyNode = node.point.x();
            }
            if (key < keyNode || key == keyNode && secondKey != secondKeyNode) {
                node = node.left;
            }
            else if (key > keyNode) {
                node = node.right;
            }
            else if (key == keyNode && secondKey == secondKeyNode) {
                return node.point;
            }
            level++;
        }
        return null;
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
        return get(p) != null;
    }

    /**
     * Draws all points to standard draw.
     */
    public void draw() {
        StdDraw.setXscale(0, 1);
        StdDraw.setYscale(0, 1);
        draw(root, 0, new RectHV(0, 0, 1, 1));
    }

    /**
     * Helper method to draw all points in the subtree rooted at a given node.
     *
     * @param node  the root of the subtree
     * @param level the current level in the tree
     * @param curr  the current rectangle representing the node's region
     */
    private void draw(TreeNode node, int level, RectHV curr) {
        if (node == null) return;
        StdDraw.setPenRadius(0.015);
        StdDraw.setPenColor(StdDraw.BLACK);
        node.point.draw();
        StdDraw.setPenRadius(0.002);
        double x = node.point.x();
        double y = node.point.y();
        RectHV newCurrLeft, newCurrRight;

        if (level % 2 == 0) {
            StdDraw.setPenColor(StdDraw.RED);
            newCurrLeft = new RectHV(curr.xmin(), curr.ymin(), x, curr.ymax());
            newCurrRight = new RectHV(x, curr.ymin(), curr.xmax(), curr.ymax());
            StdDraw.line(x, curr.ymin(), x, curr.ymax());
        }
        else {
            StdDraw.setPenColor(StdDraw.BLUE);
            newCurrLeft = new RectHV(curr.xmin(), curr.ymin(), curr.xmax(), y);
            newCurrRight = new RectHV(curr.xmin(), y, curr.xmax(), curr.ymax());
            StdDraw.line(curr.xmin(), y, curr.xmax(), y);
        }
        draw(node.left, level + 1, newCurrLeft);
        draw(node.right, level + 1, newCurrRight);
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
        LinkedList<Point2D> insideRec = new LinkedList<>();
        range(root, rect, insideRec, 0, new RectHV(0, 0, 1, 1));
        return insideRec;
    }

    /**
     * Recursively finds all points in the subtree rooted at {@code node} that intersect with
     * {@code rect}.
     *
     * @param node      the root of the subtree
     * @param rect      the rectangle to search in
     * @param insideRec the list of points inside the rectangle
     * @param level     the current level in the tree
     * @param curr      the current rectangle representing the node's region
     */
    private void range(TreeNode node, RectHV rect, LinkedList<Point2D> insideRec, int level,
                       RectHV curr) {
        if (node == null) return;
        if (rect.contains(node.point)) {
            insideRec.add(node.point);
        }
        double x = node.point.x();
        double y = node.point.y();
        RectHV newCurrLeft, newCurrRight;

        if (level % 2 == 0) {
            newCurrLeft = new RectHV(curr.xmin(), curr.ymin(), x, curr.ymax());
            newCurrRight = new RectHV(x, curr.ymin(), curr.xmax(), curr.ymax());
        }
        else {
            newCurrLeft = new RectHV(curr.xmin(), curr.ymin(), curr.xmax(), y);
            newCurrRight = new RectHV(curr.xmin(), y, curr.xmax(), curr.ymax());
        }

        if (rect.intersects(newCurrLeft)) {
            range(node.left, rect, insideRec, level + 1, newCurrLeft);
        }

        if (rect.intersects(newCurrRight)) {
            range(node.right, rect, insideRec, level + 1, newCurrRight);
        }
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
        if (isEmpty()) return null;
        Champion champion = new Champion(root.point);
        nearest(root, p, 0, new RectHV(0, 0, 1, 1), champion);
        return champion.point;
    }

    /**
     * Nested class to keep track of the current nearest point (champion).
     */
    private class Champion {
        Point2D point;

        private Champion(Point2D point) {
            this.point = point;
        }
    }

    /**
     * Helper method to find the nearest neighbor in the subtree rooted at a given node.
     *
     * @param node     the root of the subtree
     * @param p        the point to find the nearest neighbor to
     * @param level    the current level in the tree
     * @param space    the current rectangle representing the node's region
     * @param champion the current nearest point
     */
    private void nearest(TreeNode node, Point2D p, int level, RectHV space, Champion champion) {
        if (node == null || champion.point.distanceSquaredTo(p) < space.distanceSquaredTo(p))
            return;
        if (p.distanceSquaredTo(node.point) < p.distanceSquaredTo(champion.point)) {
            champion.point = node.point;
        }
        double x = node.point.x();
        double y = node.point.y();
        RectHV leftSpace, rightSpace;

        if (level % 2 == 0) {
            leftSpace = new RectHV(space.xmin(), space.ymin(), x, space.ymax());
            rightSpace = new RectHV(x, space.ymin(), space.xmax(), space.ymax());
        }
        else {
            leftSpace = new RectHV(space.xmin(), space.ymin(), space.xmax(), y);
            rightSpace = new RectHV(space.xmin(), y, space.xmax(), space.ymax());
        }

        boolean goLeft;
        if (leftSpace.contains(p)) goLeft = true;
        else if (rightSpace.contains(p)) goLeft = false;
        else if (leftSpace.distanceSquaredTo(p) < rightSpace.distanceSquaredTo(p)) goLeft = true;
        else goLeft = false;

        if (goLeft) {
            nearest(node.left, p, level + 1, leftSpace, champion);
            nearest(node.right, p, level + 1, rightSpace, champion);
        }
        else {
            nearest(node.right, p, level + 1, rightSpace, champion);
            nearest(node.left, p, level + 1, leftSpace, champion);
        }
    }

    /**
     * Unit testing of the methods.
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        // Create an instance of KdTree
        KdTree kdt = new KdTree();

        // Insert points
        kdt.insert(new Point2D(0.7, 0.2));
        kdt.insert(new Point2D(0.5, 0.4));
        kdt.insert(new Point2D(0.2, 0.3));
        kdt.insert(new Point2D(0.4, 0.7));
        kdt.insert(new Point2D(0.9, 0.6));

        // Create a rectangle
        RectHV rect = new RectHV(0.2, 0.2, 0.4, 0.5);

        // Check number of elements in the tree
        StdOut.println("Number of elements in the tree = " + kdt.size());

        // Check if the tree contains a point
        Point2D p = new Point2D(0.76, 0.56);
        StdOut.println("Does the tree countain the point " + p + "? " + kdt.contains(p));

        // Draw the points in the tree and the rectangle
        kdt.draw();
        StdDraw.setPenColor(StdDraw.CYAN);
        rect.draw();

        // Check points inside the rectangle
        StdOut.println("Points inside the rectangle:");
        for (Point2D point : kdt.range(rect)) {
            StdOut.println(point);
        }

        // Check the nearest neighbor in the tree to point p
        Point2D point2 = new Point2D(0.1, 0.3);
        StdOut.println("Closest point to " + point2 + ": " + kdt.nearest(point2));
        StdDraw.setPenRadius(0.015);
        StdDraw.setPenColor(StdDraw.RED);
        point2.draw();
    }
}