from PIL import Image

size = 200

im = Image.new("RGB", (size, size))
for x in range(size):
    for y in range(size):
        im.putpixel((x,y,),(int((round(x*255 / size))), 0, int(round(y*255 / size))))

im.save("test.png")