# Restaurant
from datetime import date

MENU = {
    'Tea': 10,
    'Coffee': 15,
    'Biscuits': 20,
    'Lemonade': 25,
    'Sandwich': 20,
    'Water': 20,
    'Bun Maska': 30
}


def restaurant(menu):

    order_total = 0
    while True:
        order = input('Order:')

        if not order:
            print(f'Your total is {order_total}')
            break

        try:
            order_total += menu[order]
            print(f'{order} costs is {menu[order]}, total is {order_total}')
        except:
            print('Are you sure? This item is on the menu!!')


restaurant(MENU)


USER_PASS = {
    'A': '9999',
    'B': '8888',
    'C': '7777',
    'D': '6666',
    'P': '5555'
}


def login(user_pwd):

    usr_name = input('Enter your username: ')
    pwd = input('Enter your password: ').strip()

    if usr_name in user_pwd and user_pwd[usr_name] == pwd:
        print('You logged in successfully!!')

    else:
        print('Why are you using wrong credentials? If you don\'t want to block please use correct credentials.')


login(USER_PASS)


DATEWISE_TEMPERATURE = {
    '01-09-2024': 24,
    '02-09-2024': 25,
    '03-09-2024': 23,
    '04-09-2024': 27,
    '05-09-2024': 22,
    '06-09-2024': 23
}


def temperature_on_dates(dates):

    time = input('Enter the date: ')
    if date in dates:
        print(dates[time])

    else:
        print('You entered wrong date.')


temperature_on_dates(DATEWISE_TEMPERATURE)

BIRTH_DATES = {
    'Dhruv': date(2005, 3, 30),
    'Ayush': date(2000, 8, 19),
    'Mummy': date(1970, 1, 20),
    'Papa': date(1968, 1, 30)
}


def age(family_members):

    name = input('Enter the name of your family member: ')
    print(date.today() - family_members[name])


age(BIRTH_DATES)
