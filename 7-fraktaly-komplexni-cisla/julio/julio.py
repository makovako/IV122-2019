from math import sqrt
from PIL import Image
from numpy import arange

def distance(x,y):
    return sqrt((x.real - y.real)**2 + (x.imag - y.imag)**2)

def julio(z,c,iter = 30):
    average_distance = 0
    for i in range(iter):
        z = z**2 +c
        if abs(z.real) > 2 or abs(z.imag) > 2:
            return (3,i)
        average_distance += distance(z,complex(0,0))
    return (z,average_distance/iter)

def julio_set(filename, size = (400,400),c = complex(-0.13,0.75), zoom = ((-2,2),(-2,2))):
    iterations = abs(int(120 / (zoom[0][1] - zoom[0][0]))) # compute number of iterations, whole set = 30 iterations
    im = Image.new("RGB",size,(255,255,255))
    for i in range(size[0]):
        for j in range(size[1]):
            x = (i/size[0]) * (zoom[0][1] - zoom[0][0]) + zoom[0][0] # change range of computing
            y = (j/size[1]) * (zoom[1][1] - zoom[1][0]) + zoom[1][0]
            z, average_distance = julio(complex(x,y),c,iterations)

            if z.real <= 2 and z.imag <= 2:
                color = int(average_distance*255/3)
                im.putpixel((i,j),(color,color,color))
            else:
                color = int(average_distance*255/iterations)
                im.putpixel((i,j),(color,color,color))
    im.transpose(Image.FLIP_TOP_BOTTOM).save(filename)

julio_set("julio.png")
julio_set("julio_zoom_1.png",zoom=((-1,1),(-1,1)))
julio_set("julio_zoom_2.png",zoom=((-1,1),(0,2)))
julio_set("julio_other_c.png",c=complex(-0.13,0.80))

# Some loops for animations

# for i in arange(-2,2,0.05):
#     i = round(i,2)
#     julio_set("images/julio{}.png".format(int((i*100+200)/5)),c=complex(-0.13,i))  

# for i in arange(-2,2,0.05):
#     i = round(i,2)
#     julio_set("images/julio{}.png".format(int((i*100+200)/5)),c=complex(-0.20,i))
  
# for i in arange(0.3,1.3,0.01):
#     i = round(i,2)
#     julio_set("images/julio{}.png".format(int((i*100+200))),c=complex(-0.20,i))
