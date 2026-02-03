# Test Cases Documentation - wordCount.py

## Overview
This document contains the complete test cases for the `wordCount.py` program, which identifies all distinct words in a file and calculates their frequency using manual algorithms.

---

## Test Case 1: Simple Sentence with Repeated Words

### Description
Tests basic word counting functionality with common English sentences.

### Input File: `test_case_1.txt`
```
The quick brown fox jumps over the lazy dog.
The fox is quick and the dog is lazy.
```

### Expected Results
- "the" should appear 4 times (most frequent)
- "fox", "dog", "is", "lazy", "quick" should appear 2 times each
- Other words appear once
- Case-insensitive counting (The = the)

### Actual Output
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
```

### Verification
- ✅ Total words: 18 (correct)
- ✅ Distinct words: 10 (correct)
- ✅ "the" is most frequent with 4 occurrences
- ✅ Words sorted by frequency (descending), then alphabetically
- ✅ Case-insensitive ("The" counted as "the")

### Status: ✅ PASSED
Basic word counting and frequency analysis works correctly.

---

## Test Case 2: Punctuation and Special Characters

### Description
Tests word extraction with various punctuation marks.

### Input File: `test_case_2.txt`
```
Hello, world! How are you?
I'm fine, thank you. What about you?
I'm doing well, thanks!
```

### Expected Results
- Punctuation should be removed (!, ?, ., ,)
- "you" appears 3 times
- "i'm" appears 2 times (apostrophe preserved)
- Words should be clean (no punctuation attached)

### Actual Output
```
Reading data from 'test_data/test_case_2.txt'...
Successfully read 16 words.
Analyzing word frequencies...

======================================================================
WORD FREQUENCY ANALYSIS RESULTS
======================================================================

STATISTICS:
Total words: 16
Distinct words: 13
Most frequent word(s): you
Maximum frequency: 3

WORD FREQUENCY TABLE:
(Sorted by frequency descending, then alphabetically)

+--------+-----------+
| Word   | Frequency |
+--------+-----------+
| you    |         3 |
| i'm    |         2 |
| about  |         1 |
| are    |         1 |
| doing  |         1 |
| fine   |         1 |
| hello  |         1 |
| how    |         1 |
| thank  |         1 |
| thanks |         1 |
| well   |         1 |
| what   |         1 |
| world  |         1 |
+--------+-----------+

Execution Time: 0.000366 seconds
======================================================================
```

### Verification
- ✅ Punctuation correctly removed
- ✅ Apostrophes in contractions preserved ("i'm")
- ✅ "you" counted 3 times (most frequent)
- ✅ All words extracted cleanly

### Status: ✅ PASSED
Punctuation handling works correctly; apostrophes in contractions are preserved.

---

## Test Case 3: Repeated Words with Clear Frequency Differences

### Description
Tests frequency counting with obvious repetition patterns.

### Input File: `test_case_3.txt`
```
test test test test test
hello hello hello
world world
test test
```

### Expected Results
- "test" should appear 7 times (most frequent)
- "hello" should appear 3 times
- "world" should appear 2 times

### Actual Output
```
Reading data from 'test_data/test_case_3.txt'...
Successfully read 12 words.
Analyzing word frequencies...

======================================================================
WORD FREQUENCY ANALYSIS RESULTS
======================================================================

STATISTICS:
Total words: 12
Distinct words: 3
Most frequent word(s): test
Maximum frequency: 7

WORD FREQUENCY TABLE:
(Sorted by frequency descending, then alphabetically)

+-------+-----------+
| Word  | Frequency |
+-------+-----------+
| test  |         7 |
| hello |         3 |
| world |         2 |
+-------+-----------+

Execution Time: 0.000404 seconds
======================================================================
```

### Verification
- ✅ "test" counted 7 times (correct)
- ✅ "hello" counted 3 times (correct)
- ✅ "world" counted 2 times (correct)
- ✅ Sorted by frequency descending

### Status: ✅ PASSED
Frequency counting algorithm is accurate.

---

## Test Case 4: Case-Insensitive Word Counting

### Description
Tests that words are counted case-insensitively.

### Input File: `test_case_4.txt`
```
Python PYTHON python PyThOn
Programming PROGRAMMING programming
Code code CODE
```

### Expected Results
- "python" (all variations) → 4 occurrences
- "programming" (all variations) → 3 occurrences
- "code" (all variations) → 3 occurrences

### Actual Output
```
Reading data from 'test_data/test_case_4.txt'...
Successfully read 10 words.
Analyzing word frequencies...

======================================================================
WORD FREQUENCY ANALYSIS RESULTS
======================================================================

STATISTICS:
Total words: 10
Distinct words: 3
Most frequent word(s): python
Maximum frequency: 4

