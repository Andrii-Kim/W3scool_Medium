"""
Read a list of numbers and print them in reverse order.

Instructions
The first line of input is a count (how many numbers will follow).

The next lines each have one number.

Print all numbers in reverse order, separated by spaces, on one line.
"""

# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
numbers.reverse()
# Reverse and print
print(*numbers)