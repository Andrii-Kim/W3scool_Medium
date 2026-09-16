"""
Find all prime factors of a number.

Instructions
Read a number from input (2 or greater).

Find all its prime factors and print them in ascending order, separated by spaces, on one line.

If a prime factor appears more than once, print it that many times.
"""
# Read the number
n = int(input())

# Find and print prime factors
factors = []
d = 2
while d * d <= n:
    while n % d == 0:
        factors.append(str(d))
        n //= d
    d += 1
if n > 1:
    factors.append(str(n))
print(' '.join(factors))