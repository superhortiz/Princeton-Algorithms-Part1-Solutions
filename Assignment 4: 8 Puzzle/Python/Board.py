import copy

class Board:
	def __init__(self, tiles):
		"""
		Initialize the Board with a deep copy of the given tiles.

		Args:
			tiles (list of list of int): The initial configuration of the board.
		"""
		self.n = len(tiles) # Dimension of the board
		self.board = copy.deepcopy(tiles) # 2D list to store the tiles

	def __str__(self):
		"""
		Return a string representation of the board.

		Returns:
			str: The board size followed by the board's rows.
		"""
		string = '\n'.join(' '.join(map(str, row)) for row in self.board)
		return f"{self.n}\n{string}\n"

	def dimension(self):
		"""
		Return the dimension of the board.

		Returns:
			int: The dimension of the board.
		"""
		return self.n

	def hamming(self):
		"""
		Calculate the Hamming distance of the board.

		The Hamming distance is the number of tiles out of place.

		Returns:
			int: The Hamming distance.
		"""
		distance = 0;
		for i in range(self.n):
			for j in range(self.n):
				if self.board[i][j] != self.n * i + j + 1 and self.board[i][j] != 0:
					distance += 1
		return distance

	def manhattan(self):
		"""
		Calculate the Manhattan distance of the board.

		The Manhattan distance is the sum of the distances of the tiles from their goal positions.

		Returns:
			int: The Manhattan distance.
		"""
		distance = 0;
		for i in range(self.n):
			for j in range(self.n):
				if self.board[i][j] != 0:
					value = self.board[i][j]
					row = (value - 1) // self.n
					col = (value - 1) % self.n
					distance += abs(row - i) + abs(col - j)
		return distance

	def isGoal(self):
		"""
		Check if the board is in the goal state.

		The goal state is when all tiles are in order from 1 to n*n-1, with the blank tile (0) at the end.

		Returns:
			bool: True if the board is in the goal state, False otherwise.
		"""
		for i in range(self.n):
			for j in range(self.n):
				if i == self.n - 1 and j == self.n - 1:
					if self.board[i][j] != 0:
						return False
				elif self.board[i][j] != self.n * i + j + 1:
					return False
		return True

	def __eq__(self, other):
		"""
		Check if two Board instances are equal.

		Args:
			other (Board): The other Board instance to compare with.

		Returns:
			bool: True if both Board instances are equal, False otherwise.
		"""
		if self is other:
			return True
		if other is None or not isinstance(other, Board):
			return False
		return self.n == other.n and self.board == other.board

	def neighbors(self):
		"""
		Generate all neighboring boards by sliding a tile into the blank space.

		Returns:
			list of Board: A list of all neighboring board configurations.
		"""
		neighbors = []
		i, j = self.findIndices()
		candidates = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
		for candidate in candidates:
			x = candidate[0]
			y = candidate[1]
			if 0 <= x < self.n and 0 <= y < self.n:
				newBoard = copy.deepcopy(self.board)
				newBoard[i][j], newBoard[x][y] = newBoard[x][y], newBoard[i][j]
				neighbors.append(Board(newBoard))
		return neighbors

	def twin(self):
		"""
		Create a twin board by swapping any pair of tiles.

		Returns:
			Board: A new board instance with two tiles swapped.
		"""
		x1, y1, x2, y2 = 0, 0, 0, 1
		newBoard = copy.deepcopy(self.board)
		i, j = self.findIndices()
		if (i == x1 and j == y1) or (i == x2 and j == y2):
			x1, x2, y1, y2 = self.n - 1, self.n - 1, self.n - 1, self.n - 2
		newBoard[x1][y1], newBoard[x2][y2] = newBoard[x2][y2], newBoard[x1][y1]
		return Board(newBoard)

	def findIndices(self):
		"""
		Find the indices of the blank tile (0) in the board.

		Returns:
			tuple: The (row, column) indices of the blank tile.
		"""
		for i in range(self.n):
			for j in range(self.n):
				if self.board[i][j] == 0:
					return (i, j)
		return (-1, -1)


# Example usage
if __name__ == "__main__":
	tiles = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
	board = Board(tiles)
	print(board)
	print("Hamming distance =", board.hamming())
	print("Manhattan distance =", board.manhattan())
	print("Is the goal?", board.isGoal())
	for neighbor in board.neighbors():
		print(neighbor)
	print("Twin =\n", board.twin(), sep = '')
