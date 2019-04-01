# Vector Graphics

from vector_graphic import vector_graphic

# lines - list of lines
# x,y - coordinates of point to rotate around
def rotate_90(lines,x,y):
    new_lines = []
    for line in lines:
        v1,v2 = line
        new_lines.append(((-v1[1] + x + y,v1[0] - x + y),(-v2[1] + x + y,v2[0] - x + y)))
    return new_lines

def rotate_180(lines,x,y):
    new_lines = []
    for line in lines:
        v1,v2 = line
        new_lines.append(((-v1[0] + 2*x,-v1[1] + 2*y),(-v2[0] + 2*x,-v2[1] + 2*y)))
    return new_lines

def rotate_270(lines,x,y):
    new_lines = []
    for line in lines:
        v1,v2 = line
        new_lines.append(((v1[1] - y + x,-v1[0] + x + y),(v2[1] - y + x,-v2[0] + x + y)))
    return new_lines
# Prints parts of the star in different quadrants
#        ^
#   1    |    0
#        |
#<-------S-------->
#        |
#   2    |    3
#        V
# S - Middle of the coordinate system, number - number of quadrant
# x0, y0 - coordinates of S
# q - number of quadrant (originally i wanted to rotate q times 90 degrees)
# r - radius, width of star from S to Edge
# part - number of lines in quadrant
# stroke - color of line, stroke_width - thickness of line
#
# This function print lines in given quadrant.
# r/part gives distance between start and end points of lines
def part_star(vg, x0, y0, q, r = 500, part = 5, stroke = "black", stroke_width = 1):
    dist = r / part
    lines = []
    x_a = x0 + r
    y_a = y0
    x_b = x0
    y_b = y0
    # Creates lines for first quadrant
    for _ in range(part):
        lines.append(((x_a,y_a),(x_b,y_b)))
        x_a -= dist
        y_b += dist
    # if q == 0, don't rotate
    # Rotate if necessary
    if q == 1:
        lines = rotate_90(lines,x0,y0)
    elif q == 2:
        lines = rotate_180(lines,x0,y0)
    elif q == 3:
        lines = rotate_270(lines,x0,y0)
    for line in lines:
        vg.line(line[0][0],line[0][1],line[1][0],line[1][1],stroke,stroke_width)

# Creates star with the middle in x,y
# name - filename
# part - number of lines in each quadrant
# stroke - color of lines, stroke_width - thickness of lines
def make_star(name,x,y,r,part = 5, stroke = "black", stroke_width = 1):
    vg = vector_graphic(name,2*x,2*y)
    vg.start()
    for i in range(4):
        part_star(vg,x,y,i,r,part,stroke,stroke_width)
    vg.stop()

# Creates frame with the middle in x,y
# name - filename
# part - number of lines in each quadrant
# stroke - color of lines, stroke_width - thickness of lines
def make_frame(name,x,y,r,part = 5, stroke = "black", stroke_width = 1):
    vg = vector_graphic(name,2*x,2*y)
    vg.start()
    part_star(vg,x-r,y-r,0,2*r,part,stroke,stroke_width)
    part_star(vg,x+r,y-r,1,2*r,part,stroke,stroke_width)
    part_star(vg,x+r,y+r,2,2*r,part,stroke,stroke_width)
    part_star(vg,x-r,y+r,3,2*r,part,stroke,stroke_width)
    vg.stop()

make_star("star1.svg",100,100,100)
make_star("star2.svg",100,100,100,10,"green",2)
make_star("star3.svg",200,200,150,50)

make_frame("frame1.svg",100,100,100,10)
make_frame("frame2.svg",200,200,200,50,"red")
