import sys
import random
import statistics
from Percolation import Percolation

class PercolationStats:
    def __init__(self, n, trials):
        """
        Initializes a PercolationStats object.

        Args:
            n (int): The grid size for percolation experiments.
            trials (int): The number of independent trials.

        Raises:
            ValueError: If n or trials is not a positive integer.
        """

        self.n = n
        results = []

        # Perform independent trials
        for i in range(trials):
            self.p = Percolation(n)

            while not self.p.percolates():
                row, col = random.randint(1, n), random.randint(1, n)  # Get random positions to open
                self.p.open(row, col)
            results.append(self.p.numberOfOpenSites() / (n ** 2))

        # Compute statistics
        confidence_95 = 1.96
        self.mean_value = statistics.mean(results)
        self.stddev_value = statistics.stdev(results)
        self.confidenceLo_value = self.mean_value - confidence_95 * self.stddev_value / (trials ** (1 / 2))
        self.confidenceHi_value = self.mean_value + confidence_95 * self.stddev_value / (trials ** (1 / 2))

    def mean(self):
        """
        Returns the mean percolation threshold.
        """

        return self.mean_value

    def stddev(self):
        """
        Returns the standard deviation of percolation thresholds.
        """

        return self.stddev_value

    def confidenceLo(self):
        """
        Returns the lower bound of the 95% confidence interval.
        """

        return self.confidenceLo_value

    def confidenceHi(self):
        """
        Returns the upper bound of the 95% confidence interval.
        """

        return self.confidenceHi_value


def main():
    """
    Entry point for the PercolationStats script.

    Reads command-line arguments for grid size (n) and number of trials (T).
    Computes percolation statistics and prints the results.

    Usage:
        python "1.5 Percolation.py" n T

    Args:
        None (reads from sys.argv)

    Returns:
        None
    """

    args = sys.argv[1:]  # args is a list of the command-line args
    if len(args) != 2:
        print('Usage: python PercolationStats.py n trials')
        return

    n, T = map(int, args)
    if n < 0 or T < 2:
        raise ValueError("'n' must be a positive integer, 'trials' must be equal or bigger than 2.")

    percolation = PercolationStats(n, T)
    print(f"Received n = {n}, T = {T}")
    print("mean                    =", percolation.mean())
    print("stddev                  =", percolation.stddev())
    print("95% confidence interval =", [percolation.confidenceLo(), percolation.confidenceHi()])


if __name__ == "__main__":
    main()

