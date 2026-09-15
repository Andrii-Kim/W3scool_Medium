"""
Print a pyramid of numbers.

Instructions
Read a number N from input.

Print N rows. Each row contains numbers from 1 up to the row number, separated by spaces.
"""
# Read N
n = int(input())

# Print the number pyramid

for i in range(1, n + 1 ):
    for j in range(1, i + 1):
        if j == i:
            print(j)
        else:
            print(j, end=" ")
   