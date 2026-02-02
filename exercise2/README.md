# Exercise 2: Number Converter

## Description
A Python program that converts decimal numbers to binary and hexadecimal representations using manual algorithms (no built-in conversion functions).

## Features
- ✅ Command-line file input
- ✅ Decimal to Binary conversion (manual algorithm)
- ✅ Decimal to Hexadecimal conversion (manual algorithm)
- ✅ Invalid data handling with error messages
- ✅ Results displayed in formatted table on console and saved to file
- ✅ Execution time measurement
- ✅ Support for large datasets (hundreds to thousands of items)
- ✅ Handles negative numbers
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
python convertNumbers.py <input_file>
```

### Example
```bash
python convertNumbers.py test_data/test_case_1.txt
```

### Expected Output Format
```
Reading data from 'test_data/test_case_1.txt'...
Successfully read 5 numbers.
Converting numbers...

======================================================================
NUMBER CONVERSION RESULTS (Decimal to Binary and Hexadecimal)
======================================================================
Total numbers converted: 5

+---------+--------+-------------+
| Decimal | Binary | Hexadecimal |
+---------+--------+-------------+
| 10      | 1010   | A           |
| 15      | 1111   | F           |
| 20      | 10100  | 14          |
| 25      | 11001  | 19          |
| 30      | 11110  | 1E          |
+---------+--------+-------------+

Execution Time: 0.000382 seconds
======================================================================

Results saved to 'ConvertionResults.txt'
```

## Input File Format
The input file should contain one number per line. The program accepts:
- Integer numbers: `10`, `255`, `1000`
- Negative numbers: `-10`, `-255`
- Decimal numbers (converted to integers): `10.5` → `10`

Example input file:
```
10
15
20
25
30
```

## Output Files
- **Console**: Results displayed in formatted table
- **ConvertionResults.txt**: Complete results saved to file with table format

## Conversion Examples

| Decimal | Binary | Hexadecimal | Explanation |
|---------|--------|-------------|-------------|
| 10      | 1010   | A           | Basic conversion |
| 15      | 1111   | F           | Max single hex digit |
| 255     | 11111111 | FF        | Max 8-bit value |
| 256     | 100000000 | 100      | First 9-bit value |
| 4095    | 111111111111 | FFF   | Max 12-bit value |

## Test Cases
The program has been validated with 7 comprehensive test cases:

1. **Small Basic Dataset** - Tests basic conversion accuracy
2. **Invalid Data Handling** - Tests error handling
3. **Powers of 2** - Tests binary patterns (1, 2, 4, 8, 16...)
4. **Large Numbers** - Tests hexadecimal boundaries (FF, FFF, FFFF)
5. **Zero and Single Digits** - Tests edge cases
6. **Negative Numbers** - Tests sign handling
7. **Large Dataset** - Tests scalability (200 items)

See [test_cases.md](test_cases.md) for detailed documentation.

## Code Quality

### PyLint Validation
```bash
pylint convertNumbers.py > pylint_report.txt
```

**Result**: 10.00/10 ✅

See [pylint_report.txt](pylint_report.txt) for complete analysis.

## Project Structure
```
exercise2/
├── convertNumbers.py          # Main program
├── README.md                  # This file
├── test_cases.md              # Test cases documentation
├── pylint_report.txt          # PyLint validation report
├── ConvertionResults.txt      # Output file (generated)
└── test_data/                 # Test input files
    ├── test_case_1.txt       (basic)
    ├── test_case_2.txt       (invalid data)
    ├── test_case_3.txt       (powers of 2)
    ├── test_case_4.txt       (large numbers)
    ├── test_case_5.txt       (zero and single digits)
    ├── test_case_6.txt       (negative numbers)
    └── test_case_7.txt       (200 numbers)
```

## Technical Details

### Algorithms Implemented

#### Binary Conversion (Decimal to Binary)
Uses repeated division by 2, collecting remainders:
```python
Example: 10 decimal
10 ÷ 2 = 5 remainder 0
5 ÷ 2 = 2 remainder 1
2 ÷ 2 = 1 remainder 0
1 ÷ 2 = 0 remainder 1
Read backwards: 1010
```

#### Hexadecimal Conversion (Decimal to Hexadecimal)
Uses repeated division by 16, collecting remainders:
```python
Example: 255 decimal
255 ÷ 16 = 15 remainder 15 (F)
15 ÷ 16 = 0 remainder 15 (F)
Read backwards: FF
```

Both conversions are implemented **without using built-in Python functions** like `bin()`, `hex()`, or format strings.

### Error Handling
- Invalid data entries are skipped with warnings
- File not found errors are handled gracefully
- Program continues execution after encountering errors
- All invalid entries are logged to console

### Table Formatting
- Dynamic column width adjustment based on content
- Clean ASCII table borders
- Proper alignment for readability

## Requirements Compliance

| Requirement | Status | Description |
|-------------|--------|-------------|
| Req 1 | ✅ | Command-line file parameter |
| Req 2 | ✅ | Binary and hex conversion with manual algorithms |
| Req 3 | ✅ | Invalid data handling implemented |
| Req 4 | ✅ | Named `convertNumbers.py` |
| Req 5 | ✅ | Correct invocation format |
| Req 6 | ✅ | Handles large datasets (tested with 200+ items) |
| Req 7 | ✅ | Execution time displayed and saved |
| Req 8 | ✅ | PEP-8 compliant (10/10 PyLint) |

## Performance
- Handles 200 numbers in < 5ms
- Efficient O(log n) conversion algorithms
- Memory efficient (processes one number at a time)
- Scalable to thousands of numbers

## Mathematical Verification

### Binary System (Base-2)
Each position represents a power of 2:
```
1010 = 1×2³ + 0×2² + 1×2¹ + 0×2⁰
     = 8 + 0 + 2 + 0
     = 10
```

### Hexadecimal System (Base-16)
Each position represents a power of 16:
```
A = 10 (decimal)
1E = 1×16¹ + 14×16⁰
   = 16 + 14
   = 30
```

## Author
**Alejandro Díaz**  
February 2026

## License
Educational project - Free to use for learning purposes
