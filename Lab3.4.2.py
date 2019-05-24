while True:

    n = input('Enter  1st year ')
    if n == 's':
        break
    s = input('Enter  2nd year ')
    ly = []
    for y in range(int(n), int(s)+1):
        if not ((y % 4 != 0) or ((y % 4 == 0) and (y % 100 == 0) and (y % 400 != 0))):
            ly.append(y)
    print(ly)
