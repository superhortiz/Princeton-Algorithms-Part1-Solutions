from Point import Point

class LineSegment:
    def __init__(self, p, q):
        """
        Initializes a line segment with two distinct points.

        Args:
            p (Point): The first point.
            q (Point): The second point.
        Raises:
            ValueError: If either `p` or `q` is None.
            ValueError: If `p` and `q` are the same point.
        """
        if p is None or q is None:
            raise ValueError("argument to LineSegment constructor is None")
        if p == q:
            raise ValueError(f"both arguments to LineSegment constructor are the same point: {p}")
        self.p = p
        self.q = q

    def __str__(self):
        """
        Returns a string representation of the line segment.

        Returns:
            str: A string representation of the line segment in the format "p -> q".
        """
        return f'{self.p} -> {self.q}'


# Example usage
if __name__ == "__main__":
    p = Point(0, 0)
    q = Point(2, 3)
    segment = LineSegment(p, q)
    print(segment)
