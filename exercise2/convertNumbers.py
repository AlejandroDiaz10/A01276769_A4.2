"""
Convert Numbers Program

This program converts decimal numbers to binary and hexadecimal
representations using manual algorithms (no built-in conversion functions).

Author: Alejandro Díaz
Date: February 2026

Note: Module name 'convertNumbers' is required by assignment specification
(Req 4), hence pylint's snake_case naming convention is disabled.
"""

# pylint: disable=invalid-name

import sys
import time


def read_numbers_from_file(filename):
    """
    Read numbers from a file and return a list of valid integers.

    Args:
        filename (str): Path to the file containing numbers

    Returns:
        list: List of valid integers
    """
    numbers = []
    invalid_count = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        # Convert to float first, then to int to handle decimals
                        number = int(float(line))
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


def decimal_to_binary(number):
    """
    Convert a decimal number to binary representation using manual algorithm.

    Args:
        number (int): Decimal number to convert

    Returns:
        str: Binary representation (e.g., "1010" for 10)
    """
    if number == 0:
        return "0"

    # Handle negative numbers
    is_negative = number < 0
    number = abs(number)

    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    if is_negative:
        binary = "-" + binary

    return binary


def decimal_to_hexadecimal(number):
    """
    Convert a decimal number to hexadecimal representation using manual algorithm.

    Args:
        number (int): Decimal number to convert

    Returns:
        str: Hexadecimal representation (e.g., "A" for 10)
    """
    if number == 0:
        return "0"

    # Handle negative numbers
    is_negative = number < 0
    number = abs(number)

    # Hexadecimal digits mapping
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""

    while number > 0:
        remainder = number % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        number = number // 16

    if is_negative:
        hexadecimal = "-" + hexadecimal

    return hexadecimal


def format_conversion_table(conversions):
    """
    Format conversions into a table string.

    Args:
        conversions (list): List of tuples (decimal, binary, hexadecimal)

    Returns:
        str: Formatted table
    """
    # Calculate column widths
    max_decimal_width = max(len(str(conv[0])) for conv in conversions)
    max_binary_width = max(len(conv[1]) for conv in conversions)
    max_hex_width = max(len(conv[2]) for conv in conversions)

    # Ensure minimum widths for headers
    decimal_width = max(max_decimal_width, len("Decimal"))
    binary_width = max(max_binary_width, len("Binary"))
    hex_width = max(max_hex_width, len("Hexadecimal"))

    # Build table
    separator = (
        "+"
        + "-" * (decimal_width + 2)
        + "+"
        + "-" * (binary_width + 2)
        + "+"
        + "-" * (hex_width + 2)
        + "+"
    )

    header = (
        f"| {'Decimal':<{decimal_width}} | "
        f"{'Binary':<{binary_width}} | "
        f"{'Hexadecimal':<{hex_width}} |"
    )

    table = separator + "\n" + header + "\n" + separator + "\n"

    for decimal, binary, hexadecimal in conversions:
        row = (
            f"| {str(decimal):<{decimal_width}} | "
            f"{binary:<{binary_width}} | "
            f"{hexadecimal:<{hex_width}} |"
        )
        table += row + "\n"

    table += separator

    return table


def save_results(filename, conversions, elapsed_time):
    """
    Save conversion results to a file.

    Args:
        filename (str): Output filename
        conversions (list): List of tuples (decimal, binary, hexadecimal)
        elapsed_time (float): Execution time in seconds
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("=" * 70 + "\n")
            file.write(
                "NUMBER CONVERSION RESULTS (Decimal to Binary and Hexadecimal)\n"
            )
            file.write("=" * 70 + "\n\n")
            file.write(f"Total numbers converted: {len(conversions)}\n\n")

            # Write conversion table
            table = format_conversion_table(conversions)
            file.write(table)

            file.write(f"\n\nExecution Time: {elapsed_time:.6f} seconds\n")
            file.write("=" * 70 + "\n")

        print(f"\nResults saved to '{filename}'")
    except (IOError, OSError) as e:
        print(f"Error saving results: {e}")


def display_results(conversions, elapsed_time):
    """
    Display conversion results on console.

    Args:
        conversions (list): List of tuples (decimal, binary, hexadecimal)
        elapsed_time (float): Execution time in seconds
    """
    print("\n" + "=" * 70)
    print("NUMBER CONVERSION RESULTS (Decimal to Binary and Hexadecimal)")
    print("=" * 70)
    print(f"Total numbers converted: {len(conversions)}\n")

    # Display conversion table
    table = format_conversion_table(conversions)
    print(table)

    print(f"\n\nExecution Time: {elapsed_time:.6f} seconds")
    print("=" * 70)


def main():
    """Main function to execute the number conversion."""
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = "ConvertionResults.txt"

    # Start timing
    start_time = time.time()

    print(f"Reading data from '{input_filename}'...")

    # Read numbers from file
    numbers = read_numbers_from_file(input_filename)

    if not numbers:
        print("Error: No valid numbers found in the file.")
        sys.exit(1)

    print(f"Successfully read {len(numbers)} numbers.")
    print("Converting numbers...")

    # Convert all numbers
    conversions = []
    for number in numbers:
        binary = decimal_to_binary(number)
        hexadecimal = decimal_to_hexadecimal(number)
        conversions.append((number, binary, hexadecimal))

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Display and save results
    display_results(conversions, elapsed_time)
    save_results(output_filename, conversions, elapsed_time)


if __name__ == "__main__":
    main()
