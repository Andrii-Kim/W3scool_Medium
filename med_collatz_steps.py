"""
Count the steps to reach 1 using the Collatz sequence.

Instructions
Read a positive number from input.

Repeat these steps until the number becomes 1:

If the number is even, divide it by 2
If the number is odd, multiply it by 3 and add 1
Count how many steps it takes and print:

Steps: [count]
"""
# Read the number
n = int(input())

count = 0

# Count steps to reach 1
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1    
    count += 1    
    
print(f'Steps: {count}')