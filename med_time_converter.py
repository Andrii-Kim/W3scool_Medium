"""
Convert a number of seconds into hours, minutes, and seconds.

Instructions
Read a number of total seconds from input.

Convert it to hours, minutes, and seconds.

Print the result like this:

[h]h [m]m [s]s
"""

# Read total seconds
total = int(input())

# Calculate hours, minutes, seconds

hour = total // 3600
minutes = (total % 3600) // 60
seconds = (total % 60)

# Print the result
print(f'{hour}h {minutes}m {seconds}s')
