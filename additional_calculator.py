<<<<<<< HEAD
"""
Problem 10-7 of Python Crash Course
"""
while True:
    print("Lets add some numbers. Enter 'f' to exit")
    num1 = input("the first number?")
    if num1 == 'f':
        break
    num2 = input("the second number?")
    if num2 == 'f':
        break
    answer = ''

    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print('You can only add numbers')
        # pass
    print(answer)
=======
"""
Problem 10-7 of Python Crash Course
"""
while True:
    print("Lets add some numbers. Enter 'f' to exit")
    num1 = input("the first number?")
    if num1 == 'f':
        break
    num2 = input("the second number?")
    if num2 == 'f':
        break
    answer = ''

    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print('You can only add numbers')
        # pass
    print(answer)
>>>>>>> d6cebe3bac15c85979ad1f97188c8d67d987d0ae
