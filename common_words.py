"""
Problem 10-10 of Python Crash Course
"""


def word_count(book, word='sawyer'):
    """
    Given a book in text format word_count returns the number of times a word
        appears in it.
    :param book: The text file
    :param word: The word that the function searches for
    :return: The number of times the word appears in the book
    """
    count = 0
    lower_case_lines = []

    try:
        # needed to specify type of txt file encoding
        with open(book, 'r', encoding="utf8") as b:
            lines = b.readlines()

            # make all text lowercase
            for line in lines:
                lower_case_lines.append(line.lower())

            for lower_case_line in lower_case_lines:
                count += lower_case_line.count(word)

    except FileNotFoundError:
        print("File not found")

    return count


if __name__ == '__main__':
    print(word_count('sawyer.txt'))
    print(word_count('dogs.txt', 'fido'))
    print(word_count('saw.txt'))
