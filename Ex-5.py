# Pig Latin

def pig_latin(string):

    if string[0] in ['a', 'e', 'i', 'o', 'u']:
        return string + 'way'

    return string[1:] + string[0] + 'ay'

print(pig_latin('ayush'))


def pig_latin_capitalized(string):

    is_capital = False
    
    if string[0] in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
        is_capital = True

    string = pig_latin(string.lower())

    if is_capital:
        return string[0].upper() + string[1:].lower()

    return string


print(pig_latin_capitalized('Ayush'))


def pig_latin_punctuation(string):

    if string[-1] not in 'qwertyuioplkjhgfdsazxcvbnm':
        return pig_latin_capitalized(string[:-1]) + string[-1]

    return pig_latin_capitalized(string)


print(pig_latin_punctuation('H!'))


def pig_latin_alternate(string):

    vowel_set = []

    for i in string:
        if i in 'aeiou':
            vowel_set.append(i)

    vowel_set = set(vowel_set)

    if len(vowel_set) > 1:
        return string + 'way'

    return string[1:] + string[0] + 'ay'


print(pig_latin_alternate('agarwal'))
