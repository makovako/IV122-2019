from math import sqrt
from PIL import Image
from numpy import arange

colors = [(255,0,0),(0,0,255),(0,255,0)]

# distance of two complex numbers
def distance(x,y):
    return sqrt((x.real - y.real)**2 + (x.imag - y.imag)**2)

def newton(x,y):
    z = complex(x,y)
    for _ in range(20):
        zn = z - (z**3 - 1)/(3 * z**2)
        z = zn
    return z

# size = size of the picture
# zoom = width of the fractal from zero to the edge, real number greater than zero
def newton_fractal(size, zoom = 2):
    roots = [complex(1,0),complex(-0.5,sqrt(3)/2),complex(-0.5,-sqrt(3)/2)]
    im = Image.new("RGB",(size,size),(255,255,255))
    for i in range(size):
        for j in range(size):
            x = i * (zoom/(size-1)) - (zoom/2) #normalisation to -zoom/2 - +zoom/2
            y = j * (zoom/(size-1)) - (zoom/2)
            z = newton(x,y)
            dist = []
            for root in roots:
                dist.append(distance(z,root))
            index = dist.index(min(dist))
            im.putpixel((i,j),colors[index])
    # im.save("images/newton-{}.png".format(int(zoom*100))) # just for generating animationn
    im.save("newton.png")

# for i in arange(0.01,5,0.01): # just for generating animation
    # newton_fractal(300,i)
# for i in arange(0.1,20,0.1):
    # newton_fractal(300,i)
newton_fractal(300,2)