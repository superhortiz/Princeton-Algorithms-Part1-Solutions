from matplotlib import pyplot as plt
from Point2D import Point2D
from RectHV import RectHV

class KdTree:
    """
    A class representing a 2-dimensional k-d tree (KdTree) for organizing points in a 2D space.

    Expected Performance:
    - Insertion: O(log N) on average, where N is the number of points, assuming the tree is balanced.
    - Contains: O(log N) on average, due to the binary search nature of the tree.
    - Nearest Neighbor Search:
        - Typical case: O(log N).
        - Worst case (even if the tree is balanced): O(N).
    - Range Search:
        - Typical case: O(R + log N), where R is the number of points in the range.
        - Worst case (assuming the tree is balanced): O(R + √N).
    """

    def __init__(self):
        """
        Initialize an empty 2D KdTree.
        """
        self.root = None

    class TreeNode:
        """
        A class representing a node in the 2D KdTree.
        """
        def __init__(self, point, count):
            """
            Initialize a TreeNode.

            Args:
                point (Point2D): The 2-dimensional point stored in this node.
                count (int): The size of the subtree rooted at this node.
            """
            self.left = None
            self.right = None
            self.point = point
            self.count = count

    def isEmpty(self):
        """
        Check if the 2D KdTree is empty.

        Returns:
            bool: True if the tree is empty, False otherwise.
        """
        return self.root == None

    def size(self):
        """
        Get the number of nodes in the 2D KdTree.

        Returns:
            int: The total number of nodes in the tree.
        """
        return self._size(self.root)

    def _size(self, x):
        """
        Get the number of nodes in the 2D KdTree.

        Returns:
            int: The total number of nodes in the tree.
        """
        if x is None:
            return 0
        return x.count

    def insert(self, point):
        """
        Insert a new point into the 2D KdTree.

        Args:
            point (Point2D): The 2-dimensional point to be inserted.

        Raises:
            ValueError: If the point is None.
        """
        if point is None:
            raise ValueError("Invalid argument")

        self.root = self._insert(self.root, point, level = 0)

    def _insert(self, node, newPoint, level):
        """
        Recursively insert a new point into the subtree rooted at the given node.

        Args:
            node (TreeNode): The root of the subtree.
            newPoint (Point2D): The 2-dimensional point to be inserted.
            level (int): The current level in the tree.

        Returns:
            TreeNode: The updated subtree root.
        """
        if node is None:
            return KdTree.TreeNode(newPoint, 1)

        if level % 2 == 0:
            key = newPoint.x()
            keyNode = node.point.x()
            secondKey = newPoint.y()
            secondKeyNode = node.point.y()

        else:
            key = newPoint.y()
            keyNode = node.point.y()
            secondKey = newPoint.x()
            secondKeyNode = node.point.x()

        if key < keyNode or (key == keyNode and secondKey != secondKeyNode):
            node.left = self._insert(node.left, newPoint, level + 1)
        elif key > keyNode:
            node.right = self._insert(node.right, newPoint, level + 1)
        elif key == keyNode and secondKey == secondKeyNode:
            node.point = point

        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def get(self, point):
        """
        Retrieve a point from the 2D KdTree.

        Args:
            point (Point2D): The 2-dimensional point to be retrieved.

        Returns:
            Point2D: The point if found, None otherwise.
        """
        node = self.root
        level = 0

        while node:
            if level % 2 == 0:
                key = point.x()
                keyNode = node.point.x()
                secondKey = point.y()
                secondKeyNode = node.point.y()
            else:
                key = point.y()
                keyNode = node.point.y()
                secondKey = point.x()
                secondKeyNode = node.point.x()

            if key < keyNode or (key == keyNode and secondKey != secondKeyNode):
                node = node.left
            elif key > keyNode:
                node = node.right
            elif key == keyNode and secondKey == secondKeyNode:
                return node.point
            level += 1
        return None

    def contains(self, point):
        """
        Check if a point exists in the 2D KdTree.

        Args:
            point (Point2D): The 2-dimensional point to be checked.

        Raises:
            ValueError: If the point is None.

        Returns:
            bool: True if the point exists in the tree, False otherwise.
        """
        if point is None:
            raise ValueError("Invalid argument")
        return not self.get(point) is None

    def draw(self):
        """
        Draw the 2D KdTree.

        Sets up the plot limits and initiates the recursive drawing process.
        """
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        self._draw(self.root, 0, RectHV(0, 0, 1, 1))
        plt.show()

    def _draw(self, node, level, curr):
        """
        Recursively draw the 2D KdTree.

        Args:
            node (TreeNode): The current node in the tree.
            level (int): The current level in the tree.
            curr (RectHV): The current rectangle representing the node's region.

        Returns:
            None
        """
        if node is None:
            return

        node.point.draw()
        x, y = node.point.x(), node.point.y()

        if level % 2 == 0:
            currLeft = RectHV(curr.xmin(), curr.ymin(), x, curr.ymax())
            currRight = RectHV(x, curr.ymin(), curr.xmax(), curr.ymax())
            plt.plot([x, x], [curr.ymin(), curr.ymax()], 'r-')

        else:
            currLeft = RectHV(curr.xmin(), curr.ymin(), curr.xmax(), y)
            currRight = RectHV(curr.xmin(), y, curr.xmax(), curr.ymax())
            plt.plot([curr.xmin(), curr.xmax()], [y, y], 'b-')

        self._draw(node.left, level + 1, currLeft)
        self._draw(node.right, level + 1, currRight)

    def range(self, rect):
        """
        Find all points in the 2D KdTree that lie within a given rectangle.

        Args:
            rect (RectHV): The rectangle to search within.

        Raises:
            ValueError: If the rectangle is None.

        Returns:
            list: A list of points within the given rectangle.
        """
        if rect is None:
            raise ValueError("Invalid argument")

        insideRec = []
        self._range(self.root, rect, insideRec, 0, RectHV(0, 0, 1, 1))
        return insideRec

    def _range(self, node, rect, insideRec, level, curr):
        """
        Recursively find all points in the subtree rooted at the given node that lie within a given rectangle.

        Args:
            node (TreeNode): The current node in the tree.
            rect (RectHV): The rectangle to search within.
            insideRec (list): The list to store points found within the rectangle.
            level (int): The current level in the tree.
            curr (RectHV): The current rectangle representing the node's region.

        Returns:
            None
        """
        if node is None:
            return

        if rect.contains(node.point):
            insideRec.append(node.point)

        x, y = node.point.x(), node.point.y()

        if level % 2 == 0:
            currLeft = RectHV(curr.xmin(), curr.ymin(), x, curr.ymax())
            currRight = RectHV(x, curr.ymin(), curr.xmax(), curr.ymax())

        else:
            currLeft = RectHV(curr.xmin(), curr.ymin(), curr.xmax(), y)
            currRight = RectHV(curr.xmin(), y, curr.xmax(), curr.ymax())

        if rect.intersects(currLeft):
            self._range(node.left, rect, insideRec, level + 1, currLeft)
        
        if rect.intersects(currRight):
            self._range(node.right, rect, insideRec, level + 1, currRight)

    def nearest(self, point):
        """
        Find the nearest neighbor to a given point in the 2D KdTree.

        Args:
            point (Point2D): The 2-dimensional point to find the nearest neighbor for.

        Raises:
            ValueError: If the point is None.

        Returns:
            Point2D: The nearest point in the tree to the given point.
        """
        if point is None:
            raise ValueError("Invalid argument")

        if self.isEmpty():
            return None

        champion = [self.root.point]
        self._nearest(self.root, point, 0, RectHV(0, 0, 1, 1), champion)
        return champion[0]

    def _nearest(self, node, p, level, curr, champion):
        """
        Recursively find the nearest neighbor to a given point in the subtree rooted at the given node.

        Args:
            node (TreeNode): The current node in the tree.
            p (Point2D): The point to find the nearest neighbor for.
            level (int): The current level in the tree.
            curr (RectHV): The current rectangle representing the node's region.
            champion (list): A list containing the current nearest point.

        Returns:
            None
        """
        if node is None or champion[0].distanceSquaredTo(p) < curr.distanceSquaredTo(p):
            return  # Prune strategy

        if p.distanceSquaredTo(node.point) < p.distanceSquaredTo(champion[0]):
            champion[0] = node.point

        x, y = node.point.x(), node.point.y()

        if level % 2 == 0:
            currLeft = RectHV(curr.xmin(), curr.ymin(), x, curr.ymax())
            currRight = RectHV(x, curr.ymin(), curr.xmax(), curr.ymax())

        else:
            currLeft = RectHV(curr.xmin(), curr.ymin(), curr.xmax(), y)
            currRight = RectHV(curr.xmin(), y, curr.xmax(), curr.ymax())

        goLeft = False

        if currLeft.contains(p):
            goLeft = True
        elif currRight.contains(p):
            goLeft = False
        elif currLeft.distanceSquaredTo(p) < currRight.distanceSquaredTo(p):
            goLeft = True
        else:
            goLeft = False

        if goLeft:
            self._nearest(node.left, p, level + 1, currLeft, champion)
            self._nearest(node.right, p, level + 1, currRight, champion)

        else:
            self._nearest(node.right, p, level + 1, currRight, champion)
            self._nearest(node.left, p, level + 1, currLeft, champion)

    def print_tree(self):
        """
        Print the 2D KdTree in a structured format.
        """
        self._print_tree(self.root)

    def _print_tree(self, node = None, level = 0, prefix = "Root: "):
        """
        Recursively print the 2D KdTree in a structured format.

        Args:
            node (TreeNode): The current node in the tree.
            level (int): The current level in the tree.
            prefix (str): The prefix to print before the node's point.

        Returns:
            None
        """
        if node is not None:
            print(" " * (level * 4) + prefix + f"({node.point})")
            if node.left:
                self._print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self._print_tree(node.right, level + 1, "R--- ")


