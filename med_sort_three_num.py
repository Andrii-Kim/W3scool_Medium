"""
Read three numbers and print them in ascending order.

Instructions
Read three numbers from input (three lines).

Print them in ascending order (smallest first), separated by spaces, on one line.
"""
# Read three numbers
a = int(input())
b = int(input())
c = int(input())

# Sort and print
lst = [a, b, c]
lst.sort()

print(*lst, sep=" ")