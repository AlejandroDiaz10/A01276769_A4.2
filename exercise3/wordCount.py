"""
Word Count Program

This program identifies all distinct words in a file and calculates
their frequency using manual algorithms (no built-in counting functions).

Author: Alejandro Díaz
Date: February 2026

Note: Module name 'wordCount' is required by assignment specification
(Req 4), hence pylint's snake_case naming convention is disabled.
"""

# pylint: disable=invalid-name

import sys
import time


def is_valid_word_character(char):
    """
    Check if a character is valid for a word (letter or apostrophe).

    Args:
        char (str): Character to check

    Returns:
        bool: True if character is valid for a word
    """
    # Letters (a-z, A-Z) and apostrophes are valid
    return char.isalpha() or char == "'"


def extract_words_from_line(line):
    """
    Extract words from a line of text manually.

    Args:
        line (str): Line of text

    Returns:
        list: List of words extracted from the line
    """
    words = []
    current_word = ""

    for char in line:
        if is_valid_word_character(char):
            current_word += char
        else:
            # End of word - save it if not empty
            if current_word:
                words.append(current_word.lower())
                current_word = ""

    # Don't forget the last word if line doesn't end with delimiter
    if current_word:
        words.append(current_word.lower())

    return words


def read_words_from_file(filename):
    """
    Read words from a file and return a list of all words.

    Args:
        filename (str): Path to the file containing text

    Returns:
        list: List of all words (in lowercase)
    """
    all_words = []
    invalid_lines = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        words = extract_words_from_line(line)
                        all_words.extend(words)
                    except (UnicodeDecodeError, ValueError) as e:
                        invalid_lines += 1
                        print(
                            f"Warning: Error processing line "
                            f"{line_number}: {e} - Skipping"
                        )

        if invalid_lines > 0:
            print(f"\nTotal lines with errors: {invalid_lines}\n")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except (IOError, OSError) as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return all_words


def count_word_frequencies(words):
    """
    Count the frequency of each word manually (no Counter library).

    Args:
        words (list): List of words

    Returns:
        dict: Dictionary with word as key and frequency as value
    """
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def sort_by_frequency(frequency_dict):
    """
    Sort words by frequency (descending) manually, then alphabetically.

    Args:
        frequency_dict (dict): Dictionary of word frequencies

    Returns:
        list: List of tuples (word, frequency) sorted by frequency desc,
              then alphabetically
    """
    # Convert dictionary to list of tuples
    items = []
    for word, freq in frequency_dict.items():
        items.append((word, freq))

    # Manual sorting using bubble sort (educational purpose)
    # Sort by frequency (descending), then by word (ascending)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare frequencies (higher first)
            # If same frequency, compare words alphabetically
            if items[j][1] < items[j + 1][1] or (
                items[j][1] == items[j + 1][1] and items[j][0] > items[j + 1][0]
            ):
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


def format_results_table(sorted_words):
    """
    Format word frequency results into a table string.

    Args:
        sorted_words (list): List of tuples (word, frequency)

    Returns:
        str: Formatted table
    """
    # Calculate column widths
    max_word_width = max(len(word) for word, _ in sorted_words)
    max_freq_width = max(len(str(freq)) for _, freq in sorted_words)

    # Ensure minimum widths for headers
    word_width = max(max_word_width, len("Word"))
    freq_width = max(max_freq_width, len("Frequency"))

    # Build table
    separator = "+" + "-" * (word_width + 2) + "+" + "-" * (freq_width + 2) + "+"

    header = f"| {'Word':<{word_width}} | {'Frequency':>{freq_width}} |"

    table = separator + "\n" + header + "\n" + separator + "\n"

    for word, frequency in sorted_words:
        row = f"| {word:<{word_width}} | {frequency:>{freq_width}} |"
        table += row + "\n"

    table += separator

    return table


