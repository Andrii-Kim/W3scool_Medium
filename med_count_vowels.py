"""
Count the number of vowels in a string.

Instructions
Read a string from input.

Count the number of vowels (a, e, i, o, u). Counting is case-insensitive (both "A" and "a" count).

Print the result:

Vowels: [count]
"""
text = input().strip().lower()

cnt = 0
cnt = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')

print(f'Vowels: {cnt}')