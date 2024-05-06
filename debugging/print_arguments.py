#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

# Check if there are command-line arguments
if len(sys.argv) > 1:
    # Calculate factorial
    f = factorial(int(sys.argv[1]))
    print(f)

    # Print remaining command-line arguments on separate lines
    for arg in sys.argv[2:]:
        print(arg)
else:
    print("Usage: python script.py <integer>")