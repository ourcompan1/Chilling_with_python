import random
import time
import easygui
import sys


while True:
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
        time.sleep(0)
        answer1 = input('\n Сыграем еще раз? (да \ нет ) ')
        if answer1 == 'да':
            easygui.msgbox('Погнали !')
        else:
            break

    if lang == 'eng':
        print('Guess!!!')
        guess2 = input('\n heads or tails : ')
        if guess2 == hort_eng:
            print('You are right!')
        else:
            print('You are wrong (((')
        time.sleep(0)
        answer1 = input('\n Play again? (yes \ no) ')
        if answer1 == 'yes':
            easygui.msgbox('Lets go !')
        else:
            break
easygui.msgbox('Ok see you later !')
sys.exit(0)
