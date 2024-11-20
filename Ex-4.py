# Hexadecimal output

def hex_output():
    
    dec_number = 0
    hex_number = input('Enter a hex number for which you want decimal equivalent:')
    ascii_values = list(range(48, 58)) + list(range(97, 103))
    total_digits = 0
    
    for _, number in enumerate(reversed(hex_number)):
        
        if ord(number) not in ascii_values:
            continue
        
        if number.isdigit():
            number = ord(number) - 48
            
        elif number.isalpha():
            print(number)
            number = ord(number) - 87

        dec_number += number * 16 ** total_digits
        total_digits += 1

    print(f'Decimal equivalent of provided hexadecimal number is: {dec_number}')


hex_output()


def name_pattern(name):

    string_to_be_print = ''
    for i in range(len(name)):
        string_to_be_print += name[i]
        print(string_to_be_print)


name_pattern('Ayush')
