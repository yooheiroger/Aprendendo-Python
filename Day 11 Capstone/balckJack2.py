import random

from pydantic.v1.errors import cls_kwargs

from art import logo
import os

def draw_card(cards):
    hand_cards = random.choice(cards)
    return hand_cards
def hide_cards_dealer(hand_dealer):
    hide_hand = hand_dealer.copy()
    hide_hand[0] = '_'
    return hide_hand
def show_hands(new_dealer, your_hands,total_d, total_y):
    print(f'Dealer hand: {new_dealer} \nDealer score: {total_d}\n')
    print(f'Your hand: {your_hands} \nYour score: {total_y}\n')
    print('------------------------------------------------------------------------------------------------------')

def sum_cards_hand(cards):
    return sum(cards)

def calculate_score(cards):
    """ Calcula a pontuação da mão """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # BlackJack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return 'It is a draw '
    elif computer_score == 0:
        return 'You lose, the opponent has a BlackJack '
    elif user_score == 0:
        return 'BlackJack, You WIN!!!'
    elif  user_score > 21:
        return 'Your score is over 21, You lose'
    elif computer_score > 21:
        return 'The house is over 21, You win!!!'
    elif user_score > computer_score:
        return 'You Win!!!'
    else:
        return 'You lose'

def play_blackjack():
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    you = []
    dealer = []
    new_hand_dealer = dealer.copy()
    is_game_over = True
    your_score = -1
    dealer_score = -1


    for _ in range(2):
        you.append(draw_card(deck))
        dealer.append(draw_card(deck))
        new_hand_dealer = hide_cards_dealer(dealer)

    while is_game_over:
        your_score = calculate_score(you)
        dealer_score = calculate_score(dealer)
        show_hands(new_hand_dealer,you, dealer_score, your_score)

        if your_score == 0 or dealer_score == 0 or your_score == 21:
            is_game_over = False
        else:
            user_should_deal = input('Type "y" to get another card or "n" to pass: ').lower()
            if user_should_deal == 'y':
                you.append(draw_card(deck))
                your_score = calculate_score(you)
                show_hands(new_hand_dealer, you, dealer_score, your_score)
                if your_score > 20:
                    break
            elif user_should_deal == 'n':
                is_game_over = False


    while dealer_score !=0 and dealer_score < 17:
        dealer.append(draw_card(deck))
        dealer_score = calculate_score(dealer)

    show_hands(dealer,you, dealer_score, your_score)

    final_score = compare_score(your_score, dealer_score)
    print(final_score)

while input('Do you want to play again? type "y" to continue or "no" : ').lower() =='y':
    os.system('cls')
    play_blackjack()