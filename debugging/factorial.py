#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return 1 if n == 0 else n * factorial(n - 1)

try:
    n = int(sys.argv[1])
except (IndexError, ValueError):
    print("Usage: python script.py <integer>")
    sys.exit(1)

print(factorial(n))