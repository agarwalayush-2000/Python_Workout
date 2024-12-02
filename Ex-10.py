# Summing anything

def mysum(*items):

    if not items:
        return items

    answer = items[0]
    for i in items[1:]:
        answer += i

    return answer


print(mysum([1, 2, 3], [1, 2, 3]))
print(mysum([1, 2, 3]))
print(mysum((1, 2, 3)))
print(mysum((1, 2, 3), (4, 5, 6)))
print(mysum('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'))


def mysum_bigger_than(*items):

    if not items[1:]:
        return items[1:]

    answer = None
    for i in items[1:]:
        if items[0] < i:
            if answer is not None:
                answer += i
            else:
                answer = i

    if answer is not None:
        return answer

    try:
        return items[0][len(items[0]):]
    except:
        return 0


print(mysum_bigger_than([1, 2, 3], [0, 1, 2]))
print(mysum_bigger_than(10, 2, 3))
print(mysum_bigger_than((1, 2, 3)))
print(mysum_bigger_than((1, 2, 3), (4, 5, 6)))
print(mysum_bigger_than('abc', 'def', 'aaa', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'))


def sum_numeric(*items):

    if not items:
        return items
    
    answer = 0
    
    for i in items:
        
        if type(i) is int:
            answer += i
            continue
        
        if type(i) is str and i.isnumeric():
            answer += int(i)
            
    return answer


print(sum_numeric(10, '2.0', 3))


def dict_addition(dicts):

    final_dict = {}
    for i in dicts:
        for j in i.keys():
            if j not in final_dict.keys():
                final_dict[j] = [i[j]]
            else:
                final_dict[j].append(i[j])

    return final_dict


print(dict_addition([{1: 'a', 2: 'b'}, {1: 'c', 3: 'd'}]))
