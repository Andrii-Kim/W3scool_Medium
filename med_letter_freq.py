"""
Count how many times each letter appears in a word.

Instructions
Read a word from input (all lowercase letters).

For each letter that appears, print the letter and its count, sorted by letter.

Each line should look like:

[letter]:[count]
"""
word = input().strip().lower()

# # Count and print letter frequencies
dict_letters = {}


for char in word:
    dict_letters[char] = dict_letters.get(char, 0) +1


for char in dict_letters:
    print(char,':', dict_letters[char])
    # print(char +':' + str(dict_letters[char])) if need without whitespaces


# Solve from W3School
# word = input().strip().lower()
# counts = [0] * 26
# for ch in word:
#     if 'a' <= ch <= 'z':
#         counts[ord(ch) - ord('a')] += 1
# for i in range(26):
#     if counts[i] > 0:
#         print(chr(i + ord('a')) + ":" + str(counts[i]))
