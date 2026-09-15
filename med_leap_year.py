"""
Determine if a given year is a leap year.

Instructions
Read a year from input.

Print Leap year or Not a leap year.

A year is a leap year if:

It is divisible by 4 and
It is NOT divisible by 100, unless it is also divisible by 400
"""
# Read the year
year = int(input())

# Check and print
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")