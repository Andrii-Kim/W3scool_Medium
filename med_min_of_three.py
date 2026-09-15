"""
Write a function that returns the smallest of three numbers.

Instructions
Read three numbers from input (three lines).

Write a function that takes three numbers and returns the smallest one.

Print the result:

Min: [result]
"""
def min_of_three(a, b, c):
    # Return the smallest of the three numbers
    return min(a, b, c)

a = int(input())
b = int(input())
c = int(input())
print("Min: " + str(min_of_three(a, b, c)))
