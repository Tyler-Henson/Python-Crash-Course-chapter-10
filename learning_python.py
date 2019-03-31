<<<<<<< HEAD
"""
Problem 10-1 of Python Crash Course
"""
lines = []
with open('learning_python.txt') as f:
    print(f.read())
    f.seek(0)
    lines = f.readlines()

for line in lines:
    print(line.rstrip())
=======
"""
Problem 10-1 of Python Crash Course
"""
lines = []
with open('learning_python.txt') as f:
    print(f.read())
    f.seek(0)
    lines = f.readlines()

for line in lines:
    print(line.rstrip())
>>>>>>> d6cebe3bac15c85979ad1f97188c8d67d987d0ae
