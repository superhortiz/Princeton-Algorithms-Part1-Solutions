import matplotlib.pyplot as plt

class Point2D:
    """
    A class to represent a point in 2D space.
    
    Attributes:
        _x (float): The x-coordinate of the point.
        _y (float): The y-coordinate of the point.
    """

    def __init__(self, x, y):
        """
        Initialize the Point2D object with x and y coordinates.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self._x = x
        self._y = y

    def x(self):
        """
        Get the x-coordinate of the point.

        Returns:
            float: The x-coordinate of the point.
        """
        return self._x

    def y(self):
        """
        Get the y-coordinate of the point.

        Returns:
            float: The y-coordinate of the point.
        """
        return self._y

    def distanceTo(self, that):
        """
        Calculate the Euclidean distance to another point.

        Args:
            that (Point2D): Another point to which the distance is calculated.

        Returns:
            float: The Euclidean distance to the other point.
        """
        return self.distanceSquaredTo(that) ** 0.5

    def distanceSquaredTo(self, that):
        """
        Calculate the squared Euclidean distance to another point.

        Args:
            that (Point2D): Another point to which the squared distance is calculated.

        Returns:
            float: The squared Euclidean distance to the other point.
        """
        return (self.x() - that.x()) ** 2 + (self.y() - that.y()) ** 2

    def __eq__(self, that):
        """
        Check if this point is equal to another point.

        Args:
            that (Point2D): Another point to compare with.

        Returns:
            bool: True if the points are equal, False otherwise.
        """
        if that is None:
            return False

        return self.x() == that.x() and self.y() == that.y()

    def __lt__(self, that):
        """
        Check if this point is less than another point.

        Args:
            that (Point2D): Another point to compare with.

        Returns:
            bool: True if this point is less than the other point, False otherwise.
        """
        if self.x() != that.x():
            return self.x() < that.x()

        return self.y() < that.y()

    def draw(self, color = 'black'):
        """
        Draws the point represented by this object on a matplotlib plot.

        The point is plotted as a black circle ('o') at the coordinates
        returned by the x() and y() methods of this object.

        Args:
            None

        Returns:
            None
        """
        plt.plot(self.x(), self.y(), 'o', color = color)

    def __str__(self):
        """
        Return a string representation of the point.

        Returns:
            str: A string representation of the point in the format (x, y).
        """
        return f"({self.x()}, {self.y()})"


# Example usage
if __name__ == "__main__":
    a = Point2D(0, 0)
    b = Point2D(1, 1)
    
    print("Point a:", a)
    print("Distance from point a to point b:", a.distanceTo(b))
    print("Is point a equal to point b?", a == b)
    a.draw()
    b.draw()
    plt.show()