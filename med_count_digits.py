"""
Write a function that counts the number of digits in a number.

Instructions
Read a positive number from input.

Write a function that counts how many digits the number has.

Print the result:

Digits: [count]
"""
def count_digits(n):
    # Return the number of digits in n
    lst = list(map(str, str(n)))
    return len(lst)

n = int(input())
print("Digits: " + str(count_digits(n)))
