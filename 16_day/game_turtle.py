# #Turtle docstrings: https://docs.python.org/3/library/turtle.html
# # Python packages: pypi.org
# # Pretty table helps you get a tabular form

# from turtle import Turtle, Screen

# obj = Turtle()
# obj.shape("turtle")
# obj.color("coral")
# obj.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("City name", ["Lagos", "Abuja", "Ilorin"])
table.add_column("City populatione", [800, 500, 420])
table.align = "l"
# table.border = False
# table.header = False
print(table)