WORD FREQUENCY TABLE:
(Sorted by frequency descending, then alphabetically)

+-------------+-----------+
| Word        | Frequency |
+-------------+-----------+
| python      |         4 |
| code        |         3 |
| programming |         3 |
+-------------+-----------+

Execution Time: 0.000445 seconds
======================================================================
```

### Verification
- ✅ All variations of "Python" counted as one word (4 total)
- ✅ All variations of "Programming" counted as one word (3 total)
- ✅ All variations of "Code" counted as one word (3 total)
- ✅ Words converted to lowercase for counting

### Status: ✅ PASSED
Case-insensitive counting works perfectly.

---

## Test Case 5: Words with Apostrophes (Contractions)

### Description
Tests handling of contractions and apostrophes within words.

### Input File: `test_case_5.txt`
```
I'm happy because it's sunny today.
Don't worry, we'll be there soon.
She's going to the store. They're coming too.
```

### Expected Results
- Contractions should be preserved (i'm, it's, don't, we'll, she's, they're)
- Each word appears once
- Apostrophes should not break words

### Actual Output
```
Reading data from 'test_data/test_case_5.txt'...
Successfully read 20 words.
Analyzing word frequencies...

======================================================================
WORD FREQUENCY ANALYSIS RESULTS
======================================================================

STATISTICS:
Total words: 20
Distinct words: 20
Most frequent word(s): be, because, coming, don't, going, happy, i'm, 
                       it's, she's, soon, store, sunny, the, there, 
                       they're, to, today, too, we'll, worry
Maximum frequency: 1

WORD FREQUENCY TABLE:
(Sorted by frequency descending, then alphabetically)

+---------+-----------+
| Word    | Frequency |
+---------+-----------+
| be      |         1 |
| because |         1 |
| coming  |         1 |
| don't   |         1 |
| going   |         1 |
| happy   |         1 |
| i'm     |         1 |
| it's    |         1 |
| she's   |         1 |
| soon    |         1 |
| store   |         1 |
| sunny   |         1 |
| the     |         1 |
| there   |         1 |
| they're |         1 |
| to      |         1 |
| today   |         1 |
| too     |         1 |
| we'll   |         1 |
| worry   |         1 |
+---------+-----------+

Execution Time: 0.000439 seconds
======================================================================
```

### Verification
- ✅ All contractions preserved correctly
- ✅ Apostrophes treated as valid word characters
- ✅ All 20 words counted (no breaking at apostrophes)
- ✅ Multiple most frequent words displayed alphabetically

### Status: ✅ PASSED
Apostrophe handling in contractions works correctly.

---

## Test Case 6: Numbers and Special Characters

### Description
Tests handling of numbers and special characters like @ and -.

### Input File: `test_case_6.txt`
```
The year 2024 was great.
I have 3 apples and 2 oranges.
Contact me at email@example.com or call 555-1234.
```

### Expected Results
- Numbers should separate words (not counted as part of words)
- Special characters (@, -) should separate words
- Only alphabetic words should be counted

### Actual Output
```
Reading data from 'test_data/test_case_6.txt'...
Successfully read 17 words.
Analyzing word frequencies...

======================================================================
WORD FREQUENCY ANALYSIS RESULTS
======================================================================

STATISTICS:
Total words: 17
Distinct words: 17
Most frequent word(s): and, apples, at, call, com, contact, email, 
                       example, great, have, i, me, or, oranges, 
                       the, was, year
Maximum frequency: 1

WORD FREQUENCY TABLE:
(Sorted by frequency descending, then alphabetically)

+---------+-----------+
| Word    | Frequency |
+---------+-----------+
| and     |         1 |
| apples  |         1 |
| at      |         1 |
| call    |         1 |
| com     |         1 |
| contact |         1 |
| email   |         1 |
| example |         1 |
| great   |         1 |
| have    |         1 |
| i       |         1 |
| me      |         1 |
| or      |         1 |
| oranges |         1 |
| the     |         1 |
| was     |         1 |
| year    |         1 |
+---------+-----------+

Execution Time: 0.000404 seconds
======================================================================
```

### Verification
- ✅ Numbers (2024, 3, 2, 555-1234) correctly separated from words
- ✅ Email split correctly: "email", "example", "com" as separate words
- ✅ Special characters act as word delimiters
- ✅ Only alphabetic words counted

### Status: ✅ PASSED
Non-alphabetic characters correctly separate words.

---

## Test Case 7: Large Dataset (Scalability)

### Description
Tests program performance with a large text containing 445 words.

### Input File: `test_case_7.txt`
Large text about Python programming (445 words total).

### Expected Results
- Program should handle hundreds of words efficiently
- "python" should be most frequent (appears many times)
- Execution time should be reasonable (< 50ms)
- All distinct words should be identified

### Actual Output (Summary)
```
Reading data from 'test_data/test_case_7.txt'...
Successfully read 445 words.
Analyzing word frequencies...

