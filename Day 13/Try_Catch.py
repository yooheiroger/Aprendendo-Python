import numbers

try:
    age = int (input('how old are you? '))
except ValueError:
    print('You type a invalid number. Try a numerical such as 20')
    age = int(input('how old are you? '))


