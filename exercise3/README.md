# Exercise 3: Word Count

## Description
A Python program that identifies all distinct words in a text file and calculates their frequency using manual algorithms (no built-in counting functions like Counter).

## Features
- ✅ Command-line file input
- ✅ Case-insensitive word counting
- ✅ Word frequency analysis
- ✅ Manual counting algorithm (no Counter library)
- ✅ Punctuation removal
- ✅ Apostrophe preservation in contractions
- ✅ Results sorted by frequency (descending) then alphabetically
- ✅ Results displayed in formatted table on console and saved to file
- ✅ Execution time measurement
- ✅ Support for large text files (hundreds to thousands of words)
- ✅ PEP-8 compliant (PyLint score: 10/10)

## Installation

### Requirements
- Python 3.6 or higher
- pylint (for code validation)

### Setup
```bash
# Install pylint (optional, for code validation)
pip install pylint
```

## Usage

### Basic Execution
```bash
python wordCount.py <input_file>
```

### Example
```bash
python wordCount.py test_data/test_case_1.txt
```

### Expected Output Format
```
Reading data from 'test_data/test_case_1.txt'...
Successfully read 18 words.
Analyzing word frequencies...

======================================================================
WORD FREQUENCY ANALYSIS RESULTS
======================================================================

STATISTICS:
Total words: 18
Distinct words: 10
Most frequent word(s): the
Maximum frequency: 4

WORD FREQUENCY TABLE:
(Sorted by frequency descending, then alphabetically)

+-------+-----------+
| Word  | Frequency |
+-------+-----------+
| the   |         4 |
| dog   |         2 |
| fox   |         2 |
| is    |         2 |
| lazy  |         2 |
| quick |         2 |
| and   |         1 |
| brown |         1 |
| jumps |         1 |
| over  |         1 |
+-------+-----------+

Execution Time: 0.000374 seconds
======================================================================

Results saved to 'WordCountResults.txt'
```

## Input File Format
The input file should contain text with words separated by spaces or punctuation. The program accepts:
- Regular text with punctuation
- Contractions with apostrophes ("don't", "it's")
- Mixed case words (counted case-insensitively)
- Numbers and special characters (treated as word separators)

Example input file:
```
The quick brown fox jumps over the lazy dog.
The fox is quick and the dog is lazy.
```

## Output Files
- **Console**: Results displayed with statistics and formatted table
- **WordCountResults.txt**: Complete results saved to file

## Word Processing Rules

