from PIL import Image

def feigenbaum(filename,size = 200, it = 200, zoom = ((2.4,4),(0,1))):
    image_height = int(size * (zoom[1][1] - zoom[1][0]) / (zoom[0][1] - zoom[0][0]))
    im = Image.new("RGB",(size,image_height),(255,255,255))
    for i in range(size):
        r = i*(zoom[0][1] - zoom[0][0])/(size-1) + zoom[0][0]
        x = 0.5
        for j in range(it):
            x = r*x*(1-x)
            if j > it/2:
                lx = x*(zoom[1][1] - zoom[1][0]) + zoom[1][0]
                im.putpixel((i,int((lx - zoom[1][0]) * ((image_height) - 1)/(zoom[1][1] - zoom[1][0]))),(0,0,0))        
    im.transpose(Image.FLIP_TOP_BOTTOM).save(filename)

feigenbaum("feigenbaum.png", 400)
feigenbaum("feigenbaum_zoom.png", 400,zoom = ((3,3.7),(0.3,0.8)))