from random import randint

random_number = randint(1, 15)

attempts = 0
user_input = 0

print('\n You have 5 attempts to guess a number from 1 to 15 !')

while attempts < 5:
    user_input = int(input('\nTry it:  '))
    attempts += 1
    if user_input > random_number:
        print('\n My number is lower :)')
    elif user_input < random_number:
        print('\n My number is bigger :)')
    elif user_input == random_number:
        break
if user_input == random_number:
        print('\nCool ! \nYou guessed the number in '+ str(attempts)+ ' attempts . \nThanks for playing :> ')

else:
        print('\n So sad ur attempts are empty :(')
