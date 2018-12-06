liste = []
inn = ''
def add(stack):
    x = stack.pop()
    y = stack.pop()
    result = float(y)+float(x)
    stack.append(result)
    return stack


def calculate(stack, op):
    liste = stack
    inn = op
    if inn == '+':
        liste = add(liste)
    else:
        liste.append(inn)
    
    str_liste = []
    for e in liste:
        str_liste.append(str(e))    
    return str_liste

if __name__ == '__main__':    
    while inn != 'x':
        inn = input('Tall eller operasjon: ')
        liste = calculate(liste, inn)
        print(liste)
