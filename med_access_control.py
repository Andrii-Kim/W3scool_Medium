"""
Determine if a person gets access based on role, age, and membership.

Instructions
Read a role, an age, and a membership status from input.

A person gets access if any of these are true:

Role is admin
Age is 18 or older and membership is yes
Print Access granted or Access denied.
"""

# Read input
role = input().strip()
age = int(input())
membership = input().strip()

# Check and print
if role == 'admin' or (age >= 18 and membership == 'yes'):
    print("Access granted")
else:
    print("Access denied")