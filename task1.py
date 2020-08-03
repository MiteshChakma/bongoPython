#developer : Mitesh Chakma
#contact : miteshchakma@gmail.com


def x(d,n):
    s=''
    for i in d:
        s += str(i) +' ' +  str(n) + '\n'
        if type(d[i]) == dict:
            s+= str(x(d[i],n+1))
    return s

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = {
        'key1': 1,
        'key2': {
            'key3': 1,
            'key4': {
                'key5': 4
                }
        }
    }

    print (x(a,1))
