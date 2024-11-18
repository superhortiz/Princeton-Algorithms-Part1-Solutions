import heapq
from Board import Board

class Solver:
    """
    Solver class to find a solution to the initial board using the A* algorithm.
    """
    def __init__(self, initial):
        """
        Initializes the Solver with the initial board configuration.
        Raises a ValueError if the initial board is None.
        """
        if initial == None:
            raise ValueError("Invalid argument")
        self.solutionPath = []
        pq, pqTwin = [], []

        # Create initial search nodes for the board and its twin
        firstNode = self._SearchNode(initial, g = 0, prevNode = None)
        firstTwinNode = self._SearchNode(initial.twin(), g = 0, prevNode = None)

        # Push the initial nodes onto their respective priority queues
        heapq.heappush(pq, (firstNode.f, firstNode))
        heapq.heappush(pqTwin, (firstTwinNode.f, firstTwinNode))

        # Process the priority queues until a solution is found or both are empty
        while pq and pqTwin:
            currentNode = heapq.heappop(pq)[1]
            currentTwinNode = heapq.heappop(pqTwin)[1]

            # Check if the current node or its twin is the goal
            if currentNode.board.isGoal():
                self._buildPath(currentNode)
                return

            if currentTwinNode.board.isGoal():
                self.solutionPath = None
                return

            # Add neighbors of the current node to the priority queue
            for neighbor in currentNode.board.neighbors():
                if currentNode.prevNode == None or currentNode.prevNode.board != neighbor:
                    Node = self._SearchNode(neighbor, currentNode.g + 1, currentNode)
                    heapq.heappush(pq, (Node.f, Node))

            # Add neighbors of the current twin node to the twin priority queue
            for neighbor in currentTwinNode.board.neighbors():
                if currentTwinNode.prevNode == None or currentTwinNode.prevNode.board != neighbor:
                    Node = self._SearchNode(neighbor, currentTwinNode.g + 1, currentTwinNode)
                    heapq.heappush(pqTwin, (Node.f, Node))

    def isSolvable(self):
        """
        Returns True if the puzzle is solvable, False otherwise.
        """
        return self.solutionPath != None

    def moves(self):
        """
        Returns the number of moves to solve the puzzle.
        Returns -1 if the puzzle is unsolvable.
        """
        if not self.isSolvable():
            return -1
        return len(self.solutionPath) - 1

    def solution(self):
        """
        Returns the sequence of boards in the solution path.
        """
        return self.solutionPath

    def _buildPath(self, node):
        """
        Builds the solution path from the goal node to the initial node.
        """
        while node:
            self.solutionPath.append(node.board)
            node = node.prevNode
        self.solutionPath.reverse()

    class _SearchNode:
        def __init__(self, board, g, prevNode):
            """
            Initializes a search node with the given board, move count, and previous node.
            """
            self.board = board
            self.g = g
            self.prevNode = prevNode
            self.f = g + board.manhattan()

        def __lt__(self, other):
            """
            Less-than comparison based on the f-score for priority queue ordering.
            """
            return self.f < other.f

        def __eq__(self, other):
            """
            Equality comparison based on the f-score.
            """
            if self is other:
                return True
            if other is None or not isinstance(other, Solver._SearchNode):
                return False
            return self.f == other.f