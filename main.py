from prettytable import PrettyTable
from turtle import Turtle, Screen

sven = Turtle()
my_screen = Screen()
sven.shape("turtle")
sven.color("black", "red")
sven.forward(100)

print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.align = "l"
table.field_names = ["Player Name", "Season 1994", "Season 1995", "Season 1996"]
table.add_row(["Gravy", 123, 129, 160])
table.add_row(["Tiny", 586, 194, 114])
table.add_row(["XXX", 112, 100, 171])
table.add_row(["Deuce", 137, 256, 161])
table.add_row(["Rico", 208, 434, 121])
table.add_row(["Morgan", 156, 292, 164])
table.add_row(["Juan", 156, 159, 186])
print(table)
