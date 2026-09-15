"""
Check if a number is a prime number.

Instructions
Read a number from input (2 or greater).

Print Prime if the number is a prime number.

Print Not prime if it is not.

A prime number is only divisible by 1 and itself.
"""
# Read the number
n = int(input())

# Check if prime and print
flag = False
if n == 0 or n == 1:
    print("Not prime")
elif n > 1:
    # check for factors
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break

    # check if flag is True
    if flag:
        print("Not prime")
    else:
        print("Prime")