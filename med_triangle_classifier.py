"""
Classify a triangle based on its side lengths.

Instructions
Read three side lengths from input (three lines).

First check if the sides can form a valid triangle. A triangle is valid if the sum of any two sides is greater than the third side.

If not valid, print Not a triangle.

If valid, print the type:

Equilateral if all three sides are equal
Isosceles if exactly two sides are equal
Scalene if no sides are equal
"""
# Read three sides
a = int(input())
b = int(input())
c = int(input())

# Classify and print
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles") 
    else:
        print("Scalene")
else:
    print("Not a triangle")