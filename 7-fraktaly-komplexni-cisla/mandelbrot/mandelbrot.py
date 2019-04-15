from math import sqrt
from PIL import Image

def distance(x,y):
    return sqrt((x.real - y.real)**2 + (x.imag - y.imag)**2)

def mandelbrot(c,iter=30):
    z = 0
    average_distance = 0
    for i in range(iter):
        z = z**2 + c
        if abs(z.real) > 2 or abs(z.imag) > 2:
            return (3,i) # 3 so that its outside, i - number of iterations to go outside
        average_distance += distance(z,complex(0,0))
    return (z, average_distance/iter)

# size = size of the picture
# zoom = boundries of space to compute mandelbrot set ((left x, right x),(left y, right y))
def mandelbrot_set(filename, size = (600,400),zoom = ((-2,1),(-1,1))):
    iterations = abs(int(90 / (zoom[0][1] - zoom[0][0]))) # compute number of iterations, whole set = 30 iterations
    im = Image.new("RGB",size,(255,255,255))
    for i in range(size[0]):
        for j in range(size[1]):
            x = (i/size[0]) * (zoom[0][1] - zoom[0][0]) + zoom[0][0] # change range of computing
            y = (j/size[1]) * (zoom[1][1] - zoom[1][0]) + zoom[1][0]
            z, average_distance = mandelbrot(complex(x,y),iterations)

            if z.real <= 2 and z.imag <= 2:
                color = int(average_distance*255/3)
                im.putpixel((i,j),(color,color,color))
            else:
                color = int(average_distance*255/iterations)
                im.putpixel((i,j),(color,color,color))
    im.transpose(Image.FLIP_TOP_BOTTOM).save(filename) 

mandelbrot_set("mandelbrot_all.png")
mandelbrot_set("mandelbrot_part.png",(600,400),((-0.5,0.25),(0.5,1)))
