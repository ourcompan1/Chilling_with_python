import random
hort_rus = random.choice(['орел', 'решка'])
hort_eng = random.choice(['heads', 'tails'])
lang = input('\nВыбери язык ( рус \ eng ) : ')

if lang == 'рус':
    print('Угадай!!!')
    guess1 = input('\n орел или решка : ')
    if guess1 == hort_rus:
        print('ВЕРНО!')
    else:
        print('НЕ ВЕРНО (((')

if lang == 'eng':
    print('Guess!!!')
    guess2 = input('\n heads or tails : ')
    if guess2 == hort_eng:
        print('You are right!')
    else:
        print('You are wrong (((')

