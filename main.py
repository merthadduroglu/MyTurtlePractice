import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()
turtle_instance_2 = turtle.Turtle()
#square
'''
turtle_instance.color("black")
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
'''
#for x in range(4):
    #turtle_instance.forward(100)
    #turtle_instance.right(90)
'''
#star
turtle_instance_2.left(75)
turtle_instance_2.forward(100)
turtle_instance_2.right(150)
turtle_instance_2.forward(100)
turtle_instance_2.right(150)
turtle_instance_2.forward(100)
turtle_instance_2.right(135)
turtle_instance_2.forward(90)
turtle_instance_2.right(135)
turtle_instance_2.forward(100)
'''
#star
#for y in range(5):
    #turtle_instance_2.right(144)
    #turtle_instance_2.forward(100)
#polygon
num_sides = 10
angles = 360.0 / num_sides
side_length = 80
for z in range(num_sides):
    turtle_instance.forward(side_length)
    turtle_instance.right(angles)
turtle.done()