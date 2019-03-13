import json

numbers = list(range(5, 11))

with open('json_test.txt', 'w') as file:
    json.dump(numbers, file)

file.close()

with open('json_test.txt', 'r') as file2:
    new_numbers = json.load(file2)
print(new_numbers)