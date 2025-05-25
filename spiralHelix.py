import random
import turtle

my_board = turtle.Screen()
my_board.bgcolor("light blue")
my_board.title("helix")

my_turtle = turtle.Turtle()
#my_turtle.speed(0)
color_list = ["red","blue","green","purple","pink","yellow","black","white"]
for i in range(20):
    my_turtle.color(color_list[random.randint(0, len(color_list) - 1)])
    my_turtle.circle(5 * i)
    my_turtle.color(color_list[random.randint(0, len(color_list)-1)])
    my_turtle.circle(-5 * i)
    my_turtle.left(i)
turtle.done()