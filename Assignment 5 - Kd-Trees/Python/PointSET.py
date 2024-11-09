from matplotlib import pyplot as plt
from Point2D import Point2D
from RectHV import RectHV

class PointSET:
    """
    A class representing a set of 2-dimensional points.

    Expected Performance:
    - Insertion: O(1) on average, as points are appended to a list.
    - Contains: O(N) in the worst case, where N is the number of points, since it requires a linear search.
    - Nearest Neighbor Search: O(N) in the worst case, as it involves checking the distance to each point.
    - Range Search: O(N) in the worst case, as it involves checking each point to see if it lies within the given rectangle.
    """

    def __init__(self):
        """
        Initialize an empty set of points.
        """
        self.set = []

    def isEmpty(self):
        """
        Check if the set of points is empty.

        Returns:
            bool: True if the set is empty, False otherwise.
        """
        return not self.set

    def size(self):
        """
        Get the number of points in the set.

        Returns:
            int: The number of points in the set.
        """
        return len(self.set)

    def insert(self, point):
        """
        Insert a new point into the set.

        Args:
            point (Point2D): The 2-dimensional point to be inserted.

        Raises:
            ValueError: If the point is None.
        """
        if point is None:
            raise ValueError("Invalid argument")

        self.set.append(point)

    def get(self, point):
        """
        Retrieve a point from the set.

        Args:
            point (Point2D): The 2-dimensional point to be retrieved.

        Raises:
            ValueError: If the point is None.

        Returns:
            Point2D: The point if found, None otherwise.
        """
        if point is None:
            raise ValueError("Invalid argument")

        if point in self.set:
            return point

        return None

    def contains(self, point):
        """
        Check if a point exists in the set.

        Args:
            point (Point2D): The 2-dimensional point to be checked.

        Raises:
            ValueError: If the point is None.

        Returns:
            bool: True if the point exists in the set, False otherwise.
        """
        if point is None:
            raise ValueError("Invalid argument")

        return point in self.set

    def draw(self):
        """
        Draw all points in the set.

        Sets up the plot limits and draws each point.
        """
        plt.xlim(0, 1)
        plt.ylim(0, 1)

        for point in self.set:
            point.draw()

        plt.show()

    def range(self, rect):
        """
        Find all points in the set that lie within a given rectangle.

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

        for point in self.set:
            if rect.contains(point):
                insideRec.append(point)

        return insideRec

    def nearest(self, point):
        """
        Find the nearest neighbor to a given point in the set.

        Args:
            point (Point2D): The 2-dimensional point to find the nearest neighbor for.

        Raises:
            ValueError: If the point is None.

        Returns:
            Point2D: The nearest point in the set to the given point.
        """
        if point is None:
            raise ValueError("Invalid argument")

        if self.isEmpty():
            return None

        champion = self.set[0]
        
        for p in self.set:
            if p.distanceSquaredTo(point) < champion.distanceSquaredTo(point):
                champion = p
        return champion



# Example usage
if __name__ == "__main__":
    # Create an instance of PointSET
    pointSet = PointSET()

    # Insert points
    points = [
    Point2D(0.1, 0.3), Point2D(0.5, 0.6), Point2D(0.8, 0.9), Point2D(0.4, 0.2),
    Point2D(0.1, 0.4), Point2D(0.7, 0.4), Point2D(0.3, 0.8), Point2D(0.6, 0.1),
    Point2D(0.9, 0.7), Point2D(0.2, 0.5), Point2D(0.5, 0.3), Point2D(0.8, 0.2)]

    for point in points:
        pointSet.insert(point)

    # Check number of elements in the tree
    print("Number of elements in the tree = ", pointSet.size())

    # Check if the tree contains a point
    p = Point2D(0.7, 0.2)
    print(f"Does the tree countain the point {p}? {pointSet.contains(p)}")

    # Check nearest point
    point = Point2D(0.3, 0.35)
    print(f"Closest point to {point}: {pointSet.nearest(point)}")

    # Check points inside a rectangle
    rect = RectHV(0.15, 0.15, 0.75, 0.75)
    pointsInRect = pointSet.range(rect)
    print("Points inside the rectangle:", *[p for p in sorted(pointsInRect)])

    # Draw the elements
    rect.draw()
    point.draw('red')
    pointSet.draw()