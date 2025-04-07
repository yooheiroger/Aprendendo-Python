def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b== 0:
        print('Can''t divide by 0')
    else:
        return a/b

def switch_case(option_,a1,b1):
    match option_:
        case 1:
                return add(a1,b1)
        case 2:
                return subtract(a1, b1)
        case 3:
                return multiply(a1, b1)
        case 4:
                return divide(a1, b1)
        case _:
            return print('Wrong input')

close = True
while close:
    a = float(input('What''s  the first number: \n'))
    b = float(input('What''s  the second number: \n'))
    option = int(input(''' insert the operation
    Type 1 for "+"
    Type 2 for "-"
    Type 3 for "*"
    Type 4 for "/"
    '''))
    result = switch_case(option,a,b)
    print(f'Your result is: {result}')
    yes_or_no = input('Do you want to try again with new numbers or continue with the preview result? "yes" for continue the application or "no" for close it ').lower()
    if yes_or_no == 'no':
        print('closing the app...')
        close = False
    else:
        while close:
            print('Type again')
            new_number = float(input('type a new number: '))
            option = int(input(''' insert the operation
                Type 1 for "+"
                Type 2 for "-"
                Type 3 for "*"
                Type 4 for "/"
                '''))
            result = switch_case(option,result,new_number)
            print(f'Your result is: {result}')
            yes_or_no = input(
                'Do you want to try again with new numbers or continue with the preview result? "yes" for continue the application or "no" for close it ').lower()
            if yes_or_no == 'no':
                print('closing the app...')
                close = False


