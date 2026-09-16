"""
Check if a number is a power of 2.

Instructions
Read a positive number from input.

Print Yes if it is a power of 2 (1, 2, 4, 8, 16, ...).

Print No if it is not.
"""
# Read the number
n = int(input())

# Check if power of 2 and print
if n <= 0:
    print("No")
else:
    while n > 1:
        if n % 2 != 0:
            break
        n //= 2
    print("Yes" if n == 1 else "No")
