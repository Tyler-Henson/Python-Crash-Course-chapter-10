<<<<<<< HEAD
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


=======
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


>>>>>>> d6cebe3bac15c85979ad1f97188c8d67d987d0ae
print(answer)