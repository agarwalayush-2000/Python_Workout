# Alphabetizing names
import operator

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}]


def alphabetize_names(list_of_dicts):

    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))


print(alphabetize_names(PEOPLE))


def sort_absolute(numbers):

    return sorted(numbers, key=abs)


print(sort_absolute([1, 2, -3, 4, 5, 6, 7]))


def sort_number_of_vowels(strings):

    return sorted(strings, key=lambda s: sum(1 for char in s if char in 'aeiou'))


print(sort_number_of_vowels(['apple', 'banana', 'custard', 'dragonfruit']))


def sort_by_list_sum(list_of_lists):

    return sorted(list_of_lists, key=sum)


print(sort_by_list_sum([[1, 2, 3], [1, 1, 1]]))
