users_vip = ['Tomas', 'Evelina', 'Mindaugas', 'Brigita', 'Petras', 'Birute']
name = input('Enter your name: ')
if name.capitalize() in users_vip:
    print(f'Welcome back {name.capitalize()}')
else:
    print('Welcome')
