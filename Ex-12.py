# Word with most repeated letters
from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_vowel_count(word):
    vowels = 'aeiou'
    vowel_counts = Counter(char for char in word if char in vowels)
    return sum(count for count in vowel_counts.values() if count > 1)


def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)


print(most_repeating_word(WORDS))


def most_repeating_vowel_word(words):

    return sorted(words, key=most_repeating_vowel_count)[-1]


print(most_repeating_vowel_word(WORDS))
