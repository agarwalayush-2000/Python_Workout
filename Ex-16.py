# Dictdiff

DICT1 = {'one': 1, 'two': 2, 'three': 3}
DICT2 = {'one': 1, 'four': 4, 'five': 5}


def dictdiff(dict1, dict2):

    answer = {}
    keys_list = dict1.keys() | dict2.keys()

    for key in keys_list:
        if dict1.get(key) != dict2.get(key):
            answer[key] = [dict1.get(key), dict2.get(key)]

    return answer


print(dictdiff(DICT1, DICT2))


def merge_dicts(*dicts):

    answer = {}

    for d in dicts:
        answer.update(d)

    return answer


print(merge_dicts(DICT1, DICT2))


def even_keys_odd_values(*dict_parameters):

    if len(dict_parameters) % 2:
        return None

    answer = {}

    for key in range(0, len(dict_parameters), 2):
        answer[dict_parameters[key]] = dict_parameters[key+1]

    return answer


print(even_keys_odd_values(1, 2, 3, 4, 5, 6))


def even_key(one, two):
    if one % 2:
        return True
    return False


def dict_partition(dictionary, func):

    answer1 = {}
    answer2 = {}

    for d in dictionary:

        if func(d, dictionary[d]):
            answer1.update({d: dictionary[d]})

        else:
            answer2.update({d: dictionary[d]})

    return answer1, answer2


print(dict_partition({1: 2, 2: 3, 3: 4}, even_key))
