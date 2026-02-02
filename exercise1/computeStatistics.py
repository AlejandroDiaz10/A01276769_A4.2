"""
Compute Statistics Program

This program computes descriptive statistics (mean, median, mode,
standard deviation, and variance) from a file containing numbers.

Author: Alejandro Díaz
Date: February 2026

Note: Module name 'computeStatistics' is required by assignment specification
(Req 4), hence pylint's snake_case naming convention is disabled.
"""

# pylint: disable=invalid-name

import sys
import time


def read_numbers_from_file(filename):
    """
    Read numbers from a file and return a list of valid numbers.

    Args:
        filename (str): Path to the file containing numbers

    Returns:
        list: List of valid numbers (float)
    """
    numbers = []
    invalid_count = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        number = float(line)
                        numbers.append(number)
                    except ValueError:
                        invalid_count += 1
                        print(
                            f"Warning: Invalid data at line {line_number}: "
                            f"'{line}' - Skipping"
                        )

        if invalid_count > 0:
            print(f"\nTotal invalid entries skipped: {invalid_count}\n")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except (IOError, OSError) as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return numbers


def calculate_mean(numbers):
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        float: Mean value
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        float: Median value
    """
    if not numbers:
        return 0.0

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        # Even number of elements: average of two middle values
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        # Odd number of elements: middle value
        median = sorted_numbers[n // 2]

    return median


def calculate_mode(numbers):
    """
    Calculate the mode(s) of a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        list: List of mode values (can be multiple if multimodal)
    """
    if not numbers:
        return []

    # Count frequency of each number
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    # Find maximum frequency
    max_frequency = max(frequency.values())

    # Find all numbers with maximum frequency
    modes = [num for num, freq in frequency.items() if freq == max_frequency]

    # If all numbers appear once, there is no mode
    if max_frequency == 1:
        return []

    return sorted(modes)


def calculate_variance(numbers, mean):
    """
    Calculate the variance of a list of numbers.

    Args:
        numbers (list): List of numbers
        mean (float): Mean of the numbers

    Returns:
        float: Variance value
    """
    if len(numbers) < 2:
        return 0.0

    # Sum of squared differences from mean
    squared_diffs = sum((x - mean) ** 2 for x in numbers)

    # Population variance (dividing by n)
    variance = squared_diffs / len(numbers)

    return variance


def calculate_std_deviation(variance):
    """
    Calculate the standard deviation from variance.

    Args:
        variance (float): Variance value

    Returns:
        float: Standard deviation value
    """
    # Manual square root calculation using Newton's method
    if variance == 0:
        return 0.0

    # Initial guess
    x = variance
    # Newton's method for square root
    for _ in range(50):  # Sufficient iterations for convergence
        x = (x + variance / x) / 2

    return x


def format_mode(modes):
    """
    Format mode list for display.

    Args:
        modes (list): List of mode values

    Returns:
        str: Formatted mode string
    """
    if not modes:
        return "No mode (all values appear once)"
    if len(modes) == 1:
        return f"{modes[0]}"
    return f"Multiple modes: {', '.join(map(str, modes))}"


def save_results(filename, results, elapsed_time):
    """
    Save statistics results to a file.

    Args:
        filename (str): Output filename
        results (dict): Dictionary containing statistics results
        elapsed_time (float): Execution time in seconds
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("=" * 50 + "\n")
            file.write("DESCRIPTIVE STATISTICS RESULTS\n")
            file.write("=" * 50 + "\n\n")
            file.write(f"Count of numbers: {results['count']}\n")
            file.write(f"Mean: {results['mean']:.6f}\n")
            file.write(f"Median: {results['median']:.6f}\n")
            file.write(f"Mode: {results['mode']}\n")
            file.write(f"Variance: {results['variance']:.6f}\n")
            file.write(f"Standard Deviation: {results['std_dev']:.6f}\n")
            file.write(f"\nExecution Time: {elapsed_time:.6f} seconds\n")
            file.write("=" * 50 + "\n")
        print(f"\nResults saved to '{filename}'")
    except (IOError, OSError) as e:
        print(f"Error saving results: {e}")


def display_results(results, elapsed_time):
    """
    Display statistics results on console.

    Args:
        results (dict): Dictionary containing statistics results
        elapsed_time (float): Execution time in seconds
    """
    print("\n" + "=" * 50)
    print("DESCRIPTIVE STATISTICS RESULTS")
    print("=" * 50)
    print(f"Count of numbers: {results['count']}")
    print(f"Mean: {results['mean']:.6f}")
    print(f"Median: {results['median']:.6f}")
    print(f"Mode: {results['mode']}")
    print(f"Variance: {results['variance']:.6f}")
    print(f"Standard Deviation: {results['std_dev']:.6f}")
    print(f"\nExecution Time: {elapsed_time:.6f} seconds")
    print("=" * 50)


def main():
    """Main function to execute the statistics computation."""
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = "StatisticsResults.txt"

    # Start timing
    start_time = time.time()

    print(f"Reading data from '{input_filename}'...")

    # Read numbers from file
    numbers = read_numbers_from_file(input_filename)

    if not numbers:
        print("Error: No valid numbers found in the file.")
        sys.exit(1)

    print(f"Successfully read {len(numbers)} numbers.")

    # Calculate statistics
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    modes = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_std_deviation(variance)

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Prepare results
    results = {
        "count": len(numbers),
        "mean": mean,
        "median": median,
        "mode": format_mode(modes),
        "variance": variance,
        "std_dev": std_dev,
    }

    # Display and save results
    display_results(results, elapsed_time)
    save_results(output_filename, results, elapsed_time)


if __name__ == "__main__":
    main()
