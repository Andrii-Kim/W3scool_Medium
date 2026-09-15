"""
Remove consecutive duplicate characters from a string.

Instructions
Read a string from input.

Remove all consecutive duplicate characters, keeping only the first of each group.

Print the result.
"""
# Read the string
# text = input().strip()


# Remove consecutive duplicates and print
# result = "".join(dict.fromkeys(text))
# print(result)


text = input().strip()
result = ''
for ch in text:
    if not result or ch != result[-1]:
        result += ch
print(result)