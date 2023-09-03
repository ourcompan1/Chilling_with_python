import random

attempts = 0
name = input('Привет, представься - ')

number = random.randint(1, 10)
print(name, ', твоя задача угадать число от 1 до 10. У тебя 3 попытки .')

while attempts < 3:
    guess = int(input('\nУ Г А Д А Й : '))
    attempts += 1
    if guess < number:
        print('\nТвое число меньше загаданного .')
    if guess > number:
        print('\nТвое число больше загаданного .')
    if guess == number:
        break
if guess == number:
    print('\nТы удачлив ! Угадал :) ')
else:
    print('\nНЕ УГАДАЛ .')