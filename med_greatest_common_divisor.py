"""
Find the greatest common divisor (GCD) of two numbers.

Instructions
Read two numbers from input.

Find the greatest common divisor (GCD). This is the largest number that divides both numbers evenly.

Print the result:

GCD: [result]
"""
# Read two numbers
a = int(input())
b = int(input())

# Find the GCD
while b != 0:
    a, b = b, a % b

    

# Print the result
print(f'GCD: {a}')
