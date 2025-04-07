# from turtle import Turtle, Screen
#
# my_turtle = Turtle()
# my_screen = Screen()
# print(my_screen.canvheight)
# my_turtle.shape('turtle')
# my_turtle.color('red')
# my_turtle.forward(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column('Pokemon Name',['pokachu','charmander'])
table.add_column('Pokemon Type',['eletric','fire'])
table.align ='r'
print(table)











