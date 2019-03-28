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
