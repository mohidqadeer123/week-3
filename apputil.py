import seaborn as sns
import pandas as pd


# update/add code below ...

#Exercise 1: Write a recursive function (fibonacci) that, given n, will give the nth number of the Fibonacci Series.

def fibonacci(n):
    """Using recursion to find the nth number in the Fibonacci series"""
    # Input validation
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("n has to be a positive integer")

    # Base cases
    if n in {0,1}:
        return n

    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)

    # Test cases
    print(fibonacci(9))  # 34 