# Test Cases Documentation - computeStatistics.py

## Overview
This document contains the complete test cases for the `computeStatistics.py` program, which computes descriptive statistics (mean, median, mode, variance, and standard deviation) from a file containing numbers.

---

## Test Case 1: Small Basic Dataset

### Description
Tests basic functionality with a small dataset of 5 sequential numbers.

### Input File: `test_case_1.txt`
```
5
10
15
20
25
```

### Expected Results
- **Count**: 5 numbers
- **Mean**: 15.0
- **Median**: 15.0
- **Mode**: No mode (all values appear once)
- **Variance**: 50.0
- **Standard Deviation**: ~7.071

### Actual Output
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
```

### Status: ✅ PASSED
All calculations are correct. Program handles basic dataset properly.

---

## Test Case 2: Invalid Data Handling

### Description
Tests error handling capability with a dataset containing invalid entries.

### Input File: `test_case_2.txt`
```
10
20
abc
30
invalid
40
50
```

### Expected Results
- Invalid entries should be skipped with warnings
- Program should continue execution
- Valid numbers: [10, 20, 30, 40, 50]
- **Count**: 5 numbers
- **Mean**: 30.0
- **Median**: 30.0
- **Variance**: 200.0
- **Standard Deviation**: ~14.142

### Actual Output
```
Reading data from 'test_data/test_case_2.txt'...
Warning: Invalid data at line 3: 'abc' - Skipping
Warning: Invalid data at line 5: 'invalid' - Skipping

Total invalid entries skipped: 2

Successfully read 5 numbers.

==================================================
DESCRIPTIVE STATISTICS RESULTS
==================================================
Count of numbers: 5
Mean: 30.000000
Median: 30.000000
Mode: No mode (all values appear once)
Variance: 200.000000
Standard Deviation: 14.142136

Execution Time: 0.000813 seconds
==================================================
```

### Status: ✅ PASSED
Program correctly identifies and skips invalid data while continuing execution. Displays appropriate warnings as required.

---

## Test Case 3: Mode Detection

### Description
Tests the mode calculation with a dataset containing repeated values.

### Input File: `test_case_3.txt`
```
5
5
5
10
10
15
20
```

### Expected Results
- **Count**: 7 numbers
- **Mode**: 5 (appears 3 times)
- **Mean**: 10.0
- **Median**: 10.0
- **Variance**: ~28.571
- **Standard Deviation**: ~5.345

### Actual Output
```
Reading data from 'test_data/test_case_3.txt'...
Successfully read 7 numbers.

==================================================
DESCRIPTIVE STATISTICS RESULTS
==================================================
Count of numbers: 7
Mean: 10.000000
Median: 10.000000
Mode: 5.0
Variance: 28.571429
Standard Deviation: 5.345225

Execution Time: 0.000603 seconds
==================================================
```

### Status: ✅ PASSED
Program correctly identifies the mode (most frequent value) in the dataset.

---

## Test Case 4: Large Dataset (Scalability)

### Description
Tests program performance with a large dataset (300 numbers from 1 to 300).

### Input File: `test_case_4.txt`
Contains numbers 1 through 300, one per line.

### Expected Results
- **Count**: 300 numbers
- **Mean**: 150.5
- **Median**: 150.5
- **Mode**: No mode
- **Variance**: ~7499.917
- **Standard Deviation**: ~86.602

### Actual Output
```
Reading data from 'test_data/test_case_4.txt'...
Successfully read 300 numbers.

==================================================
DESCRIPTIVE STATISTICS RESULTS
==================================================
Count of numbers: 300
Mean: 150.500000
Median: 150.500000
Mode: No mode (all values appear once)
Variance: 7499.916667
Standard Deviation: 86.602059

Execution Time: 0.000889 seconds
==================================================
```

### Status: ✅ PASSED
Program handles hundreds of items efficiently (execution time < 1ms). Meets requirement 6 for managing large datasets.

---

## Test Case 5: Decimal Numbers

### Description
Tests program's ability to handle floating-point numbers.

### Input File: `test_case_5.txt`
```
3.14
2.718
1.414
2.236
1.732
```

### Expected Results
- **Count**: 5 numbers
- **Mean**: ~2.248
- **Median**: 2.236
- **Mode**: No mode
- **Variance**: ~0.396
- **Standard Deviation**: ~0.629

### Actual Output
```
Reading data from 'test_data/test_case_5.txt'...
Successfully read 5 numbers.

