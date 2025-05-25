import turtle

my_screen = turtle.Screen()
my_screen.title("Python Turtle")
my_screen.bgcolor("light blue")

my_instance = turtle.Turtle()
#shrinking square
length = 200
for num in range(12):
    for number in range(4):
        my_instance.forward(length)
        my_instance.right(90)
        length = length - 4
#circle
'''
r = 100
my_instance.circle(r)
'''
turtle.done()