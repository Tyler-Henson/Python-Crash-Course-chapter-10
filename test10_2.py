<<<<<<< HEAD
import json

numbers = list(range(5, 11))

with open('json_test.txt', 'w') as file:
    json.dump(numbers, file)

file.close()

with open('json_test.txt', 'r') as file2:
    new_numbers = json.load(file2)
=======
import json

numbers = list(range(5, 11))

with open('json_test.txt', 'w') as file:
    json.dump(numbers, file)

file.close()

with open('json_test.txt', 'r') as file2:
    new_numbers = json.load(file2)
>>>>>>> d6cebe3bac15c85979ad1f97188c8d67d987d0ae
print(new_numbers)