"""
Reverse the digits of a number.

Instructions
Read a positive number from input.

Reverse its digits and print the result as a number (no leading zeros).
"""

# Read the number
n = int(input())

lst = list(map(str, str(n)))

# Reverse the words and print
result = ''.join(lst[ : : -1])
print(int(result))