# Exercise 1: Compute Statistics

## Description
A Python program that computes descriptive statistics from a file containing numbers. The program calculates mean, median, mode, variance, and standard deviation using manual algorithms (no external statistical libraries).

## Features
- ✅ Command-line file input
- ✅ Comprehensive statistics: mean, median, mode, variance, standard deviation
- ✅ Manual algorithm implementation (no libraries)
- ✅ Invalid data handling with error messages
- ✅ Results displayed on console and saved to file
- ✅ Execution time measurement
- ✅ Support for large datasets (hundreds to thousands of items)
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
python computeStatistics.py <input_file>
```

### Example
```bash
python computeStatistics.py test_data/test_case_1.txt
```

### Expected Output Format
```
Reading data from 'test_data/test_case_1.txt'...
Successfully read 5 numbers.

==================================================
DESCRIPTIVE STATISTICS RESULTS
==================================================
Count of numbers: 5
Mean: 15.000000
Median: 15.000000
Mode: No mode (all values appear once)
Variance: 50.000000
Standard Deviation: 7.071068

Execution Time: 0.000465 seconds
==================================================

Results saved to 'StatisticsResults.txt'
```

## Input File Format
The input file should contain one number per line. The program accepts:
- Integer numbers: `5`, `10`, `100`
- Decimal numbers: `3.14`, `2.718`
- Negative numbers: `-10`, `-5.5`

Example input file:
```
5
10
15
20
25
```

## Output Files
- **Console**: Results displayed in formatted output
- **StatisticsResults.txt**: Complete results saved to file

## Test Cases
The program has been validated with 7 comprehensive test cases:

1. **Small Basic Dataset** - Tests basic functionality
2. **Invalid Data Handling** - Tests error handling
3. **Mode Detection** - Tests repeated values
4. **Large Dataset** - Tests scalability (300 items)
5. **Decimal Numbers** - Tests floating-point precision
6. **Negative Numbers** - Tests negative value handling
7. **Multiple Modes** - Tests multimodal distribution

See [test_cases.md](test_cases.md) for detailed documentation.

## Code Quality

### PyLint Validation
```bash
pylint computeStatistics.py > pylint_report.txt
```

**Result**: 10.00/10 ✅

See [pylint_report.txt](pylint_report.txt) for complete analysis.

## Project Structure
```
exercise1/
├── computeStatistics.py       # Main program
├── test_cases.md              # Test cases documentation
├── pylint_report.txt          # PyLint validation report
├── StatisticsResults.txt      # Output file (generated)
└── test_data/                 # Test input files
    ├── test_case_1.txt
    ├── test_case_2.txt
    ├── test_case_3.txt
    ├── test_case_4.txt
    ├── test_case_5.txt
    ├── test_case_6.txt
    └── test_case_7.txt
```

## Technical Details

### Algorithms Implemented
All statistics are calculated using manual implementations:

- **Mean**: Sum of values divided by count
- **Median**: Middle value (or average of two middle values)
- **Mode**: Most frequently occurring value(s)
- **Variance**: Average of squared differences from mean
- **Standard Deviation**: Square root of variance (Newton's method)

### Error Handling
- Invalid data entries are skipped with warnings
- File not found errors are handled gracefully
- Program continues execution after encountering errors
- All invalid entries are logged to console

## Requirements Compliance

| Requirement | Status | Description |
|-------------|--------|-------------|
| Req 1 | ✅ | Command-line file parameter |
| Req 2 | ✅ | All statistics computed with manual algorithms |
| Req 3 | ✅ | Invalid data handling implemented |
| Req 4 | ✅ | Named `computeStatistics.py` |
| Req 5 | ✅ | Correct invocation format |
| Req 6 | ✅ | Handles large datasets (tested with 300+ items) |
| Req 7 | ✅ | Execution time displayed and saved |
| Req 8 | ✅ | PEP-8 compliant (10/10 PyLint) |

## Author
**Alejandro Díaz**  
February 2026

## License
Educational project - Free to use for learning purposes