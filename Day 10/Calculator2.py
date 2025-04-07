import os
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

def operations_(select, n1, n2):
    if select in operations:
        total = operations[select](n1, n2)
        return total

#################################################
operations ={
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
def calculator():
    close = True
    n1 = float(input('What is the first number: '))
    while close:
        for symbol in operations:
            print(symbol)
        select = input('Select one operetion: ')
        while select not in operations:# check the operation if select is inside the  operation
            print('Invalid Operation')
            for symbol in operations:# just in case the user type something wrong
                print(symbol)
            select = input('Select one operetion: ')

        n2 = float(input('What is the second number: '))
        result = operations_(select,n1,n2)# funcao
        print(f' {n1} {select} {n2} = ', result)
        yes_or_no = input('"Yes" for continue or "No" restart the app: ').lower()

        if yes_or_no == 'yes':
            print('type again')
            n1 = result
        elif yes_or_no == 'no':
            print('Reseting the program...\n')
            print('...')
            os.system('cls')
            calculator()# recusao chamar a propria função para fazer um while
        else:
            while yes_or_no != 'yes' or yes_or_no != 'no':
                print('Wrong input try again')
                yes_or_no = input('"Yes" for continue or "No" restart the app: ').lower()


calculator()