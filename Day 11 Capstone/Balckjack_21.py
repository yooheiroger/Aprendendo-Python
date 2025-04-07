import random
from art import logo


def draw_card(deck):
    '''draw cards of a list [11,2,3,4,5,6,7,8,9,10,10,10,10]'''
    hand_cards = random.choice(deck)
    return hand_cards
def hide_cards_dealer(hand_dealer):
    '''hide 1 card on the beginning of the game (dealer)'''
    hide_hand = hand_dealer.copy()
    hide_hand[0] = '_'
    return hide_hand
def show_hands(new_dealer, your_hands,total_d, total_y):
    '''show the hand and score of the dealer and you'''
    print(f'Dealer hand: {new_dealer} \nDealer score: {total_d}\n')
    print(f'Your hand: {your_hands} \nYour score: {total_y}\n')
    print('------------------------------------------------------------------------------------------------------')

def checking_doubles_a(deck):
    '''check if the hand has double AA'''
    count = 0
    for i in range(len(deck)):
        if i == 11:
            count +=1
    return  count

def sum_cards_hand(deck):
    '''sum the value of the cards'''
    return sum(deck)

def changing_decks_if_doubleaa(deck,count):
    '''replace the double aa'''
    if count > 1:
        changed_deck = deck.copy()
        for i in range(len(deck)):
            if changed_deck[i] == 11:
                changed_deck[i].append(1)
            return changed_deck
    else:
        return deck



print(logo)

deck_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer = []
you = []
print('***Welcome to BlackJack game***\n')
for _ in range(2):
    dealer.append(draw_card(deck_cards))
for _ in range(2):
    you.append(draw_card(deck_cards))
total_you = sum_cards_hand(you)
total_dealer = sum_cards_hand(dealer)
dealer_aa = checking_doubles_a(dealer)# checking if the list have double A
dealer = changing_decks_if_doubleaa(dealer,dealer_aa) # if yes(double a), change the values of 11 to 1
new_hand_dealer = hide_cards_dealer(dealer)
show_hands(new_hand_dealer,you,dealer[1] ,total_you)

should_i_draw = True
while should_i_draw:
    you_new_card = input('Do you want a new card? "yes" or "no": \n').lower()
    if you_new_card == 'yes':
        you.append(draw_card(deck_cards))
        total_you = sum(you)
        show_hands(new_hand_dealer,you,dealer[1],total_you)
        if total_you > 21:
            print('You Lose')
            break
    elif you_new_card == 'no':
       # total_dealer = sum(dealer)
        show_hands(dealer, you,total_dealer, total_you)
        should_i_draw = False
        while total_dealer < total_you:
            dealer.append(draw_card(deck_cards))
            dealer_aa = checking_doubles_a(dealer)  # checking if the list have double A
            dealer = changing_decks_if_doubleaa(dealer, dealer_aa)  # if yes(double a), change the values of 11 to 1
            total_dealer = sum_cards_hand(dealer)
            show_hands(dealer, you,total_dealer, total_you)
            if total_dealer > 21:
                print('The house lose...\nYou WIN!!!!')
                break
    else:
        while you_new_card != 'yes' or you_new_card != 'no':
            print('Wrong answer, tyr again')
            you_new_card = input('Do you want a new card? "yes" or "no": \n').lower()
if total_you == total_dealer:
    print('It is a Draw')
elif total_you < total_dealer <= 21:
    print('The house wins')
elif total_dealer < total_you <= 21:
    print('You Win!!!!')






