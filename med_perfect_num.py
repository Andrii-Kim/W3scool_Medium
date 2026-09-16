"""
Check if a number is a perfect number.

Instructions
Read a positive number from input.

A perfect number equals the sum of its proper divisors (all divisors except itself).

Print Yes if it is a perfect number, or No if it is not.

"""

# Read the number
n = int(input())

# Check and print
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
    
if total == n:
    print("Yes")
else:
    print("No")

