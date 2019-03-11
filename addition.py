"""
Problem 10-6 of Python Crash Course
"""

num1 = input("the first number?")
num2 = input("the second number?")
answer = ''
try:
    answer = int(num1) + int(num2)
except ValueError:
    print('You can only add numbers')
    # pass


print(answer)