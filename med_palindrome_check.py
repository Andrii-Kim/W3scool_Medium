"""
Check if a word reads the same forwards and backwards.

Instructions
Read a word from input (all lowercase).

Print Yes if the word is a palindrome (reads the same forwards and backwards).

Print No if it is not.

"""
word = input().strip().lower()

# Check if palindrome and print
if word == word[::-1]:
    print("Yes")
else:
    print("No")