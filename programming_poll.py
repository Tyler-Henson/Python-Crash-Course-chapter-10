<<<<<<< HEAD
"""
Problem 10-5 of Python Crash Course
"""

filename = 'programming_poll.txt'
reasons = ''
with open(filename, 'a') as f:
    while reasons != 'f':
        reasons = input("why do you like programming? Enter 'f' to exit.")
        if reasons != 'f':
            f.write(reasons + '\n')
=======
"""
Problem 10-5 of Python Crash Course
"""

filename = 'programming_poll.txt'
reasons = ''
with open(filename, 'a') as f:
    while reasons != 'f':
        reasons = input("why do you like programming? Enter 'f' to exit.")
        if reasons != 'f':
            f.write(reasons + '\n')
>>>>>>> d6cebe3bac15c85979ad1f97188c8d67d987d0ae