def calculate_statistics(frequency_dict, total_words):
    """
    Calculate word count statistics.

    Args:
        frequency_dict (dict): Dictionary of word frequencies
        total_words (int): Total number of words

    Returns:
        dict: Dictionary containing various statistics
    """
    distinct_words = len(frequency_dict)

    # Find most frequent word(s) using max builtin
    if frequency_dict:
        max_frequency = max(frequency_dict.values())
    else:
        max_frequency = 0

    most_frequent = []
    for word, freq in frequency_dict.items():
        if freq == max_frequency:
            most_frequent.append(word)

    # Sort most frequent words alphabetically
    most_frequent = sorted(most_frequent)

    return {
        "total_words": total_words,
        "distinct_words": distinct_words,
        "most_frequent_words": most_frequent,
        "max_frequency": max_frequency,
    }


def save_results(filename, sorted_words, stats, elapsed_time):
    """
    Save word count results to a file.

    Args:
        filename (str): Output filename
        sorted_words (list): List of tuples (word, frequency)
        stats (dict): Statistics dictionary
        elapsed_time (float): Execution time in seconds
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("=" * 70 + "\n")
            file.write("WORD FREQUENCY ANALYSIS RESULTS\n")
            file.write("=" * 70 + "\n\n")

            # Write statistics
            file.write("STATISTICS:\n")
            file.write(f"Total words: {stats['total_words']}\n")
            file.write(f"Distinct words: {stats['distinct_words']}\n")
            file.write(
                f"Most frequent word(s): "
                f"{', '.join(stats['most_frequent_words'])}\n"
            )
            file.write(f"Maximum frequency: {stats['max_frequency']}\n\n")

            # Write frequency table
            file.write("WORD FREQUENCY TABLE:\n")
            file.write("(Sorted by frequency descending, then alphabetically)\n\n")
            table = format_results_table(sorted_words)
            file.write(table)

            file.write(f"\n\nExecution Time: {elapsed_time:.6f} seconds\n")
            file.write("=" * 70 + "\n")

        print(f"\nResults saved to '{filename}'")
    except (IOError, OSError) as e:
        print(f"Error saving results: {e}")


def display_results(sorted_words, stats, elapsed_time):
    """
    Display word count results on console.

    Args:
        sorted_words (list): List of tuples (word, frequency)
        stats (dict): Statistics dictionary
        elapsed_time (float): Execution time in seconds
    """
    print("\n" + "=" * 70)
    print("WORD FREQUENCY ANALYSIS RESULTS")
    print("=" * 70)

    # Display statistics
    print("\nSTATISTICS:")
    print(f"Total words: {stats['total_words']}")
    print(f"Distinct words: {stats['distinct_words']}")
    print(f"Most frequent word(s): " f"{', '.join(stats['most_frequent_words'])}")
    print(f"Maximum frequency: {stats['max_frequency']}")

    # Display frequency table
    print("\nWORD FREQUENCY TABLE:")
    print("(Sorted by frequency descending, then alphabetically)\n")
    table = format_results_table(sorted_words)
    print(table)

    print(f"\n\nExecution Time: {elapsed_time:.6f} seconds")
    print("=" * 70)


def main():
    """Main function to execute the word count analysis."""
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = "WordCountResults.txt"

    # Start timing
    start_time = time.time()

    print(f"Reading data from '{input_filename}'...")

    # Read words from file
    words = read_words_from_file(input_filename)

    if not words:
        print("Warning: No valid words found in the file.")
        # Create empty results
        sorted_words = []
        stats = {
            "total_words": 0,
            "distinct_words": 0,
            "most_frequent_words": [],
            "max_frequency": 0,
        }
    else:
        print(f"Successfully read {len(words)} words.")
        print("Analyzing word frequencies...")

        # Count word frequencies
        frequency_dict = count_word_frequencies(words)

        # Sort by frequency
        sorted_words = sort_by_frequency(frequency_dict)

        # Calculate statistics
        stats = calculate_statistics(frequency_dict, len(words))

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Display and save results
    display_results(sorted_words, stats, elapsed_time)
    save_results(output_filename, sorted_words, stats, elapsed_time)


if __name__ == "__main__":
    main()
