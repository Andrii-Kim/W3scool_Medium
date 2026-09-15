"""
Find the longest word in a sentence.

Instructions
Read a sentence from input.

Find the longest word and print it.

If two words have the same length, print the one that appears first.

Words are separated by single spaces.
"""
# Read the sentence
sentence = input().strip()

# Find and print the longest word
lst = sentence.split()
longest_word = max(lst, key=len)

print(longest_word)