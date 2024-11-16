# Summing numbers

def mysum_and_average(args, start=0):
    
    my_sum = 0
    total_numbers = 1
    
    for i in args:
        my_sum += int(i)
        total_numbers += 1

    return my_sum + start, (my_sum + start) / total_numbers

my_sum = mysum_and_average([1, 23], 29)

print(my_sum)


def word_lengths(list_of_words):

    for i in range(len(list_of_words)):
        list_of_words[i] = len(list_of_words[i])

    return min(list_of_words), max(list_of_words), sum(list_of_words) / len(list_of_words)

print(word_lengths(['a', 'nails', 'banana', 'kite', 'jinglebell']))


def integer_sum(args):

    total = 0
    for i in args:
        try:
            total += int(i)
        except:
            pass

    return total

print(integer_sum(['123', '10.23', 'ant']))
