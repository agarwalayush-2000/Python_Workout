# Run timing

from decimal import Decimal

def run_timing():
    total_time = 0
    total_run = 0
    
    while True:
        
        run = input('Enter 10 km run time: ')
        
        if not run:
            break

        total_time += float(run)
        total_run += 1

    if total_run:
        print(f'Average of {total_time/total_run}, over {total_run} runs.')

    else:
        print('Are you sure? You ran at least one time...')


run_timing()


def float_formatter(number, before, after):

    number = number / (10 ** before)
    number = number % 1
    number = number * (10 ** before)

    return f"{number:.{after}f}"


print(float_formatter(1234.123, 1, 3))


def float_with_decimal_class():

    num1 = input('Enter first number:')
    num2 = input('Enter second number')
    num1, num2 = Decimal(num1), Decimal(num2)

    print(num1 + num2)


float_with_decimal_class()