### Valid Word Characters
- Letters (a-z, A-Z)
- Apostrophes (') within words (for contractions)

### Word Delimiters
- Spaces, tabs, newlines
- Punctuation: . , ! ? ; : " ( ) [ ] { }
- Numbers: 0-9
- Special characters: @ # $ % & * - + = / \

### Case Sensitivity
All words are converted to lowercase for counting:
- "Python", "PYTHON", "python" → counted as "python"

### Contractions
Apostrophes within words are preserved:
- "don't" → counted as "don't"
- "it's" → counted as "it's"
- "we'll" → counted as "we'll"

## Test Cases
The program has been validated with 7 comprehensive test cases:

1. **Simple Repeated Words** - Tests basic frequency counting
2. **Punctuation Handling** - Tests word extraction with punctuation
3. **Clear Frequency Patterns** - Tests obvious repetition (test×7, hello×3)
4. **Case-Insensitive** - Tests mixed case (Python, PYTHON, python)
5. **Apostrophes/Contractions** - Tests contraction preservation
6. **Numbers and Special Characters** - Tests delimiter handling
7. **Large Dataset** - Tests scalability (445 words)

See [test_cases.md](test_cases.md) for detailed documentation.

## Code Quality

### PyLint Validation
```bash
pylint wordCount.py > pylint_report.txt
```

**Result**: 10.00/10 ✅

See [pylint_report.txt](pylint_report.txt) for complete analysis.

## Project Structure
```
exercise3/
├── wordCount.py               # Main program
├── README.md                  # This file
├── test_cases.md              # Test cases documentation
├── pylint_report.txt          # PyLint validation report
├── WordCountResults.txt       # Output file (generated)
└── test_data/                 # Test input files
    ├── test_case_1.txt       (simple sentences)
    ├── test_case_2.txt       (punctuation)
    ├── test_case_3.txt       (repetition patterns)
    ├── test_case_4.txt       (mixed case)
    ├── test_case_5.txt       (contractions)
    ├── test_case_6.txt       (numbers/special chars)
    └── test_case_7.txt       (large text - 445 words)
```

## Technical Details

### Algorithms Implemented

#### Word Extraction
Manual character-by-character parsing:
```python
For each character:
    If letter or apostrophe:
        Add to current word
    Else:
        Save word and start new word
```

#### Frequency Counting
Manual dictionary-based counting (no Counter):
```python
For each word:
    If word in dictionary:
        Increment count
    Else:
        Add word with count = 1
```

#### Sorting
Manual bubble sort by frequency (descending) then alphabetically:
```python
For i in range(n):
    For j in range(n-i-1):
        If freq[j] < freq[j+1] OR
           (freq[j] == freq[j+1] AND word[j] > word[j+1]):
            Swap items
```

All processing is done **without using built-in functions** like `Counter`, `sorted()` with complex keys, or other high-level abstractions.

### Statistics Calculated
- **Total words**: Count of all words (including duplicates)
- **Distinct words**: Count of unique words
- **Most frequent word(s)**: Word(s) with highest frequency
- **Maximum frequency**: Highest occurrence count

### Table Formatting
- Dynamic column width adjustment
- ASCII table borders
- Right-aligned frequency column
- Left-aligned word column

## Requirements Compliance

| Requirement | Status | Description |
|-------------|--------|-------------|
| Req 1 | ✅ | Command-line file parameter |
| Req 2 | ✅ | Identify distinct words and frequencies |
| Req 3 | ✅ | Error handling (though text rarely has "invalid" data) |
| Req 4 | ✅ | Named `wordCount.py` |
| Req 5 | ✅ | Correct invocation format |
| Req 6 | ✅ | Handles large files (tested with 445 words) |
| Req 7 | ✅ | Execution time displayed and saved |
| Req 8 | ✅ | PEP-8 compliant (10/10 PyLint) |

## Performance
- Handles 445 words in ~3ms
- Efficient O(n) word extraction and counting
- O(n²) sorting (bubble sort for educational purposes)
- Memory efficient single-pass processing
- Scalable to thousands of words

## Example Results

### Simple Text
**Input:**
```
The quick brown fox jumps over the lazy dog.
The fox is quick and the dog is lazy.
```

**Output:**
- Total words: 18
- Distinct words: 10
- Most frequent: "the" (4 times)

### Large Text
**Input:** 445-word text about Python
**Output:**
- Total words: 445
- Distinct words: 239
- Most frequent: "python" (67 times)
- Execution time: ~3ms

## Common Use Cases

### Analyzing Essays or Articles
```bash
python wordCount.py my_essay.txt
```

### Finding Most Common Words in Code Comments
```bash
python wordCount.py comments_extracted.txt
```

### Analyzing Song Lyrics
```bash
python wordCount.py song_lyrics.txt
```

### Text Processing Research
```bash
python wordCount.py research_corpus.txt
```

## Limitations
- Bubble sort is O(n²) - for very large datasets (10,000+ words), consider optimized sorting
- Apostrophes are preserved, so "don't" and "dont" are different words
- Numbers are treated as delimiters, not words
- Email addresses and URLs are split by special characters

## Future Enhancements (Not Required)
- Option to remove contractions
- Option to include numbers as words
- Export to CSV format
- Visualization of word frequencies
- N-gram analysis (word pairs, triplets)

## Author
**Alejandro Díaz**  
February 2026

## License
Educational project - Free to use for learning purposes
