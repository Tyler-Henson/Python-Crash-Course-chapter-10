"""
Problem 10-10 of Python Crash Course
"""


def word_count(book, word='sawyer'):
    count = 0
    lower_case_lines = []
    try:
        with open(book, 'r', encoding="utf8") as b:
            lines = b.readlines()
            for line in lines:
                lower_case_lines.append(line.lower())

            for lower_case_line in lower_case_lines:
                count += lower_case_line.count(word)
        return count
    except FileNotFoundError:
        print("File not found")
        return 0


if __name__ == '__main__':
    print(word_count('sawyer.txt'))
    print(word_count('dogs.txt'))
    print(word_count('saw.txt'))
