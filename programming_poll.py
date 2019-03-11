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
