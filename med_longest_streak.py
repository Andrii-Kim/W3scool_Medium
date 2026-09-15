"""
Find the longest consecutive streak of the same number.

Instructions
The first line of input is a count (how many numbers will follow).

The next lines each have one number.

Find the longest streak of consecutive identical numbers.

Print the result:

Longest streak: [length]
"""
# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Find longest streak and print
cnt = []

for i in numbers:
   cnt.append(numbers.count(i))
m = max(cnt)

print(f'Longest streak: {m}')

# Solution from W3School
# n = int(input())
# numbers = []
# for i in range(n):
#     numbers.append(int(input()))
# max_streak = 1
# streak = 1
# for i in range(1, n):
#     if numbers[i] == numbers[i - 1]:
#         streak += 1
#         if streak > max_streak:
#             max_streak = streak
#     else:
#         streak = 1
# print("Longest streak: " + str(max_streak))
