"""
Problem 10-3 of Python Crash Course
"""

filename = 'guest.txt'
with open(filename, 'w') as file:
    response = input('What is your name?')
    file.write(response)