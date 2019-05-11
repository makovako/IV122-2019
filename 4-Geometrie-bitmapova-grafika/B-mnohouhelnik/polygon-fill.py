from PIL import Image
from math import sqrt

WHITE = (255,255,255)
BLACK = (0,0,0)


# soft - not used anymore
def is_on_line(point, line, soft = False):
    # p.y - a.y / b.y - a.y = p.x - a.x / b.x - a.x
    # (p.y - a.y) * (b.x - a.x) - ((p.x - a.x)*(b.y - a.y)) = 0
    
    a,b = line
    if not (((a[0] <= point[0] <= b[0] and a[0] < b[0]) or (a[0] >= point[0] >= b[0] and a[0] > b[0])) \
        or ((a[1] <= point[1] <= b[1] and a[1] < b[1]) or (a[1] >= point[1] >= b[1] and a[1] > b[1]))):
        return False
    elif soft:
        return True
    test = ((point[1] - a[1]) * (b[0] - a[0])) - ((b[1] - a[1]) * (point[0] - a[0])) == 0
    return test

# not used anymore
def test_parallel(line1, line2):
    a,b = line1
    vector1 = (b[0] - a[0],b[1] - a[1])
    a,b = line2
    vector2 = (b[0] - a[0],b[1] - a[1])
    n = (vector1[0]*vector2[0] + vector1[1]*vector2[1])
    d = (sqrt(vector1[0]**2 + vector1[1]**2)*sqrt(vector2[0]**2 + vector2[1]**2))
    if d == 0:
        return False
    return n/d == 1

# not used anymore
def have_intersection(line1, line2):
    a,b = line1
    c,d = line2
    x1,y1 = a
    x2,y2 = b
    x3,y3 = c
    x4,y4 = d
    if ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)) == 0:
        return False
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    return is_on_line((x,y),line1,True) and is_on_line((x,y),line2,True)



def create_lines(points):
    points.append(points[0])
    lines = []
    for i in range(len(points)-1):
        lines.append((points[i],points[i+1]))
    return lines

# doesn't work, some first experiments
def polygon_fill_bad(points, size):
    lines = create_lines(points)
    im = Image.new("RGB",(size,size),WHITE)
    for x in range(size):
        help_line = ((x,0),(x,size))
        intersect = 0
        correction = 0
        for line in lines:
            if have_intersection(help_line, line):
                intersect += 1
        if intersect % 2 == 1:
            correction = 1
        for y in range(size):
            intersect = [0,0] # left right
            for line in lines:
                if is_on_line((x,y),line):
                    im.putpixel((x,y),BLACK)
                    break
                help_line = ((x,y),(x,size)) # crete line from point (x,y) to the end of image and test number of intersections
                if test_parallel(help_line,line):
                    continue
                if have_intersection(help_line,line):
                    intersect[1] += 1
                help_line = ((x,0),(x,y))
                if have_intersection(help_line,line):
                    intersect[0] += 1
            intersect[0] += correction
            if intersect[0] % 2 == 1 and intersect[1] % 2 == 1:
                print("HERE")
                im.putpixel((x,y),BLACK)
    im.show()

# this looks like it works, finally
def polygon_fill(filename,points,size):
    lines = create_lines(points)
    im = Image.new("RGB",(size,size),WHITE)
    for x in range(size):
        for y in range(size):
            intersect = 0
            for line in lines:
                a,b = line
                vector = (b[0] - a[0], b[1] - a[1])
                if vector[1] == 0: # horizontal line
                    if is_on_line((x,y),line):
                        im.putpixel((x,y),BLACK)
                        break
                    continue
                s = a[0] + vector[0]*((y-a[1])/vector[1]) # explanation in readme # TODO make readme
                if x < s and ((y < a[1]) != (y < a[1] + vector[1])):
                    intersect += 1
            if intersect % 2 == 1:
                im.putpixel((x, y),BLACK)
    im.transpose(Image.FLIP_TOP_BOTTOM).save(filename)

                
    

points1 = [(10,10),(180,20),(160,150),(100,50),(20,80)]
points2 = [(10,10),(10,190),(190,190),(190,10)]
points3 = [(10,105),(55,15),(105,195),(155,10),(195,100),(150,190),(100,20),(50,180)]

polygon_fill("polygon1.png",points1,200)
polygon_fill("square.png",points2,200)
polygon_fill("polygon2.png",points3,200)