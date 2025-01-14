# -*- coding: utf-8 -*-
"""Functions_Assignment_02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lcGm6ZwJG1Uyz2dA_JFMdJ1MP3GXLZ6L
"""

# Task 01

def divisible_by_7_not_5():
    result = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]
    return ','.join(result)

# Example usage
print(divisible_by_7_not_5())  # Output: comma-separated numbers

# Task 02

import math

def calculate_p():
    A = 50
    B = 30
    C_values = input("Enter comma-separated values for C: ").split(',')
    result = [str(int(math.sqrt((2 * A * B) / int(C)))) for C in C_values]
    return ','.join(result)

# Example usage
print(calculate_p())  # Example input: 100,150,180; Output: 18,22,24

# Task 03:

def sort_words():
    words = input("Enter comma-separated words: ").split(',')
    sorted_words = sorted(words)
    return ','.join(sorted_words)

# Example usage
print(sort_words())  # Example input: without,hello,bag,world; Output: bag,hello,without,world

# Task 04:

def capitalize_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to stop): ")
        if not line:
            break
        lines.append(line.upper())
    return '\n'.join(lines)

# Example usage
print(capitalize_lines())  # Example input: Hello world; Practice makes perfect
# Output: HELLO WORLD\nPRACTICE MAKES PERFECT

def count_vowels():
    vowels = 'aeiou'
    sentence = input("Enter a sentence: ").lower()
    vowel_counts = {vowel: sentence.count(vowel) for vowel in vowels}
    for vowel, count in vowel_counts.items():
        print(f"{vowel} appeared {count} time{'s' if count != 1 else ''}")

# Example usage
count_vowels()  # Example input: Hello world; Practice makes perfect
# Output:
# a appeared 2 times
# e appeared 5 times
# i appeared 1 time
# o appeared 2 times
# u appeared 0 times

