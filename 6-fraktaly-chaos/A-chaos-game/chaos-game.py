from PIL import Image
from math import sin, cos, pi, radians
import random

colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(0,0,0)]

# Regerates points of regular polygons
# size = size of picture
# n = number of points
# w = if the points should be weighted
def generate_points(size, n, w = False):
    points = []
    angle = radians(270)
    for i in range(n):
        x = size/2 + (size/2-1) * cos(angle)
        y = size/2 + (size/2-1) * sin(angle)
        angle += 2*pi / n
        if w: # if weighted
            points.extend(((int(x),int(y)) for _ in range((i+1)*10))) # put point 10 times the iteration
        else:
            points.append((int(x),int(y)))
    return points

# n = number of points in polygon
# r = ratio to move to other point
# size = size of picture
# c = coloring
# w = weighted points
# it = number of iterations
def draw(filename, n, r, size, c = False, w = False, it = 100000):
    r=1-r
    points = generate_points(size,n,w)
    im = Image.new("RGB",(size,size),(255,255,255))
    x,y = points[0][0],points[0][1] # choose first point
    for _ in range(it):
        point = random.choice(points) # choose random point
        x,y = x + (point[0] - x) * r, y + (point[1] - y) * r
        color = (0,0,0)
        if c:
            color = colors[points.index(point) % n] # choose index for color based on index of point in points list
        im.putpixel((int(x),int(y)),color)
    im.save(filename)

draw("sierpinsky_triangle.png",3,1/2,300)
draw("pentagon_third.png",5,1/3,300)
draw("pentagon_three_eights.png",5,3/8,300)
draw("hexagon_third.png",6,1/3,300)
draw("septagon_third.png",7,1/3,300)

# Weighted, more dots on weighted points
draw("weighted_sierpinsky_triangle.png",3,1/2,300,False,True)
draw("weighted_pentagon_third.png",5,1/3,300,False,True)

# Colors
draw("color_septagon_third.png",7,1/3,300,True)
draw("color_sierpinsky_triangle.png",3,1/2,300,True)
draw("color_pentagon_third.png",5,1/3,300,True)
draw("color_pentagon_three_eights.png",5,3/8,300,True)
draw("color_hexagon_third.png",6,1/3,300,True)
draw("color_hexagon_half.png",6,1/2,300,True)

# Mix
draw("mix_septagon.png",7,1/3,300,True,True)
