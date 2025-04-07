

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def show_how_much_cost_coffee(menu):
    '''show the cost of each coffee '''
    print(f'''
    The Menu of coffees available: 
    {'Espresso':<12} R${menu['espresso']['cost']}
    {'Latte':<12} R${menu['latte']['cost']}
    {'Cappucciono':<12} R${menu['cappuccino']['cost']}    
    ''')
def choosing_coffee(option):
    '''take the option of user and store the string'''
    if option == 'espresso':
        print('To make up wake up')
    elif option == 'latte':
        print('Latte, tasty good with some milk')
    elif option == 'cappuccino':
        print('Cappuciono...')
    elif option == 'resource':
        show_resources(resources)
    elif option == 'off':
        print('Turn off the machine')
    else:
        print('Something goes wrong. Type again')

def show_resources(resources):
    '''show the resource of the coffee machine'''
    print(resources)

def low_resources(coffee):
    if coffee == 'espresso' or coffee == 'latte' or coffee== 'cappuccino':
        for ingredients,amount in MENU[coffee]['ingredients'].items():# Search in menu the drink and get the key and value of MENU[coffee]['ingredients']
            if  resources.get(ingredients,0)<amount:
                resources[ingredients] -= amount
                print('Sorry, no resources...')
                return False

        return True
# MENU[drink]: Acessa os dados do café selecionado (drink) dentro do dicionário MENU.
# MENU[drink]["ingredients"]: Obtém o dicionário que contém os ingredientes necessários para preparar essa bebida.
# .items(): Retorna os pares chave: valor do dicionário de ingredientes, ou seja, (ingredient, amount).
# for ingredient, amount in ...: Itera sobre esses pares, onde:
#     ingredient representa o nome do ingrediente (ex.: "water", "milk", "coffee").
#     amount representa a quantidade necessária para preparar a bebida. está acessando dentro do MENU o valor de cada item do cafe e comparando se existe o suficiente para fazer

def pay_coffe(menu, money, option_coffee):
    '''calculate the change of each coffee choose'''
    if option_coffee == 'espresso':
        value = menu['espresso']['cost']
    elif option_coffee == 'latte':
        value = menu['latte']['cost']
    else:
        value = menu['cappuccino']['cost']
    money_change = money - value
    return money_change

def amount_resource(remain_resource, option,menu):
    '''Decrease the amount of resource every time that something was chose'''
    if option == 'espresso':
        remain_resource['water'] =remain_resource['water'] -  menu['espresso']['ingredients']['water']
        remain_resource['coffee'] =remain_resource['coffee'] - menu['espresso']['ingredients']['coffee']
    elif option == 'latte':
        remain_resource['water'] =remain_resource['water'] - menu['latte']['ingredients']['water']
        remain_resource['coffee'] =remain_resource['coffee'] - menu['latte']['ingredients']['coffee']
        remain_resource['milk'] =remain_resource['milk'] -  menu['latte']['ingredients']['milk']
    else:
        remain_resource['water'] =remain_resource['water'] - menu['latte']['ingredients']['water']
        remain_resource['coffee'] =remain_resource['coffee'] - menu['latte']['ingredients']['coffee']
        remain_resource['milk'] =remain_resource['milk'] - menu['latte']['ingredients']['milk']
    return remain_resource


#START
# TODO 1. Print all resources in the machine and show the options for the costumer
machine_is_on = True

while machine_is_on:
    show_how_much_cost_coffee(MENU)
    option = input('What would you like? (espresso/latte/cappuccino): ').lower()
    choosing_coffee(option)
    no_resources = low_resources(option)
    if option == 'off':
        break
    if option == 'resource':
        while option:
            show_how_much_cost_coffee(MENU)
            option = input('What would you like? (espresso/latte/cappuccino): ').lower()
            choosing_coffee(option)
    if not no_resources:
        break

# TODO 2. Turn off the machine typing 'off'


# TODO 3. Calculate the money that was insert and give the costumer the change
    inserted_money = True
    while inserted_money:
        money = float(input('Please insert the money'))
        change = pay_coffe(MENU,money,option)
        if change >=0:
            inserted_money = False
        print(f'Your change is: {change}')

# TODO 4. Calculate the amount of resource left
    resource = amount_resource(resources,option,MENU)








