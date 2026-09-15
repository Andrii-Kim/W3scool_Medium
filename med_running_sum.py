"""
Print the running (cumulative) sum of a list of numbers.

Instructions
The first line of input is a count (how many numbers will follow).

The next lines each have one number.

Print the running sum after each number, separated by spaces, on one line.

The running sum is the total of all numbers seen so far.
"""
# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

res = 0
lst = []
for i in range(n):
    res += numbers[i]
    lst.append(res)
# Print running sum
print(*lst)