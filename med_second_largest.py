"""
Find the second largest number in a list.

Instructions
The first line of input is a count (how many numbers will follow).

The next lines each have one number.

Find the second largest number and print:

Second largest: [number]
If two numbers share the highest value, the second largest is still that same value.

"""
# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Find and print the second largest
numbers.sort()

print(f'Second largest: {numbers[-2]}')
