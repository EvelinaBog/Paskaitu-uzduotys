while True:
    number1 = float(input('Enter your first number: '))
    symbol = input('Enter symbol (+, -, /, *, **): ')
    number2 = float(input('Enter your second number: '))

    if symbol == '+':
        print(f'{number1} {symbol} {number2} = {number1 + number2}')
    elif symbol == '-':
        print(f'{number1} {symbol} {number2} = {number1 - number2}')
    elif symbol == '/':
        print(f'{number1} {symbol} {number2} = {number1 / number2}')
    elif symbol == '*':
        print(f'{number1} {symbol} {number2} = {number1 * number2}')
    elif symbol == '**':
        print(f'{number1} {symbol} {number2} = {number1 ** number2}')
        break
    else:
        print('Invalid value')



