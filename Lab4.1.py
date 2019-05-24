import math
# Словник з даними про планети (радіус орбіти та лінійна швидкість
D = {'R': {'Mercury': 58e6, 'Venus': 108e6, 'Earth': 150e6}, 'V': {'Mercury': 47.87, 'Venus': 35.02, 'Earth': 29.79}}


def diy(p):
    '''
    Вираховує кількість днів у році по радіусу орбіти та лінійної швидкості зі словника вище
    '''
    R = D['R'][p]
    V = D['V'][p]
    Y = ((2 * math.pi * R) / V)/(60*60*24)
    return int(Y)


def rep(a, b):
    '''
    порівнює тривалість року на планетах і повертає значення планети з більним роком
    '''
    if diy(a) > diy(b):
        return a
    else:
        return b


while True:
    try:
        P1 = input('Enter planet name 1st ')
        for key in D.keys():
            if key == P1:
                break
    except KeyError:
        print('Unknown planet name')
        continue
while True:
    try:
        P2 = input('Enter planet name 2nd ')

    except NameError:
        print('Unknown planet name')
        continue
Y1 = diy(P1)
Y2 = diy(P2)
print(Y1, 'days in year on', P1)
print(Y2, 'days in year on', P2)
print('year on ', rep(P1, P2), 'is bigger')
