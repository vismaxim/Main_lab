n = input('Enter year')

y = int(n)
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(y, '  is leap year')
        else: print(y, '  is not leap year')
    else: print(y, '  is leap year')
else: print(y, '  is not leap year')
