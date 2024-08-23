from Point import Point
from LineSegment import LineSegment
from copy import deepcopy

class FastCollinearPoints:
	def __init__(self, points):
	"""
	Initializes a FastCollinearPoints object with an array of points.

	Args:
		points (list[Point]): An array of points.
	Raises:
		ValueError: If the input array or any point in it is None.
		ValueError: If any two points in the array are the same.
        """
		if points is None:
			raise ValueError()

		n = len(points)
		clone = []
		self.segments = []
		
		for i in range(n):
			if points[i] is None:
				raise ValueError()
			else:
				for j in range(i + 1, n):
					if points[j] is None and points[i] == points[j]:
						raise ValueError()
				clone.append(points[i])

		clone.sort()	# Sorting the points is crucial; it allows efficient segment definition
				# Once sorted, we can identify line segments efficiently when encountered for the first time
				# This approach helps us avoid storing duplicate segments

		for p in range(n):
			copy = deepcopy(clone)
			copy.sort(key = points[p].slopeOrder())

			q = 1
			while q < n:
				start = q
				while q < n and points[p].slopeTo(copy[q - 1]) == points[p].slopeTo(copy[q]):
					q += 1

				if q - start >= 2 and points[p] < copy[start - 1]:
					self.segments.append(LineSegment(points[p], copy[q - 1]))

				q += 1

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


# Example usage
if __name__ == "__main__":
    points = [Point(10000, 0), Point(0, 10000), Point(3000, 7000), Point(7000, 3000), Point(20000, 21000),
	      Point(3000, 4000), Point(14000, 15000), Point(6000, 7000)]
    
    lines = FastCollinearPoints(points)
    print(f"Number of segments found = {lines.number_of_segments()}")

    segments = lines.get_segments()
    for segment in segments:
        print(segment)
