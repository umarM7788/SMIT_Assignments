# -*- coding: utf-8 -*-
"""Functions_Assignment_01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18kYsy3dwUgSdiwB9nM5Ue_VjIVCW2cn3
"""

# Question #01:

def max_of_three(a, b, c):
    return max(a, b, c)

# Example usage
print(max_of_three(3, 6, -5))

# Question #02:

def sum_list(numbers):
    return sum(numbers)


print(sum_list([8, 2, 3, 0, 7]))

# Question #03

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(multiply_list([8, 2, 3, -1, 7]))

# Quesiton #04

def reverse_string(s):
    return s[::-1]


print(reverse_string("1234abcd"))

# Question #05

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
