"""
Read a list of numbers and find the largest one.

Instructions
The first line of input is a count (how many numbers will follow).

The next lines each have one number.

Find the largest number and print it:

Largest: [number]
"""

# Read count
n = int(input())
lst = []
# Read numbers and find the largest
for i in range(n):
    num = int(input())
    lst.append(num)
largest_num = max(lst)

# Print the largest
print(f"Largest: {largest_num}")
