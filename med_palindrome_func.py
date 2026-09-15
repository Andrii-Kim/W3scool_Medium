"""
Write a function that checks if a word is a palindrome.

Instructions
Read a word from input (all lowercase).

Write a function that checks if the word is a palindrome (reads the same forwards and backwards).

Print Yes or No.

"""

def is_palindrome(word):

    # Return True if word is a palindrome, False otherwise
    

    # Check if palindrome and print
    if word == word[::-1]:
        print("Yes")
    else:
        print("No")


is_palindrome('racecar')


# def is_palindrome(word):
#     return word == word[::-1]

# word = input().strip().lower()
# print("Yes" if is_palindrome(word) else "No")
