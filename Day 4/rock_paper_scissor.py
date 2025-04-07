import random
from idlelib.pyshell import extended_linecache_checkcache
from random import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_2 = [rock, paper,scissors]

play = int(input('Do you wanna play? 1-yes , 2-No'))
while play == 1:
    you = int(input('0 = rock , 1 = paper, 2 = scissor'))
    pc = random.randrange(len(player_2))
    choice = ''
    pc_choice = ''
    if pc == 0:
        pc_choice = rock
    elif pc == 1:
        pc_choice = paper
    elif pc == 2:
        pc_choice = scissors
    else:
        print('wrong number')

    if you == 0:
        choice = rock
        print('you chose rock')

    elif you == 1:
        choice = paper
        print('you chose paper')

    elif you == 2:
        choice = scissors
        print('you chose scissor')

    else:
        print('wrong number')
    if you == 0 and pc == 0:
        print(choice)
        print()
        print(pc_choice)
        print('Draw')

    elif you == 1 and pc == 1:
        print(choice)
        print()
        print(pc_choice)
        print('Draw')

    elif you == 2 and pc == 2:
        print(choice)
        print()
        print(pc_choice)
        print('Draw')

    elif you == 0 and pc == 1:
        print(choice)
        print()
        print(pc_choice)
        print('you lose')

    elif you == 0 and pc == 2:
        print(choice)
        print()
        print(pc_choice)
        print('you win!!!')
    elif you == 1 and pc == 0:
        print(choice)
        print()
        print(pc_choice)
        print('you win!!!')

    elif you == 1 and pc == 2:
        print(choice)
        print()
        print(pc_choice)
        print('you lose')

    elif you == 2 and pc == 0:
        print(choice)
        print()
        print(pc_choice)
        print('you lose')

    elif you == 2 and pc == 1:
        print(choice)
        print()
        print(pc_choice)
        print('you win!!!')

print('Continue to play? 1 = yes 2 = no')









