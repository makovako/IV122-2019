from vector_graphic import vector_graphic
from math import sin, cos, radians

CIRCLE_ANGLE = 360

class Turtle(object):
    def __init__(self, x = 0, y = 0, angle = 0.0):
        self.x = x
        self.y = y
        self.angle = angle
        self.lines = []
        self.pen = True
        self.stack = []
        self.boundries = [0,0,0,0] # boudnries of canvas, min max points in both axis [left x, right x, top y, botttom y]

    def left(self, angle):
        self.angle = (self.angle - angle) % CIRCLE_ANGLE
        if self.angle < 0:
            self.angle += CIRCLE_ANGLE
    
    def right(self, angle):
        self.angle = (self.angle + angle) % CIRCLE_ANGLE
    
    def forward(self, distance):
        dx = (sin(radians(self.angle))) * distance
        dy = -(cos(radians(self.angle))) * distance
        if self.pen:
            self.lines.append((self.x, self.y, self.x + dx, self.y + dy))
        #calculating boundries
        self.boundries[0] = min(self.boundries[0], self.x, self.x + dx)
        self.boundries[1] = max(self.boundries[1], self.x, self.x + dx)
        self.boundries[2] = min(self.boundries[2], self.y, self.y + dy)
        self.boundries[3] = max(self.boundries[3], self.y, self.y + dy)
        self.x += dx
        self.y += dy
    
    def backward(self,distance):
        self.right(180)
        self.forward(distance)
        self.right(180)
    
    def penup(self):
        self.pen = False

    def pendown(self):
        self.pen = True

    def push(self):
        self.stack.append((self.x,self.y,self.angle))

    def pop(self):
        self.x, self.y, self.angle = self.stack.pop()

    def save_to_file(self, filename):
        # calculaitng size of canvas from boundries
        vg = vector_graphic(filename, self.boundries[1] - self.boundries[0],self.boundries[3] - self.boundries[2])
        vg.start()
        for x1, y1, x2, y2 in self.lines:
            # moving lines according to min boundries in both acis
            # "-" because if its negative number i neet to move positive size
            vg.line(x1 - self.boundries[0], y1 - self.boundries[2], x2 - self.boundries[0], y2 - self.boundries[2])
        vg.stop()

