from art import logo, vs
from List_of_famous import data
import random

def pick_famous():
    num1 = int(input('Type 1 or 2: '))
    if num1 == 1:
        print('you choose 1')
        return 1
    elif num1 == 2:
        print('you choose 2')
        return 2
    else:
        print('Wrong number')

def show_celebrity_properties(list_of_famous):
    celebrity1 = random.choice(list_of_famous)
    print(  ' Name:        ',celebrity1['name'],'\n',
            'Description: ',celebrity1['description'],'\n',
            'Country:     ',celebrity1['country'])
    return celebrity1['follower_count']

def comparing_results(number,cele1,cele2):
    if cele1 > cele2:
        if number == 1:
            print('That is the correct answer')
            print('******************************************************************************************************************************')
            return 1
        else:
            print('Wrong answer')
            print('\n'*5)
            return False
    else:
        if number == 2:
            print('That is the correct answer')
            print('******************************************************************************************************************************')

            return 1
        else:
            print('Wrong answer!')
            print('\n' * 5)
            return False


def game():
    score1 = 0
    guess_famous = True
    print(logo)
    print('Wellcome to the Higher or Lower game.\n ')
    print('You need to guess who has te most follower on Instagram\n')


    while guess_famous :
        print(f'Your score is: {score1}\n')
        # randomly chose someone of the list of the celebrities
        c1 = show_celebrity_properties(data)
        print(vs)
        c2 = show_celebrity_properties(data)
        print(c1)
        print(c2)

        print()
        # Chose the famous 1 or 2
        num = pick_famous()
        while num != 1 and num !=2:
            num = pick_famous()

        # Comparing the answer, what you choose and the list who has more followers
        choice = comparing_results(num,c1,c2)
        print(choice)
        if choice == False:
            guess_famous = False
        else:
            score1 +=1

# THE GAME START HERE
game()