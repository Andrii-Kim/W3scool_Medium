"""
Reverse the order of words in a sentence.

Instructions
Read a sentence from input.

Print the words in reverse order.

The words should be separated by spaces, just like the input.

"""
# Read the sentence
sentence = input().strip()
lst = sentence.split(" ")

# Reverse the words and print
result = ' '.join(lst[ : : -1])
print(result)