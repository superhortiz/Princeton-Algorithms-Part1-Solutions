import matplotlib.pyplot as plt

class RectHV:
    """
    Represents a 2D axis-aligned rectangle with coordinates (xmin, ymin) and (xmax, ymax).
    """

    def __init__(self, xmin, ymin, xmax, ymax):
        """
        Initializes a new rectangle with the specified coordinates.
        
        Args:
            xmin (float): The minimum x-coordinate.
            ymin (float): The minimum y-coordinate.
            xmax (float): The maximum x-coordinate.
            ymax (float): The maximum y-coordinate.
        
        Raises:
            ValueError: If xmax < xmin or ymax < ymin.
        """
        if xmax < xmin or ymax < ymin:
            raise ValueError("Invalid arguments")
        self._xmin = xmin
        self._ymin = ymin
        self._xmax = xmax
        self._ymax = ymax

    def xmin(self):
        """
        Returns the minimum x-coordinate of the rectangle.
        
        Returns:
            float: The minimum x-coordinate.
        """
        return self._xmin

    def ymin(self):
        """
        Returns the minimum y-coordinate of the rectangle.
        
        Returns:
            float: The minimum y-coordinate.
        """
        return self._ymin

    def xmax(self):
        """
        Returns the maximum x-coordinate of the rectangle.
        
        Returns:
            float: The maximum x-coordinate.
        """
        return self._xmax

    def ymax(self):
        """
        Returns the maximum y-coordinate of the rectangle.
        
        Returns:
            float: The maximum y-coordinate.
        """
        return self._ymax

    def contains(self, point):
        """
        Checks if the rectangle contains the given point.
        
        Args:
            point (Point): The point to check.
        
        Returns:
            bool: True if the rectangle contains the point, False otherwise.
        """
        return self.xmin() <= point.x() <= self.xmax() and self.ymin() <= point.y() <= self.ymax()

    def intersects(self, that):
        """
        Checks if the rectangle intersects with another rectangle.
        
        Args:
            that (RectHV): The other rectangle to check.
        
        Returns:
            bool: True if the rectangles intersect, False otherwise.
        """
        return self.xmax() >= that.xmin() and self.xmin() <= that.xmax() and self.ymax() >= that.ymin() and self.ymin() <= that.ymax()

    def distanceTo(self, point):
        """
        Computes the Euclidean distance from the rectangle to a point.
        
        Args:
            point (Point): The point to compute the distance to.
        
        Returns:
            float: The Euclidean distance to the point.
        """
        return self.distanceSquaredTo(point) ** 0.5

    def distanceSquaredTo(self, point):
        """
        Computes the square of the Euclidean distance from the rectangle to a point.
        
        Args:
            point (Point): The point to compute the distance to.
        
        Returns:
            float: The square of the Euclidean distance to the point.
        """
        dx, dy = 0, 0
        if point.x() > self.xmax():
            dx = point.x() - self.xmax()
        elif point.x() < self.xmin():
            dx = self.xmin() - point.x()
        if point.y() > self.ymax():
            dy = point.y() - self.ymax()
        elif point.y() < self.ymin():
            dy = self.ymin() - point.y()
        return dx ** 2 + dy ** 2

    def __eq__(self, that):
        """
        Checks if this rectangle is equal to another rectangle.
        
        Args:
            that (RectHV): The other rectangle to compare.
        
        Returns:
            bool: True if the rectangles are equal, False otherwise.
        """
        if that is None:
            return None

        return self.xmin() == that.xmin() and self.xmax() == that.xmax() and self.ymin() == that.ymin() and self.ymax() == that.ymax()

    def draw(self):
        x = [self.xmin(), self.xmax(), self.xmax(), self.xmin(), self.xmin()]
        y = [self.ymin(), self.ymin(), self.ymax(), self.ymax(), self.ymin()]
        plt.plot(x, y, 'g-')

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        
        Returns:
            str: The string representation of the rectangle.
        """
        return "[" + str(self.xmin()) + ", " + str(self.xmax()) + "] x [" + str(self.ymin()) + ", " + str(self.ymax()) + "]"


# Example usage
if __name__ == "__main__":
    from Point2D import Point2D

    a = RectHV(0, 0, 1, 1)
    b = RectHV(0.5, 0.5, 1.5, 1.5)
    p = Point2D(1.5, 1.5)
    
    print(f"Rectangle {a} contains the point {p}?", a.contains(p))
    print(f"Rectangle {a} intersects rectangle {b}?", a.intersects(b))
    print(f"Euclidean distance between the point {p} and the closest point on the rectangle {a}:", a.distanceTo(p))
    a.draw()
    b.draw()
    plt.show()