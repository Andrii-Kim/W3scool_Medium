"""
Calculate the least common multiple of two numbers.

Instructions
Read two positive numbers from input.

Calculate their least common multiple (LCM).

The LCM is the smallest positive number that is divisible by both numbers.

Hint: LCM(a, b) = a * b / GCD(a, b).

Print the result:

LCM: [result]
"""
# Read two numbers
a = int(input())
b = int(input())

#Sve original values
a_orig = a
b_orig = b
# Calculate and print LCM
# Find GCD
while b != 0:
    a, b = b, a % b
    gcd = a

lcm = (a_orig * b_orig)  // gcd
print(f'LCM: {lcm}')