"""
Write a function that doubles every number in a list.

Instructions
The first line of input is a count (how many numbers will follow).

The next lines each have one number.

Write a function that takes an array of numbers and returns a new array where each number is doubled.

Print the doubled numbers, separated by spaces, on one line.
"""

def double_all(numbers):
    scope = []
    # Return a new list with each number doubled
    for i in range(numbers):
        n = int(input())
        scope.append(n * 2)
    print(*scope)    




double_all(5)

# Reolution by W3School
# def double_all(numbers):
#     result = []
#     for x in numbers:
#         result.append(x * 2)
#     return result

# n = int(input())
# numbers = []
# for i in range(n):
#     numbers.append(int(input()))
# result = double_all(numbers)
# print(' '.join(str(x) for x in result))