==================================================
DESCRIPTIVE STATISTICS RESULTS
==================================================
Count of numbers: 5
Mean: 2.248000
Median: 2.236000
Mode: No mode (all values appear once)
Variance: 0.395704
Standard Deviation: 0.629050

Execution Time: 0.000837 seconds
==================================================
```

### Status: ✅ PASSED
Program correctly handles decimal/floating-point numbers with proper precision.

---

## Test Case 6: Negative Numbers

### Description
Tests program's handling of negative values and zero.

### Input File: `test_case_6.txt`
```
-10
-5
0
5
10
15
20
```

### Expected Results
- **Count**: 7 numbers
- **Mean**: 5.0
- **Median**: 5.0
- **Mode**: No mode
- **Variance**: 100.0
- **Standard Deviation**: 10.0

### Actual Output
```
Reading data from 'test_data/test_case_6.txt'...
Successfully read 7 numbers.

==================================================
DESCRIPTIVE STATISTICS RESULTS
==================================================
Count of numbers: 7
Mean: 5.000000
Median: 5.000000
Mode: No mode (all values appear once)
Variance: 100.000000
Standard Deviation: 10.000000

Execution Time: 0.000591 seconds
==================================================
```

### Status: ✅ PASSED
Program correctly handles negative numbers and calculates statistics accurately.

---

## Test Case 7: Multiple Modes (Multimodal Distribution)

### Description
Tests mode detection when multiple values have the same highest frequency.

### Input File: `test_case_7.txt`
```
1
1
1
2
3
3
3
5
5
5
```

### Expected Results
- **Count**: 10 numbers
- **Mode**: Multiple modes (1, 3, and 5 each appear 3 times)
- **Mean**: 2.9
- **Median**: 3.0
- **Variance**: ~2.49
- **Standard Deviation**: ~1.578

### Actual Output
```
Reading data from 'test_data/test_case_7.txt'...
Successfully read 10 numbers.

==================================================
DESCRIPTIVE STATISTICS RESULTS
==================================================
Count of numbers: 10
Mean: 2.900000
Median: 3.000000
Mode: Multiple modes: 1.0, 3.0, 5.0
Variance: 2.490000
Standard Deviation: 1.577973

Execution Time: 0.000453 seconds
==================================================
```

### Status: ✅ PASSED
Program correctly identifies and reports all modes when multiple values have the same frequency.

---

## Summary of Test Results

| Test Case | Description | Status | Notes |
|-----------|-------------|--------|-------|
| 1 | Small basic dataset | ✅ PASSED | Basic functionality verified |
| 2 | Invalid data handling | ✅ PASSED | Error handling working correctly |
| 3 | Mode detection | ✅ PASSED | Correctly identifies mode |
| 4 | Large dataset (300 items) | ✅ PASSED | Scalability verified |
| 5 | Decimal numbers | ✅ PASSED | Floating-point precision correct |
| 6 | Negative numbers | ✅ PASSED | Handles negative values properly |
| 7 | Multiple modes | ✅ PASSED | Multimodal detection working |

**Total: 7/7 test cases passed ✅**

---

## Requirements Verification

### ✅ Req 1: Command Line Invocation
Program successfully accepts filename as command line parameter.

### ✅ Req 2: Statistics Computation
All descriptive statistics (mean, median, mode, standard deviation, variance) are computed correctly using manual algorithms (no libraries used).

### ✅ Req 3: Invalid Data Handling
Program detects invalid entries, displays warnings, and continues execution as required.

### ✅ Req 4: Program Naming
Program is named `computeStatistics.py` as specified.

### ✅ Req 5: Invocation Format
Program follows format: `python computeStatistics.py fileWithData.txt`

### ✅ Req 6: Large Dataset Handling
Successfully processes datasets with hundreds of items (tested with 300 numbers).

### ✅ Req 7: Execution Time
Execution time is displayed on screen and saved to results file.

### ✅ Req 8: PEP8 Compliance
Code achieves **10.00/10** PyLint score (see `pylint_report.txt`).

---

## Additional Notes

- All calculations are performed using manual algorithms (no NumPy, statistics module, etc.)
- Results are displayed both on console and saved to `StatisticsResults.txt`
- Square root calculation uses Newton's method for standard deviation
- Program handles edge cases (empty mode, single value, all identical values)
- Execution is fast even with large datasets (< 1ms for 300 items)

---

**Date**: February 2026  
**Author**: Student  
**Version**: 1.0