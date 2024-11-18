from Point import Point
from LineSegment import LineSegment

class BruteCollinearPoints:
    def __init__(self, points):
        """
        Initializes a BruteCollinearPoints object with an array of points.

        Args:
            points (list[Point]): An array of points.
        Raises:
            ValueError: If the input array or any point in it is None.
            ValueError: If any two points in the array are the same.
        """
        if points is None:
            raise ValueError()

        n = len(points)
        self.segments = []

        for p in range(n):
            if points[p] is None:
                raise ValueError()
            for q in range(p + 1, n):
                if points[q] is None or points[p].slopeTo(points[q]) == float("-inf"):
                    raise ValueError()
                for r in range(q + 1, n):
                    if points[r] is None or points[q].slopeTo(points[r]) == float("-inf"):
                        raise ValueError()
                    if points[p].slopeTo(points[q]) == points[p].slopeTo(points[r]):
                        for s in range(r + 1, n):
                            if points[s] is None or points[r].slopeTo(points[s]) == float("-inf"):
                                raise ValueError()
                            if points[p].slopeTo(points[q]) == points[p].slopeTo(points[s]):
                                segment = [points[p], points[q], points[r], points[s]]
                                segment.sort()
                                self.segments.append(LineSegment(segment[0], segment[3]))

    def number_of_segments(self):
        """
        Returns the number of line segments found.

        Returns:
            int: The number of line segments.
        """
        return len(self.segments)

    def get_segments(self):
        """
        Returns an array of line segments found.

        Returns:
            list[LineSegment]: An array of line segments.
        """
        return self.segments