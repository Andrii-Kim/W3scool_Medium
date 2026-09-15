"""
Calculate the sum of all digits in a number.

Instructions
Read a positive number from input.

Calculate the sum of its digits and print:

Digit sum: [result]
"""

# Read the number
n = int(input())

# Calculate digit sum and print
result = 0
lst = list(map(int, str(n)))

if n >=0:
    for i in range(len(lst)):
        result += lst[i] 


print(f"Digit sum: {result}")