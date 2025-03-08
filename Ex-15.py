# Rainfall
from collections import defaultdict


def get_rainfall():

    rainfall = {}

    while True:
        location = input('Enter the location for the recorded rain:')
        if not location:
            break
        rain = input('Enter the amount of rain:')
        rainfall[location] = rainfall.get(location, 0) + int(rain)

    for location, rain in rainfall.items():
        print(f'{location}: {rain}')


get_rainfall()


def total_and_avg_rainfall():

    rainfall = defaultdict(list)

    while True:
        location = input('Enter the location for the recorded rain:')
        if not location:
            break

        rain = int(input('Enter the amount of rain:'))
        rainfall[location].append(rain)

    for location, rain in rainfall.items():
        print(f'{location}: Total rain, {sum(rain)} and Average rain, {sum(rain)/len(rain)}')


total_and_avg_rainfall()


def word_len_dict(path):
    
    word_len = {}
    file = open(path, 'r')
    
    lines = file.readlines()
    
    for line in lines:
        words = line.split(" ")
        for word in words:
            word_len[len(word)] = word_len.get(len(word), 0) + 1
    
    print(word_len)
    
word_len_dict("Test_Files/Ex-15_3.txt")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
