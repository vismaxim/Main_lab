
users_pass = {'user1': 'user1pass', 'user2': 'user2pass', 'user3': 'user3pass'}

while True:
    try:
        us_name = input('enter username')

        us_pass = input('enter password')
        if users_pass[us_name] == us_pass:
            print('Access garanted')
            break
    except KeyError:
        print('unknown name or password')