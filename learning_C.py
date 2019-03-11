"""
Problem 10-2 of Python Crash Course
"""
lines = []
with open('learning_python.txt') as file:
    lines = file.readlines()
new_lines = []
for line in lines:
    print(line.replace('python', 'C').strip())
    new_lines.append(line.replace('python', 'C').strip())

print(new_lines)
