import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

/**
 * The `PercolationStats` class performs Monte Carlo simulations to estimate percolation thresholds.
 * It computes statistical properties such as mean, standard deviation, and confidence intervals.
 */
public class PercolationStats {
    private static final double CONFIDENCE_95 = 1.96; // 95% confidence level
    private int n; // Grid size (n-by-n)
    private double[] results; // Fraction of open sites for each trial
    private double meanValue; // Mean of open site fractions
    private double stddevValue; // Standard deviation of open site fractions
    private double confidenceLoValue; // Lower bound of confidence interval
    private double confidenceHiValue; // Upper bound of confidence interval

    /**
     * Initializes a `PercolationStats` object with Monte Carlo simulations.
     *
     * @param n      The grid size (n-by-n).
     * @param trials The number of independent trials.
     * @throws IllegalArgumentException if n or trials is not positive.
     */
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("n and T must be a positive integers");
        }

        this.n = n;
        results = new double[trials];

        // Perform independent trials
        for (int i = 0; i < trials; i++) {
            Percolation p = new Percolation(n);

            while (!p.percolates()) {
                int row = StdRandom.uniformInt(1, n + 1);
                int col = StdRandom.uniformInt(1, n + 1);
                p.open(row, col);
            }

            results[i] = (double) p.numberOfOpenSites() / (n * n);
        }

        // Compute statistics
        meanValue = StdStats.mean(results);
        stddevValue = StdStats.stddev(results);
        confidenceLoValue = meanValue - CONFIDENCE_95 * stddevValue / Math.sqrt(trials);
        confidenceHiValue = meanValue + CONFIDENCE_95 * stddevValue / Math.sqrt(trials);
    }

    /**
     * Returns the mean of the percolation threshold.
     *
     * @return The mean value.
     */
    public double mean() {
        return meanValue;
    }

    /**
     * Returns the standard deviation of the percolation threshold.
     *
     * @return The standard deviation value.
     */
    public double stddev() {
        return stddevValue;
    }

    /**
     * Returns the lower bound of the 95% confidence interval.
     *
     * @return The lower bound value.
     */
    public double confidenceLo() {
        return confidenceLoValue;
    }

    /**
     * Returns the upper bound of the 95% confidence interval.
     *
     * @return The upper bound value.
     */
    public double confidenceHi() {
        return confidenceHiValue;
    }

    /**
     * Example usage demonstrating the `PercolationStats` class.
     *
     * @param args Command-line arguments (n and trials).
     */
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java PercolationStats <n> <T>");
            return;
        }

        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);

        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("Both 'n' and 'trials' must be positive integers.");
        }

        PercolationStats stats = new PercolationStats(n, trials);

        StdOut.println("mean                    = " + stats.mean());
        StdOut.println("stddev                  = " + stats.stddev());
        StdOut.println(
                "95% confidence interval = [" + stats.confidenceLo() + ", " + stats.confidenceHi()
                        + "]");
    }

}

