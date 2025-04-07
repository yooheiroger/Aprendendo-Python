import random
from random import randint



def attempts(easy_hard):
    if easy_hard == 'easy':
        return 10
    else:
        return 5
def generate_numbers():
    number_random = randint(1,100)
    return number_random

def lives_remaining(live,your_number, random_number_ ):
    if your_number != random_number_:
        live-= 1
        return live


def guessing_number(number, random_num):
    if number > random_num:
        print('Too high')
    elif number < random_num:
        print('Too low')
    else:
        print(f'You got it, you guessed the number, {number}')

# select the difficult
select_difficult = True
while select_difficult:
    mode_game = input('Please select the difficult, "easy" or "hard": ').lower()
    if mode_game == 'easy':
        print('Easy mode selected')
        select_difficult = False
    elif mode_game == 'hard':
        print('Hard mode selected')
        select_difficult = False
    else:
        print('Invalid input, try again')
list_numbers = generate_numbers()
random_number = generate_numbers()
lives = attempts(mode_game)
# chose the number
while lives > 0:
    print('Guess the number between 1 and 100 \n')
    print(f'You have {lives} lives remaining\n')
    number_choose = int(input('Type the number: '))
    guessing_number(number_choose, random_number)
    lives = lives_remaining(lives,number_choose,random_number)

    if number_choose == random_number:
        break
    if lives == 0:
        print('GAME OVER')
