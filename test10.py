<<<<<<< HEAD

# opens the file in subfolder text_files of this project
with open('text_files/pi_digits.txt') as number_file:
    lines = number_file.readlines()

full_number =''
for line in lines:
    full_number += line.rstrip()

print(full_number)
print(len(full_number))  # 30 not including 3 and .
pi = float(full_number)
print(pi)


print(lines)
number_file.close()

huge_pi = ''
with open('C:/Users/TiZ/Documents/GitHub/pcc/chapter_10/pi_million_digits.txt') as number_file:
    raw_pi = number_file.readlines()
for line in raw_pi:
    huge_pi += line.strip()
print(huge_pi)

if str(721813) in huge_pi:
    print("number in first million digits of pi")

number_file.close()


try:
    answer =5/1
except ZeroDivisionError:
    print("cant divide by 0")
else:
    print(answer)
=======

# opens the file in subfolder text_files of this project
with open('text_files/pi_digits.txt') as number_file:
    lines = number_file.readlines()

full_number =''
for line in lines:
    full_number += line.rstrip()

print(full_number)
print(len(full_number))  # 30 not including 3 and .
pi = float(full_number)
print(pi)


print(lines)
number_file.close()

huge_pi = ''
with open('C:/Users/TiZ/Documents/GitHub/pcc/chapter_10/pi_million_digits.txt') as number_file:
    raw_pi = number_file.readlines()
for line in raw_pi:
    huge_pi += line.strip()
print(huge_pi)

if str(721813) in huge_pi:
    print("number in first million digits of pi")

number_file.close()


try:
    answer =5/1
except ZeroDivisionError:
    print("cant divide by 0")
else:
    print(answer)
>>>>>>> d6cebe3bac15c85979ad1f97188c8d67d987d0ae
