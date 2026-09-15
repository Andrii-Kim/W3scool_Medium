"""
Write a recursive function to sum numbers from 1 to N.

Instructions
Read a positive number N from input.

Write a recursive function that calculates the sum of all numbers from 1 to N.

The function must call itself (no loops allowed in the function).

Print the result:

Sum: [result]
"""
def recursive_sum(n):
    result = 0
    # Base case and recursive case
    for i in range(n):
        i += 1
        result +=i
    return result


n = int(input())
print("Sum: " + str(recursive_sum(n)))
