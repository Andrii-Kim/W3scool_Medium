"""
Calculate the sum of squares from 1 to N.

Instructions
Read a number N from input.

Calculate the sum: 1² + 2² + 3² + ... + N²

Print the result:

Sum: [result]
"""
# Read N
n = int(input())

# Calculate and print sum of squares
total = 0

for i in range(1, n + 1):
    total += (i ** 2)


print(f'Sum: {total}')