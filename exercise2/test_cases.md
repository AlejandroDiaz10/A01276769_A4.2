# Test Cases Documentation - convertNumbers.py

## Overview
This document contains the complete test cases for the `convertNumbers.py` program, which converts decimal numbers to binary and hexadecimal representations using manual algorithms.

---

## Test Case 1: Small Basic Dataset

### Description
Tests basic conversion functionality with simple decimal numbers.

### Input File: `test_case_1.txt`
```
10
15
20
25
30
```

### Expected Results
| Decimal | Binary | Hexadecimal |
|---------|--------|-------------|
| 10      | 1010   | A           |
| 15      | 1111   | F           |
| 20      | 10100  | 14          |
| 25      | 11001  | 19          |
| 30      | 11110  | 1E          |

### Actual Output
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
```

### Verification
- ✅ 10 decimal = 1010 binary = A hex
- ✅ 15 decimal = 1111 binary = F hex
- ✅ All conversions accurate

### Status: ✅ PASSED
Basic conversion algorithms work correctly for simple numbers.

---

## Test Case 2: Invalid Data Handling

### Description
Tests error handling capability with a dataset containing invalid entries.

### Input File: `test_case_2.txt`
```
100
200
abc
300
invalid
400
500
```

### Expected Results
- Invalid entries should be skipped with warnings
- Program should continue execution
- Valid numbers: [100, 200, 300, 400, 500]

### Actual Output
```
Reading data from 'test_data/test_case_2.txt'...
Warning: Invalid data at line 3: 'abc' - Skipping
Warning: Invalid data at line 5: 'invalid' - Skipping

Total invalid entries skipped: 2

Successfully read 5 numbers.
Converting numbers...

======================================================================
NUMBER CONVERSION RESULTS (Decimal to Binary and Hexadecimal)
======================================================================
Total numbers converted: 5

+---------+-----------+-------------+
| Decimal | Binary    | Hexadecimal |
+---------+-----------+-------------+
| 100     | 1100100   | 64          |
| 200     | 11001000  | C8          |
| 300     | 100101100 | 12C         |
| 400     | 110010000 | 190         |
| 500     | 111110100 | 1F4         |
+---------+-----------+-------------+

Execution Time: 0.000457 seconds
======================================================================
```

### Verification
- ✅ 100 decimal = 64 hex (6×16 + 4 = 100)
- ✅ 200 decimal = C8 hex (12×16 + 8 = 200)
- ✅ 500 decimal = 1F4 hex (1×256 + 15×16 + 4 = 500)

### Status: ✅ PASSED
Program correctly identifies and skips invalid data while continuing execution.

---

## Test Case 3: Powers of 2

### Description
Tests conversion accuracy with powers of 2 (easy to verify in binary).

### Input File: `test_case_3.txt`
```
1
2
4
8
16
32
64
128
256
```

### Expected Results
Powers of 2 should have single '1' bit in binary:
- 1 → 1
- 2 → 10
- 4 → 100
- 8 → 1000
- etc.

### Actual Output
```
Reading data from 'test_data/test_case_3.txt'...
Successfully read 9 numbers.
Converting numbers...

======================================================================
NUMBER CONVERSION RESULTS (Decimal to Binary and Hexadecimal)
======================================================================
Total numbers converted: 9

+---------+-----------+-------------+
| Decimal | Binary    | Hexadecimal |
+---------+-----------+-------------+
| 1       | 1         | 1           |
| 2       | 10        | 2           |
| 4       | 100       | 4           |
| 8       | 1000      | 8           |
| 16      | 10000     | 10          |
| 32      | 100000    | 20          |
| 64      | 1000000   | 40          |
| 128     | 10000000  | 80          |
| 256     | 100000000 | 100         |
+---------+-----------+-------------+

