"""
Problem 10-10 of Python Crash Course
"""


def word_count(book, word):
    count = 0

    with open(book, 'r') as b:
        lines = b.readlines()
        #for line in lines:
            #count += line.count(word)
    #return count


if __name__ == '__main__':
    print(word_count('sawyer.txt', 'the'))
