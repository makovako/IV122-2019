from turtle import Turtle
from vector_graphic import vector_graphic
from math import sin,cos,radians,pi,sqrt

# pentagon absolut
# source of points http://mathworld.wolfram.com/RegularPentagon.html

def pentagon_absolut():
    points = []
    zoom = 100
    move = 100
    c1 = cos(2*pi/5)
    c2 = cos(pi/5)
    s1 = sin(2*pi/5)
    s2 = sin(4*pi/5)

    points.append((0*zoom+move,1*zoom+move))
    points.append((-s1*zoom+move,c1*zoom+move))
    points.append((-s2*zoom+move,-c2*zoom+move))
    points.append((s2*zoom+move,-c2*zoom+move))
    points.append((s1*zoom+move,c1*zoom+move))

    vg = vector_graphic("pentagon_absolut.svg")
    vg.start()
    for i in range(5):
        for j in range(i+1,5):
            vg.line(points[i][0],points[i][1],points[j][0],points[j][1])
    vg.stop()

# pentagon relative

def pentagon_relative():
    pentagon_angle = 72 # 180 - angle of pentagon (108)
    star_angle = 144 # 180 - angle of star (36) 
    pentagon_length = 50
    star_length = int(2*pentagon_length*cos(radians(36))) # trigonometry
    t = Turtle()
    for _ in range(5):
        t.forward(pentagon_length)
        t.left(pentagon_angle)
    t.left(36)
    for _ in range(5):
        t.forward(star_length)
        t.left(star_angle)
    t.save_to_file("pentagon_relative.svg")

# recursive square - absolute

def recursive_square(size = 100):
    points = [(0,0),(size,0),(size,size),(0,size)]
    vg = vector_graphic("recursive_square.svg")
    vg.start()
    for _ in range(20):
        new_points = []
        for i in range(4):
            vg.line(points[i][0],points[i][1],points[(i+1)%4][0],points[(i+1)%4][1])
            # i want to get to quarter, i will go 2x to the middle
            middle = ((points[i][0] + points[(i+1)%4][0])/2,(points[i][1] + points[(i+1)%4][1])/2)
            new_points.append(((points[i][0] + middle[0])/2,(points[i][1] + middle[1])/2))
        points = []
        points = new_points[:]
    vg.stop()

# circle grid - absolut

def circle_grid(step = 10, r = 50, offset = 50):
    # radius 50, middle 0 0, i will step from -r to r by step, so from -50 to 50 by 10, thats x coordinate
    # i calculate y coordinates of both itersections of circle and vertical line
    # and i use it also as x coordinate for horizontal line at the same time
    vg = vector_graphic("circle_grid.svg",2*r,2*r)
    vg.start()
    for x in range(0-r,0+r+1,step): # 0+r is right boundry of circle, because of range function i need to go further so +1
        y1 = sqrt(r**2 - x**2)
        y2 = -sqrt(r**2 - x**2)
        vg.line(x+offset,y1+offset,x+offset,y2+offset)
        vg.line(y1+offset,x+offset,y2+offset,x+offset)
    vg.stop()

# triangle in triangle - relative
def triangle_in_triangle(step = 10):
    t = Turtle()
    # toto uz neviem propisat v anglictine
    # vyska = taznica
    # i = vzdialenost od taziska [0,0] k vrchnemu bodu = 2/3 vysky
    # o step posuvam vrchny bod hore
    for i in range(step, 10*step +1, step): # prvy trojuholni, posledny tojuholnik +1, posun
        height = i * 3/2
        side = sqrt(4*(height**2)/3)
        t.right(150) # som otoceny hore, cize 90 + 60 stupnov
        for _ in range(3):
            t.forward(side)
            t.right(120)
        t.angle = 0
        t.penup()
        t.forward(step)
        t.pendown()
    t.save_to_file("triangle.svg",10*step,10*step)

# flower - relative

def flower():
    t = Turtle()
    n = 30
    for _ in range(n):
        for _ in range(n):
            t.forward(360/n)
            t.right(360/n)
        t.right(360/n)
    t.save_to_file("flower.svg")


pentagon_absolut()
pentagon_relative()
recursive_square()
circle_grid()
triangle_in_triangle()
flower()