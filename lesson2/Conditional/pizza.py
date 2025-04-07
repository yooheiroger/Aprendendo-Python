print('welcome to Python Pizza Deliveries')
size = input('what size pizza do you want? S, M , L: ')
pepperoni = input ('Do you want pepperoni in your pizza ? Y or N: ')
extra_cheese = input('Do you want extra cheese ? Y or N: ')

total = 0
if size == 'S':
    total = 15
elif size == 'M':
    total = 20
else:
    total = 25

if pepperoni == 'Y':
    if size == 'S':
        total += 2

    else:
        total +=3
        print(total)
else:
    print('no pepperoni added')

if extra_cheese == 'Y':
    total += 1


print(f'The price of your pizza is: {total}')