name = input('Enter your name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))
vip_users = ['Tomas', 'Evelina', 'Mindaugas', 'Brigita', 'Petras', 'Birute']

if age >= 21:
    if name.capitalize() in vip_users:
        print(f'{name.capitalize()}, welcome to our online casino')
    else:
        print('Welcome to our online casino')
else:
    print('Sorry, you too young.')
