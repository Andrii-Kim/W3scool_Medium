"""
Print the first N numbers of the Fibonacci sequence.

Instructions
Read a number N from input.

Print the first N numbers of the Fibonacci sequence, separated by spaces.

The Fibonacci sequence starts with 0 and 1. Each next number is the sum of the two before it:

0 1 1 2 3 5 8 13 ...
"""
# Read N
n = int(input())
fib = [0, 1]
# Print the first N Fibonacci numbers
if n < 1: # check that input is a valid
    print('N must be > 0')
elif n == 1: # first Fib number is 0
    fib = [0]
elif n == 2: # second number - 1
    n_fib = 1
    fib = [0, 1]
else:
    prev_2, prev_1 = 0, 1        # prev_2 – N-2 element, prev_1 – N-1
    for i in range(2, n):
        n_fib = prev_2 + prev_1  # calculate a next value of the Fib
        prev_2 = prev_1          # shift prev_2 and prev_1 values
        prev_1 = n_fib
        fib.append(n_fib)

print(*fib)