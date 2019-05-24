while True:

    n = input('Enter year ')
    if n == 's':
        break
    
    y = int(n)

    if (y % 4 != 0) or ((y % 4 == 0) and (y % 100 == 0) and (y % 400 != 0)):
        print(y, ' is not leap year')
        p = y
        n = y
        while (p % 4 != 0) or ((p % 4 == 0) and (p % 100 == 0) and (p % 400 != 0)):
            p += 1
        while (n % 4 != 0) or ((n % 4 == 0) and (n % 100 == 0) and (n % 400 != 0)):
            n -= 1
        if p - y < y - n:
            print('Closest leap year ', p)
        elif p - y > y - n:
            print('Closest leap year ', n)
        else:
            print('Closest leap years ', n, 'and ', p)

    else:
        print(y, ' is leap year')
