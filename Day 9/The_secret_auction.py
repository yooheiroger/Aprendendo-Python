import os

anyone_else = True
auction = {}


def find_highest_bidder(auction):
    max_value = max(auction.values())
    for name1, bid_high  in auction.items():
        if bid_high == max_value:
            print(f'The highest bid was: {name1}, with value: {bid_high}')
def find_highest_without_max(auction):
    highest_value = 0
    for bidder in auction:
        bid_amount = auction[bidder]
        if highest_value < bid_amount:
            highest_value = bid_amount

    print(f'The winner is : {bidder}, the value: {highest_value}')


while anyone_else:
    name = input('Please, type your name: \n')
    bid = float(input('Type your bid: \n'))
    auction[name] = bid
    yes_or_no = input('There is someone else in the room, would like to bid? "yes" or "no"\n').lower()
    if yes_or_no == 'no':
        anyone_else = False
    elif yes_or_no == 'yes':
        print('Type again the name and the bid')
    else:
        while yes_or_no != 'yes' and yes_or_no != 'no':
            print('Incorrect type, try again')
            yes_or_no = input('There is someone else in the room, would like to bid? "yes" or "no"\n').lower()
    os.system('cls')

find_highest_without_max(auction)








