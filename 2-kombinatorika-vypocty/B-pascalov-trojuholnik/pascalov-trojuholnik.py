from PIL import Image

colors = [(255,0,0),#red
    (0,0,255),#green
    (0,255,0),#blue
    (255,255,0),#yellow
    (0,255,255),#aqua
    (255,0,255),#purple
    (255,128,255),#pink
    (255,128,0),#orange
    (128,255,128),#light green
    (128,128,255)]#light purple

# compute next line of pascal triangle
def next_line(inlist):
    l = [0] + inlist +[0]
    out  = []
    for i in range(len(l)-1):
        out.append(l[i] + l[i+1])
    return out

# name = name of file
# n = number of rows
# k = divider
def pascalov_trojuholnik(name,n=30,k=5):
    size = 7*n
    
    im = Image.new("RGB",(size,size),(255,255,255))
    # numbers in one line of a pascal triangle
    line = [1]
    # middle of square
    nextx = int(size/2)
    dx = -3
    nexty = 3
    dy = 6
    
    for _ in range(n):
        x = nextx
        y = nexty
        nextx = x + dx
        nexty = y + dy
        for i in range(len(line)):
            for a in range(x-3,x+3):
                for b in range(y-3,y+3):
                    im.putpixel((a,b),colors[line[i] % k])
            x += 6
        line = next_line(line)
    im.save("{}.png".format(name))



print('Drawing nice triangles')
pascalov_trojuholnik("triangle1")
pascalov_trojuholnik("triangle2",64,2)
pascalov_trojuholnik("triangle3",54,3)
pascalov_trojuholnik("triangle4",38,4)
pascalov_trojuholnik("triangle5",50,5)
pascalov_trojuholnik("triangle6",28,7)
pascalov_trojuholnik("triangle7",32,8)
pascalov_trojuholnik("triangle8",54,9)