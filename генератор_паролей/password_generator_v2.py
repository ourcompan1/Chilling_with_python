import random
import sys

x = 0
while x == 0:
    try:
        symbols = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        symbols1 = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        print(
            '\nВас привествует ГЕНЕРАТОР ПАРОЛЕЙ 3000 \n\nЯ генерирую пароли как и с цифрами , так и с буквами , а так же с другими символами .')

        inp0 = str(input('\nИспользовать специальные символы ? ( да \ нет ) : '))
        inp1 = int(input('\nВведите длинну пароля : '))
        if inp0 == 'да':
            for i in range(inp1):
                password = random.choice(symbols)
                print(password, end='')
        elif inp0 == 'нет':
            for n in range(inp1):
                password = random.choice(symbols1)
                print(password, end='')
        else:
            print('\nПрограмма не распознала вашего ответа :( \nДопускается только да\нет!')
            sys.exit(0)
    except ValueError:
        print('\nВы ввели вместо цифры другие символы !')
    finally:
        sys.exit(0)





