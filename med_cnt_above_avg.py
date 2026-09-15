"""
Count how many numbers are above the average.

Instructions
The first line of input is a count (how many numbers will follow).

The next lines each have one number.

Calculate the average, then count how many numbers are strictly above it.

Print the count:

Above average: [count]
"""
# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
cnt = 0
total = 0
# Calculate average and count above
for i in range(n):
    total += numbers[i]
avg_value = total / n

for i in range(n):
    if numbers[i] > avg_value:
        cnt +=1

print(f'Above average: {cnt}')