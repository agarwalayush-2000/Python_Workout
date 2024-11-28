# Sorting a string

def string_sort(string):

    return ''.join(sorted(string))


print(string_sort('abracadabra'))


def words_sorted(string):

    string = string.split()
    sorted_string = []
    for i in string:
        sorted_string.append(''.join(sorted(i)))

    return ','.join(sorted_string)


print(words_sorted('Ayush Agarwal'))


def last_word(file):
    
    file = open(file, 'r')
    text = file.read()
    return sorted(text.split(), key=str.casefold)[-1]


print(last_word('Test_Files/Ex-6_1.txt'))


def longest_word(file):
    
    file = open(file, 'r')
    text = file.read()
    return sorted(text.split(), key=len)[-1]


print(longest_word('Test_Files/Ex-6_1.txt'))
