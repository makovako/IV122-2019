from PIL import Image
from math import sqrt

# number of dividers, not counting itself
def dividers(n):
    div = 0
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            div += 1
    return div

# Functions for different conditions
def condition_is_prime(x, *args):
    return not dividers(x) == 1

def condition_divisible(n,x):
    return not n % x == 0

# name = name of the file
# size = size of canvas
# condition = when the pixel should be drawn
# args = args to the condition function
def ulam(name, size = 200, condition = condition_is_prime, *args):
    im = Image.new("RGB", (size, size))
    x = int(size/2)
    y = int(size/2)

    # Change of coordinates based on direction delta[0..3]
    delta = [(0,-1),(-1,0),(0,1),(1,0)]
    direction = 3
    last_count = count = 1
    # number we are working on
    number = 1
    while x in range(size) and y in range(size):
        if (condition(number, *args)):
            im.putpixel((x,y),(255, 255, 255))
        number += 1
        count -= 1
        x += delta[direction][0]
        y += delta[direction][1]

        if count == 0:
            # every second change we need to move one more pixel
            if direction % 2 == 0:
                last_count += 1
            direction = (direction + 1) % 4
            count = last_count
    
    im.save("{}.png".format(name))

# ulam based on prime condition
ulam("normal_ulam")

# number divisible by i, numbers chosen based on prettyness of the output
for i in [3,5,7,9,10,11,13,17,18]:
    ulam("dividers_by_{}".format(i), 200, condition_divisible, i)

