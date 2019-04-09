from PIL import Image
from math import sin,cos,radians,sqrt

WHITE = (255,255,255)
BLACK = (0,0,0)

def circle(size = 200, r = 80):
    im = Image.new("RGB",(size,size),WHITE)
    for x in range(size):
        for y in range(size):
            if (x - size/2)**2 + (y - size/2)**2 < r**2:
                im.putpixel((x,y),BLACK)
    im.save("circle.png")

def circle_depth(depth = 5, size = 200, r = 80):
    depth /= 100
    im = Image.new("RGB",(size,size),WHITE)
    for x in range(size):
        for y in range(size):
            if abs((x - size/2)**2 + (y - size/2)**2 - r**2)/r**2 < depth:
                im.putpixel((x,y),BLACK)
    im.save("circle_depth.png")

def circle_par(size = 200, r = 80):
    im = Image.new("RGB",(size,size),WHITE)
    for t in range(0,360):
        x = int(round(size/2 + r*cos(radians(t))))
        y = int(round(size/2 + r*sin(radians(t))))
        im.putpixel((x,y),BLACK)
    im.save("circle_par.png")

def spiral(size = 200):
    im = Image.new("RGB",(size,size),WHITE)
    for t in range(0,size*10):
        x = int(round(size/2 + (10*t/size)*cos(radians(t%360))))
        y = int(round(size/2 + (10*t/size)*sin(radians(t%360))))
        for i,j in {0,0,1,1,},{0,1,1,0}: # put black pixel on x,y and 3 other, right, down, right+down
            im.putpixel((x+i,y+j),BLACK)
    im.save("spiral.png")

def spiral_color(size = 200):
    im = Image.new("RGB",(size,size),WHITE)
    for t in range(0,size*10):
        x = int(round(size/2 + (10*t/size)*cos(radians(t%360))))
        y = int(round(size/2 + (10*t/size)*sin(radians(t%360))))
        R = int(abs(y*4-size*2)/200 * 255)
        G = x*-127/200 + 127
        B = x*255/200
        for i,j in {0,0,1,1,},{0,1,1,0}: # put black pixel on x,y and 3 other, right, down, right+down
            im.putpixel((x+i,y+j),(int(R),int(G),int(B)))
    im.save("spiral_color.png")

def triangle(size = 200):
    im = Image.new("RGB",(size,size),WHITE)
    sq = sqrt(size**2 - (size/2)**2)
    for x in range(size):
        for y in range(size):
            if y<size and y > (sqrt(3)*x + size - size*sqrt(3)) and y > (-sqrt(3)*x + size):
                R = (255/size) * (x)
                G = -(255/size) * (x-200)
                B = (255/size)*(y)
                im.putpixel((x,y),(int(R),int(G),int(B)))
    im.save("triangle.png")

    

circle()
circle_depth()
circle_par()
spiral()
spiral_color()
triangle()
