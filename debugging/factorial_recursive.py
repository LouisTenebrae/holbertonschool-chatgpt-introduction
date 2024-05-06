#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given non-negative integer using recursion.

    Parameters:
    - n (int): The integer for which the factorial is to be calculated.

    Returns:
    - int: The factorial of the given integer.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive call to calculate factorial of n-1

f = (factorial(int(sys.argv[1])))
print(f)
