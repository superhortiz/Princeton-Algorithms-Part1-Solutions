class Point:
    def __init__(self, x, y):
        """
        Initializes a new point with given x and y coordinates.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def slopeTo(self, that):
        """
        Calculates the slope between this point and the specified point.

        The slope is defined as (y1 - y0) / (x1 - x0). For special cases:
        - If the points are equal, the slope is negative infinity.
        - If the line segment is vertical (same x-coordinates), the slope is positive infinity.

        Args:
            that (Point): The other point.

        Returns:
            float: The slope between this point and the specified point.
        """
        if self.x == that.x and self.y == that.y:
            return float("-inf")
        elif self.x == that.x:
            return float("inf")
        else:
            return (that.y - self.y) / (that.x - self.x)

    def __lt__(self, that):
        """
        Compares two points by y-coordinate, breaking ties by x-coordinate.

        Args:
            that (Point): The other point.

        Returns:
            bool: True if this point is less than the argument point; False otherwise.
        """
        return self.y < that.y or (self.y == that.y and self.x < that.x)

    def __eq__(self, that):
        """
        Checks if two points are equal (have the same coordinates).

        Args:
            that (Point): The other point.

        Returns:
            bool: True if the points are equal; False otherwise.
        """
        return self.x == that.x and self.y == that.y

    def slopeOrder(self):
        """
        Returns a comparator function for sorting points by slope.
        The comparator compares points based on the slope they make with this point.

        Returns:
            callable: A comparator function.
        """
        def compare(that):
            slopeToThat = self.slopeTo(that)
            return slopeToThat
        return compare

    def __str__(self):
        """
        Returns a string representation of this point.

        Returns:
            str: A string representation of this point.
        """
        return f'({self.x}, {self.y})'