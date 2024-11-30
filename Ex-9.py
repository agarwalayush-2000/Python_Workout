# First-last

def first_last(data):

    return data[:1] + data[-1:]


print(first_last([1, 2, 3, 4]))
print(first_last('1, 2, 3, 4'))
print(first_last('1, 2, 3, ,'))


def square(number):

    return number ** 2


print(square(2))
print(square(2.5))


def largest(iterable):

    return max(iterable)


print(largest([1, 2, 3, 4]))
print(largest('1, 2, 3, 4'))
print(largest('1, 2, 3, ,'))
