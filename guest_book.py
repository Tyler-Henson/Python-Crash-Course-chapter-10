<<<<<<< HEAD
"""
Problem 10-4 of Python Crash Course
"""

filename = 'guest_book.txt'
with open(filename, 'w') as file:
    while True:
        name = input("Sign the guest book please. enter 'f' to exit")
        if name == 'f':
            break
        else:
            file.write(name + '\n')
=======
"""
Problem 10-4 of Python Crash Course
"""

filename = 'guest_book.txt'
with open(filename, 'w') as file:
    while True:
        name = input("Sign the guest book please. enter 'f' to exit")
        if name == 'f':
            break
        else:
            file.write(name + '\n')
>>>>>>> d6cebe3bac15c85979ad1f97188c8d67d987d0ae
