from vector_graphic import vector_graphic
from math import pi,cos,sin
import random

# number - number of lines
# lenght - length of line
# image_size - size of the final image, so no line is out of image
def generate_random_lines(number, length = 20, image_size = 200):
    lines = []
    for _ in range(number):
        x1 = random.randint(0,image_size)
        y1 = random.randint(0,image_size)
        while True:
            angle = random.random()*2*pi
            x2 = x1 + length*cos(angle)
            y2 = y1 + length*sin(angle)
            if 0 <= x2 < image_size and 0 <= y2 < image_size:
                break
        lines.append(((x1,y1),(x2,y2)))
    return lines

# v - vector_graphics to write on
# lines - list of lines to draw
def draw_lines(v, lines):
    for line in lines:
        a,b = line
        x1,y1 = a
        x2,y2 = b
        v.line(x1,y1,x2,y2)

# draws intersections as circles
# v - vector graphics to write on
# intersections - list of points
# r - radius of one drawen point
def draw_intersections(v, intersections, r):
    for x,y in intersections:
        v.circle(x,y,r,"black",1,"black")

# test if point (computed intersection) is on line
def is_on_line(point,line):
    x,y = point
    a,b = line
    return ((a[0] < x < b[0]) or (a[0] > x > b[0]))\
        and ((a[1] < y < b[1]) or (a[1] > y > b[1]))

# compute intersection of two lines based on formula
def get_intersection(line1,line2):
    a,b = line1
    x1,y1 = a
    x2,y2 = b
    c,d = line2
    x3,y3 = c
    x4,y4 = d
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) *(x3 * y4 - y3 * x4))\
         / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4))\
        / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    if is_on_line((x,y),line1) and is_on_line((x,y),line2):
        return (x,y)
    return None

# compute intersections for lines
def compute_intersections(lines):
    intersections = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            intersection = get_intersection(lines[i],lines[j])
            if intersection is not None:
                intersections.append(intersection)
    return intersections

# main function for generating, computing and drawing lines and intersections
# filename - filename
# image_size - size of image
# generation_method - function which will generate lines
# *args - orguments for generation_method function
def intersections(filename, image_size, generation_method, *args):
    lines = generation_method(*args)
    intersections = compute_intersections(lines)
    v = vector_graphic(filename, image_size, image_size)
    v.start()
    draw_lines(v, lines)
    draw_intersections(v, intersections, 2)
    v.stop()


intersections("intersections.svg", 200, generate_random_lines, 50, 40, 200)
intersections("intersections2.svg", 200, generate_random_lines, 50, 20, 200)

