from turtle import Turtle

# move a little bit for next drawing
def move(t, n):
    t.penup()
    t.angle = 90
    t.forward(n*10)
    t.angle = 0
    t.pendown()

t = Turtle()

for i in {3,4,5,6,7,8,9,12}:
    for _ in range(i):
        t.forward(30)
        t.right(360/i)
    move(t,2*i)

t.save_to_file("polygons.svg",50,150)

p = Turtle()

for i in {7,9,10,11,13,14,15,16,17,18,19,20,21}:
    for _ in range(2*i): # 2*i just so i have enough iterations
        p.forward(100)
        p.right(180 - 720/i)
    move(p,20)
    # Reset of position so more pictures fit
    if i == 15:
        p.y = 150
        p.x = 0

p.save_to_file("stars.svg",150,150)