Execution Time: 0.000306 seconds
======================================================================
```

### Verification
- ✅ Each power of 2 has exactly one '1' bit
- ✅ Position of '1' bit corresponds to the exponent
- ✅ Hexadecimal values are correct powers of 2

### Status: ✅ PASSED
Binary conversion algorithm correctly handles powers of 2.

---

## Test Case 4: Large Numbers and Hexadecimal Landmarks

### Description
Tests conversion of larger numbers including important hexadecimal boundaries (FF, FFF, FFFF).

### Input File: `test_case_4.txt`
```
255
256
1000
4095
4096
65535
65536
```

### Expected Results
- 255 = FF (max 8-bit)
- 256 = 100 (min 9-bit)
- 4095 = FFF (max 12-bit)
- 65535 = FFFF (max 16-bit)

### Actual Output
```
Reading data from 'test_data/test_case_4.txt'...
Successfully read 7 numbers.
Converting numbers...

======================================================================
NUMBER CONVERSION RESULTS (Decimal to Binary and Hexadecimal)
======================================================================
Total numbers converted: 7

+---------+-------------------+-------------+
| Decimal | Binary            | Hexadecimal |
+---------+-------------------+-------------+
| 255     | 11111111          | FF          |
| 256     | 100000000         | 100         |
| 1000    | 1111101000        | 3E8         |
| 4095    | 111111111111      | FFF         |
| 4096    | 1000000000000     | 1000        |
| 65535   | 1111111111111111  | FFFF        |
| 65536   | 10000000000000000 | 10000       |
+---------+-------------------+-------------+

Execution Time: 0.000427 seconds
======================================================================
```

### Verification
- ✅ 255 = 11111111 binary = FF hex (8 bits all 1s)
- ✅ 4095 = FFF hex (all F's in 3 hex digits)
- ✅ 65535 = FFFF hex (max 16-bit unsigned)

### Status: ✅ PASSED
Algorithm correctly handles large numbers and hexadecimal boundaries.

---

## Test Case 5: Zero and Single Digits

### Description
Tests edge case of zero and simple single-digit numbers.

### Input File: `test_case_5.txt`
```
0
1
5
7
9
```

### Expected Results
- 0 → 0 (special case)
- Single digits should equal themselves in hex (up to 9)

### Actual Output
```
Reading data from 'test_data/test_case_5.txt'...
Successfully read 5 numbers.
Converting numbers...

======================================================================
NUMBER CONVERSION RESULTS (Decimal to Binary and Hexadecimal)
======================================================================
Total numbers converted: 5

+---------+--------+-------------+
| Decimal | Binary | Hexadecimal |
+---------+--------+-------------+
| 0       | 0      | 0           |
| 1       | 1      | 1           |
| 5       | 101    | 5           |
| 7       | 111    | 7           |
| 9       | 1001   | 9           |
+---------+--------+-------------+

Execution Time: 0.000294 seconds
======================================================================
```

### Verification
- ✅ Zero handled correctly (special case)
- ✅ 5 = 101 binary (correct)
- ✅ 9 = 1001 binary = 9 hex (correct)

### Status: ✅ PASSED
Program correctly handles zero and single-digit edge cases.

---

## Test Case 6: Negative Numbers

### Description
Tests program's handling of negative values.

### Input File: `test_case_6.txt`
```
-10
-5
0
5
10
```

### Expected Results
- Negative numbers should be prefixed with '-' in both binary and hex
- Absolute values should convert correctly

### Actual Output
```
Reading data from 'test_data/test_case_6.txt'...
Successfully read 5 numbers.
Converting numbers...

======================================================================
NUMBER CONVERSION RESULTS (Decimal to Binary and Hexadecimal)
======================================================================
Total numbers converted: 5

+---------+--------+-------------+
| Decimal | Binary | Hexadecimal |
+---------+--------+-------------+
| -10     | -1010  | -A          |
| -5      | -101   | -5          |
| 0       | 0      | 0           |
| 5       | 101    | 5           |
| 10      | 1010   | A           |
+---------+--------+-------------+

