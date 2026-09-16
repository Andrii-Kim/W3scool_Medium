"""
Find the character that appears most often in a string.

Instructions
Read a word from input (all lowercase letters).

Find the character that appears most often.

If there is a tie, print the one that comes first alphabetically.

Print the letter.

"""
word = input().strip().lower()

# Find and print the most common character - Solution from W3School
counts = [0] * 26
for ch in word:
    if 'a' <= ch <= 'z':
        counts[ord(ch) - ord('a')] += 1
max_count = max(counts)
for i in range(26):
    if counts[i] == max_count:
        print(chr(i + ord('a')))
        break