"""
Convert a day number to a day name.

Instructions
Read a number from input (1 to 7).

Print the name of the day:

1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
6 = Saturday
7 = Sunday
If the number is not 1-7, print Invalid.

"""
# Read the day number
day = int(input())

# Print the day name
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid")
