#developer : Mitesh Chakma
#contact : miteshchakma@gmail.com


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)
a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4,
            'user': person_b
        }
    }
}


def turn_dict(d):
    for i in d:
        if type(d[i]) == dict:
            d[i] = turn_dict(d[i])
        try:
            d[i] = d[i].__dict__
            d[i] = turn_dict(d[i])
        except:
            pass
    return d


def x(d, n):
    s = ''
    for i in d:
        if str(i).startswith('key'):
            s += str(i) + ' ' + str(n) + '\n'
        else:
            s += str(i) + ': ' + str(n) + '\n'
        if type(d[i]) == dict:
            s += str(x(d[i], n + 1))

    return s


a = turn_dict(a)
s = x(a, 1)
print(s)
