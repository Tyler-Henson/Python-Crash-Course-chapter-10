<<<<<<< HEAD
"""
Problem 10-11 of Python Crash Course
"""
import json
filename = 'favorite_number.txt'


with open(filename, 'r') as read_file:
    prev_fav_number = json.load(read_file)
print("Your last fav number was: " + prev_fav_number)
read_file.close()


fav_number = input("What is your favorite number? ")
with open(filename, 'w') as file:
    json.dump(fav_number, file)
file.close()
=======
"""
Problem 10-11 of Python Crash Course
"""
import json
filename = 'favorite_number.txt'


with open(filename, 'r') as read_file:
    prev_fav_number = json.load(read_file)
print("Your last fav number was: " + prev_fav_number)
read_file.close()


fav_number = input("What is your favorite number? ")
with open(filename, 'w') as file:
    json.dump(fav_number, file)
file.close()
>>>>>>> d6cebe3bac15c85979ad1f97188c8d67d987d0ae
