liste = []
inn = ''
def add(stack):
    x = stack.pop()
    y = stack.pop()
    stack.append(float(y)+float(x))
    return stack


def calculate(stack, op):
    liste = stack
    inn = op
    if inn == '+':
        liste = add(liste)
    else:
        liste.append(inn)
    
    return liste

if __name__ == '__main__':    
    while inn != 'x':
        inn = input('Tall eller operasjon: ')
        liste = calculate(liste, inn)
        print(liste)
