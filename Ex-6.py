# Pig Latin Sentence

def pl_sentence(sentence):

    sentence = sentence.split(' ')
    answer = []
    for word in sentence:
        if word[0] in 'aeiou':
            answer.append(f'{word}way')
        else:
            answer.append(f'{word[1:]}{word[0]}ay')

    return ' '.join(answer)


print(pl_sentence('this is a sentence'))


def sentence_of_nth_words(file):
    
    output = []
    file = open(file, 'r')
    
    for line_number, line in enumerate(file.readlines()):
        if line_number > 9:
            break
        
        if line:
            line = line.split(' ')
            
            if len(line) > line_number:
                output.append(line[line_number])
            
    
    return ' '.join(output)


print(sentence_of_nth_words('Test_Files/Ex-6_1.txt'))


def transpose_string(list_of_string):

    for i in range(len(list_of_string)):
        list_of_string[i] = list_of_string[i].split()

    transposed = []
    for i in range(len(list_of_string)):
        temp = []
        for j in range(len(list_of_string[0])):
            temp.append(list_of_string[j][i])
        transposed.append(' '.join(temp))

    return transposed


print(transpose_string(['abc jkl stu', 'def mno vwx', 'ghi pqr yz']))


def apche_not_found(file):
    
    answer = []
    file = open(file, 'r')
    
    for line in file.readlines():
        
        if '404' in line:
            answer.append(line.split(' ')[0])
    
    return answer


print(apche_not_found(r'Test_Files/Ex-6_3'))
