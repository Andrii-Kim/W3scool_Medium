"""
Count how many times each digit appears in a number.

Instructions
Read a positive number from input.

For each digit (0-9) that appears, print the digit and its count, sorted by digit.

Each line should look like:

[digit]:[count]
"""
# Read the number as a string
num = input().strip()

# Count and print digit frequencies

count = {}

for char in str(num):
    count[char] = count.get(char, 0) +1

for char in count:
    print(char +':' + str(count[char])) 

# Solution from W3School
# counts = [0] * 10
# for ch in num:
#     if '0' <= ch <= '9':
#         counts[int(ch)] += 1
# for i in range(10):
#     if counts[i] > 0:
#         print(str(i) + ":" + str(counts[i]))    