======================================================================
WORD FREQUENCY ANALYSIS RESULTS
======================================================================

STATISTICS:
Total words: 445
Distinct words: 239
Most frequent word(s): python
Maximum frequency: 67

WORD FREQUENCY TABLE:
(Sorted by frequency descending, then alphabetically)

+------------------+-----------+
| Word             | Frequency |
+------------------+-----------+
| python           |        67 |
| is               |        25 |
| and              |        12 |
| with             |        12 |
| are              |        10 |
| for              |        10 |
| in               |         9 |
| like             |         6 |
| programming      |         5 |
...
(239 distinct words total)
...
+------------------+-----------+

Execution Time: ~0.003 seconds
======================================================================
```

### Verification
- ✅ 445 total words processed
- ✅ 239 distinct words identified
- ✅ "python" correctly identified as most frequent (67 times)
- ✅ Execution time < 5ms (excellent performance)
- ✅ Proper sorting by frequency, then alphabetically

### Status: ✅ PASSED
Program handles large datasets efficiently. Meets requirement 6 for managing files with hundreds to thousands of items.

---

## Summary of Test Results

| Test Case | Description | Status | Key Verification |
|-----------|-------------|--------|------------------|
| 1 | Simple repeated words | ✅ PASSED | Basic counting accurate |
| 2 | Punctuation handling | ✅ PASSED | Punctuation removed correctly |
| 3 | Clear frequency patterns | ✅ PASSED | Frequency counting accurate |
| 4 | Case-insensitive | ✅ PASSED | All case variations counted |
| 5 | Apostrophes/contractions | ✅ PASSED | Contractions preserved |
| 6 | Numbers and special chars | ✅ PASSED | Non-alphabetic separators |
| 7 | Large dataset (445 words) | ✅ PASSED | Scalability verified |

**Total: 7/7 test cases passed ✅**

---

## Requirements Verification

### ✅ Req 1: Command Line Invocation
Program successfully accepts filename as command line parameter.

### ✅ Req 2: Word Identification and Frequency
Program identifies all distinct words and calculates their frequency using manual algorithms (dictionary-based counting, no Counter class).

### ✅ Req 3: Invalid Data Handling
Program handles errors gracefully and continues execution (though most text files don't have "invalid" data in the traditional sense).

### ✅ Req 4: Program Naming
Program is named `wordCount.py` as specified.

### ✅ Req 5: Invocation Format
Program follows format: `python wordCount.py fileWithData.txt`

### ✅ Req 6: Large Dataset Handling
Successfully processes files with hundreds of words (tested with 445 words).

### ✅ Req 7: Execution Time
Execution time is displayed on screen and saved to results file.

### ✅ Req 8: PEP8 Compliance
Code achieves **10.00/10** PyLint score (see `pylint_report.txt`).

---

## Algorithm Details

### Word Extraction Algorithm
```
For each character in line:
    If character is letter or apostrophe:
        Add to current_word
    Else:
        Save current_word to list (if not empty)
        Reset current_word
```

### Frequency Counting Algorithm
```
For each word in word_list:
    If word exists in frequency_dict:
        Increment count
    Else:
        Add word with count = 1
```

### Sorting Algorithm
Manual bubble sort implementation:
- Primary sort: Frequency (descending)
- Secondary sort: Word (alphabetical ascending)

All algorithms implemented manually without using built-in counting or sorting libraries like `Counter` or `sorted()` with complex key functions.

---

## Special Features

### Case-Insensitive Counting
All words converted to lowercase before counting, ensuring "Python", "PYTHON", and "python" are counted as the same word.

### Apostrophe Handling
Apostrophes within words are preserved for contractions:
- "don't" → "don't" (not split)
- "it's" → "it's" (not split)

### Word Delimiters
The following are treated as word delimiters:
- Spaces, tabs, newlines
- Punctuation: . , ! ? ; :
- Numbers: 0-9
- Special characters: @ # $ % & * ( ) - + = [ ] { } / \

### Multiple Most Frequent Words
When multiple words have the same maximum frequency, all are reported alphabetically.

---

## Performance Notes

- Handles 445 words in ~3ms
- Memory efficient (single pass through file)
- O(n) for word extraction and counting
- O(n²) for sorting (bubble sort - educational implementation)
- For production, consider using more efficient sort algorithms

---

**Date**: February 2026  
**Author**: Alejandro Díaz  
**Version**: 1.0
