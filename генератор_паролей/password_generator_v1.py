import random
password0 = random.randint(66, 666666)
password1 = random.randint(77, 777777)
password2 = random.randint(88, 888888)
password3 = random.randint(99, 999999)
password01 = int(password0) + int(password1) + int(password2) + int(password3)
password = password01 * 777
hello = input('\nЧто бы сгенерировать пароль введите ваше имя : ')
print('\nOkay', hello, '\n\nВаш пароль ---> ', password)

# придумал за пару минут . Так себе . Во 2 версии надо сделать с буквами и продумать генерацию чисел в последовательности.