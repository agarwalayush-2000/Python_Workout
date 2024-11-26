# Ubbi Dubbi

def ubbi_dubbi(word):

    ubbi_dubbi_word = ''
    for i in word:
        if i in 'aeiou':
            ubbi_dubbi_word += f'ub{i}'
        else:
            ubbi_dubbi_word += i
    return ubbi_dubbi_word


print(ubbi_dubbi('elk'))


def ubbi_dubbi_capitalize(word):

    ubbi_dubbi_word = ''
    capital = False

    if word[0] in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
        capital = True

    word = word.lower()
    for i in word:
        if i in 'aeiou':
            ubbi_dubbi_word += f'ub{i}'
        else:
            ubbi_dubbi_word += i

    if not capital:
        return ubbi_dubbi_word

    return f'{ubbi_dubbi_word[0].upper()}{ubbi_dubbi_word[1:]}'


print(ubbi_dubbi_capitalize('Elk'))


def encode_url(url):
    
    dummy_url = url.split('/')[:3:2]
    dummy_url = '//'.join(dummy_url)
    url = '/'.join(url.split('/')[3:])
    
    for char in url:
        if not char.isalnum() and char != '/':
            url = url.replace(char, f'%{hex(ord(char))[2:]}')
    
    return dummy_url + f'/{url}'


print(encode_url('https://www.google.com/gdysgfy   / ()'))