Execution Time: 0.000364 seconds
======================================================================
```

### Verification
- ✅ -10 converts to -1010 binary and -A hex
- ✅ Negative sign properly handled
- ✅ Absolute conversion values are correct

### Status: ✅ PASSED
Program correctly handles negative numbers with sign preservation.

---

## Test Case 7: Large Dataset (Scalability)

### Description
Tests program performance with a large dataset (200 numbers from 1 to 200).

### Input File: `test_case_7.txt`
Contains numbers 1 through 200, one per line.

### Expected Results
- All 200 numbers should be converted correctly
- Execution time should be reasonable (< 5ms)
- Sample verifications:
  - 100 = 1100100 binary = 64 hex
  - 150 = 10010110 binary = 96 hex
  - 200 = 11001000 binary = C8 hex

### Actual Output (Sample)
```
Reading data from 'test_data/test_case_7.txt'...
Successfully read 200 numbers.
Converting numbers...

======================================================================
NUMBER CONVERSION RESULTS (Decimal to Binary and Hexadecimal)
======================================================================
Total numbers converted: 200

+---------+----------+-------------+
| Decimal | Binary   | Hexadecimal |
+---------+----------+-------------+
| 1       | 1        | 1           |
| 2       | 10       | 2           |
| 3       | 11       | 3           |
...
| 100     | 1100100  | 64          |
...
| 200     | 11001000 | C8          |
+---------+----------+-------------+

Execution Time: ~0.001 seconds
======================================================================
```

### Verification
- ✅ 200 numbers processed successfully
- ✅ Execution time < 5ms (very efficient)
- ✅ Sample spot-checks all correct

### Status: ✅ PASSED
Program handles large datasets efficiently. Meets requirement 6 for managing files with hundreds to thousands of items.

---

## Summary of Test Results

| Test Case | Description | Status | Key Verification |
|-----------|-------------|--------|------------------|
| 1 | Small basic dataset | ✅ PASSED | Basic conversion accuracy |
| 2 | Invalid data handling | ✅ PASSED | Error handling working |
| 3 | Powers of 2 | ✅ PASSED | Binary patterns correct |
| 4 | Large numbers | ✅ PASSED | Hexadecimal boundaries |
| 5 | Zero and single digits | ✅ PASSED | Edge cases handled |
| 6 | Negative numbers | ✅ PASSED | Sign preservation |
| 7 | Large dataset (200 items) | ✅ PASSED | Scalability verified |

**Total: 7/7 test cases passed ✅**

---

## Requirements Verification

### ✅ Req 1: Command Line Invocation
Program successfully accepts filename as command line parameter.

### ✅ Req 2: Binary and Hexadecimal Conversion
Both conversions are implemented using manual algorithms (division method). No built-in functions like `bin()` or `hex()` are used.

### ✅ Req 3: Invalid Data Handling
Program detects invalid entries, displays warnings, and continues execution as required.

### ✅ Req 4: Program Naming
Program is named `convertNumbers.py` as specified.

### ✅ Req 5: Invocation Format
Program follows format: `python convertNumbers.py fileWithData.txt`

### ✅ Req 6: Large Dataset Handling
Successfully processes datasets with hundreds of items (tested with 200 numbers).

### ✅ Req 7: Execution Time
Execution time is displayed on screen and saved to results file.

### ✅ Req 8: PEP8 Compliance
Code achieves **10.00/10** PyLint score (see `pylint_report.txt`).

---

## Algorithm Verification

### Binary Conversion Algorithm
Uses repeated division by 2, collecting remainders:
```
Example: 10 decimal
10 ÷ 2 = 5 remainder 0
5 ÷ 2 = 2 remainder 1
2 ÷ 2 = 1 remainder 0
1 ÷ 2 = 0 remainder 1
Read backwards: 1010
```

### Hexadecimal Conversion Algorithm
Uses repeated division by 16, collecting remainders:
```
Example: 255 decimal
255 ÷ 16 = 15 remainder 15 (F)
15 ÷ 16 = 0 remainder 15 (F)
Read backwards: FF
```

Both algorithms are implemented manually without using Python's built-in conversion functions.

---

## Additional Notes

- All conversions use manual algorithms (no `bin()`, `hex()`, or format strings)
- Results are displayed in formatted table on console and saved to `ConvertionResults.txt`
- Program handles negative numbers by preserving sign and converting absolute value
- Zero is handled as a special case
- Execution is fast even with large datasets (< 5ms for 200 items)
- Table formatting adapts to column width requirements

---

**Date**: February 2026  
**Author**: Alejandro Díaz  
**Version**: 1.0
