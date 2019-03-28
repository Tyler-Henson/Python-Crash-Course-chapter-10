"""
Problem 10-8 of Python Crash Course
"""


def print_file(filename):
    try:
        with open(filename) as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")

    file.close()


if __name__ == '__main__':
    print_file('cats.txt')
    print_file('dogs.txt')
    print_file('dos.txt')
    print_file('text_files/pi_digits.txt')