# Example usage
if __name__ == "__main__":
    # Create an instance of KdTree
    kdt = KdTree()

    # Insert points
    points = [
    Point2D(0.1, 0.3), Point2D(0.5, 0.6), Point2D(0.8, 0.9), Point2D(0.4, 0.2),
    Point2D(0.1, 0.4), Point2D(0.7, 0.4), Point2D(0.3, 0.8), Point2D(0.6, 0.1),
    Point2D(0.9, 0.7), Point2D(0.2, 0.5), Point2D(0.5, 0.3), Point2D(0.8, 0.2)]

    for point in points:
        kdt.insert(point)

    # Check number of elements in the tree
    print("Number of elements in the tree = ", kdt.size())

    # Check if the tree contains a point
    p = Point2D(0.7, 0.2)
    print(f"Does the tree countain the point {p}? {kdt.contains(p)}")

    # Check nearest point
    point = Point2D(0.3, 0.35)
    print(f"Closest point to {point}: {kdt.nearest(point)}")

    # Check points inside a rectangle
    rect = RectHV(0.15, 0.15, 0.75, 0.75)
    pointsInRect = kdt.range(rect)
    print("Points inside the rectangle:", *[p for p in sorted(pointsInRect)])

    # Draw the elements
    rect.draw()
    point.draw('red')
    kdt.draw()