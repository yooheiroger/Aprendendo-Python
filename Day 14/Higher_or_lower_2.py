from art import logo, vs
from List_of_famous import data
import random

def chose_celebrity(list):
    a = list.random.choice(list)
    return a

def print_celebrity_propertie(celebrity1):
    print(  ' Name:        ',celebrity1['name'],'\n',
            'Description: ',celebrity1['description'],'\n',
            'Country:     ',celebrity1['country'])
    return celebrity1['follower_count']






print (logo)
c1 = chose_celebrity(data)
c2 = chose_celebrity(data)
if c1 == c2:
    c2 = chose_celebrity(data)

