from turtle import Turtle

def sierpinski(turtle, depth, length):
    if depth > 0:
        for _ in range(3):
            sierpinski(turtle,depth-1,length/2)
            turtle.forward(length)
            turtle.left(120)
        
def draw_sierpinski(size):
    for i in {2,3,4,5,6,7}:
        t = Turtle()
        t.angle=-30
        sierpinski(t,i,size)
        t.save_to_file("sierpinski_{}.svg".format(i),size,size,(size,size))

def bush(turtle, depth, length):
    turtle.forward(length)
    if depth > 0:
        turtle.left(45)
        bush(turtle, depth-1, length/2)
        turtle.right(90)
        bush(turtle, depth-1, length/2)
        turtle.left(45)
    turtle.penup()
    turtle.backward(length)
    turtle.pendown()

def draw_bush(size):
    for i in {2,3,4,5,6,7}:
        t = Turtle()
        bush(t,i,size)
        t.save_to_file("bush_{}.svg".format(i),2*size,2*size)

draw_sierpinski(200)
draw_bush(200)