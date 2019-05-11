from PIL import Image
from math import sin

WHITE = (255,255,255)
BLACK = (0,0,0)

# TODO compact similar functions to less

def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)

def chessboard(filename,size,parts):
    im = Image.new("RGB",(size,size),WHITE)
    d = int(size/parts)
    borders = [d+x*d for x in range(parts)]
    for x in range(size):
        for y in range(size):
            index = [None,None] # index of chess field
            for border in borders:
                if x < border and index[0] == None:
                    index[0] = borders.index(border) % 2
                if y < border and index[1] == None:
                    index[1] = borders.index(border) % 2
            if index[0] == index[1]:
                im.putpixel((x,y),BLACK)
    im.save(filename)

def chessboard_with_cond(filename,size,parts,changes = [25,50,75]):
    im = Image.new("RGB",(size,size),WHITE)
    d = int(size/parts)
    borders = [d+x*d for x in range(parts)]
    if len(changes) % 2 == 1:
        changes.append(size)
    changes = list(zip(changes[0::2], changes[1::2])) # make tuple each two element
    for x in range(size):
        for y in range(size):
            index = [None,None]
            for border in borders:
                if x < border and index[0] == None:
                    index[0] = borders.index(border) % 2
                if y < border and index[1] == None:
                    index[1] = borders.index(border) % 2
            dist = distance((size/2,size/2),(x,y))

            condition = any([i<dist<j for i,j in changes])
            if index[0] == index[1] and condition:
                im.putpixel((x,y),BLACK)
            elif index[0] != index[1] and not condition:
                im.putpixel((x,y),BLACK)
    im.save(filename)

def chessboard_with_sin(filename,size,parts):
    im = Image.new("RGB",(size,size),WHITE)
    d = int(size/parts)
    borders = [d+x*d for x in range(parts)]
    for x in range(size):
        for y in range(size):
            index = [None,None] # index of chess field
            for border in borders:
                if x < border and index[0] == None:
                    index[0] = borders.index(border) % 2
                if y < border and index[1] == None:
                    index[1] = borders.index(border) % 2
            color = int((sin(distance((size/2,size/2),(x,y)))+1)*128)
            if index[0] == index[1]:
                im.putpixel((x,y),(color,color,color))
    im.save(filename)

def chessboard_with_sin_2(filename,size,parts,effect = 1):
    im = Image.new("RGB",(size,size),WHITE)
    d = int(size/parts)
    borders = [d+x*d for x in range(parts)]
    for x in range(size):
        for y in range(size):
            index = [None,None] # index of chess field
            for border in borders:
                if x < border and index[0] == None:
                    index[0] = borders.index(border) % 2
                if y < border and index[1] == None:
                    index[1] = borders.index(border) % 2
            color = int((sin(distance((size/2,size/2),(x,y))*effect)+1)*128)
            if index[0] == index[1]:
                im.putpixel((x,y),(color,color,color))
            else:
                im.putpixel((x,y),(255-color,255-color,255-color))
    im.save(filename)

def only_sin(filename,size,effect = 1):
    im = Image.new("RGB",(size,size),WHITE)
    for x in range(size):
        for y in range(size):
            color = int((sin(distance((x,y),(size/2,size/2))*effect)+1)*128)
            im.putpixel((x,y),(color,color,color))
    im.save(filename)

def only_sin_2(filename,size,effect = 1,border = 50):
    im = Image.new("RGB",(size,size),WHITE)
    
    for x in range(size):
        for y in range(size):
            color = int((sin(distance((x,y),(size/2,size/2))*effect)+1)*128)
            half = size//2
            if y < half-border or y > half+border or x < half-border or x > half+border:
                color = 255 - color
            im.putpixel((x,y),(color,color,color))
    im.save(filename)

def colors(filename,size, effect = 1/10):
    im = Image.new("RGB",(size,size),WHITE)
    for x in range(size):
        for y in range(size):
            R = int((sin(x*effect)+1)*128)
            G = int((sin((x+y)*effect)+1)*128)
            B = int((sin(y*effect)+1)*128)
            im.putpixel((x,y),(R,G,B))
    im.save(filename)
    


chessboard("normal_chessboard.png",240,8)
chessboard_with_cond("chessboard_border.png",240,8)
chessboard_with_cond("chessboard_custom_border.png",240,8,[15,35,75,145,175])
chessboard_with_sin("chessboard_sin.png",240,8)
chessboard_with_sin_2("chessboard_sin_2.png",240,8)
chessboard_with_sin_2("chessboard_sin_3.png",240,8,10)
chessboard_with_sin_2("chessboard_sin_4.png",240,8,50)
chessboard_with_sin_2("chessboard_sin_5.png",240,8,1/2)
chessboard_with_sin_2("chessboard_sin_6.png",240,8,1/5)
chessboard_with_sin_2("chessboard_sin_7.png",240,8,1/10)

only_sin("sin_wave.png",200)
only_sin("sin_wave_2.png",200,2)
only_sin("sin_wave_3.png",200,1/2)
only_sin("sin_wave_4.png",200,10)
only_sin("sin_wave_5.png",200,1/10)

only_sin_2("sin_cut.png",200,1/5)
only_sin_2("sin_cut_2.png",200,1/5,25)
only_sin_2("sin_cut_3.png",200,1/5,75)

colors("colors.png",200)
colors("colors2.png",200,1/7)
colors("colors3.png",200,1/5)
colors("colors4.png",200,1/3)









