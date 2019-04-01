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

    def left(self, angle):
        self.angle = (self.angle - angle) % CIRCLE_ANGLE
        if self.angle < 0:
            self.angle += CIRCLE_ANGLE
    
    def right(self, angle):
        self.angle = (self.angle - angle) % CIRCLE_ANGLE
    
    def forward(self, distance):
        dx = (sin(radians(self.angle))) * distance
        dy = -(cos(radians(self.angle))) * distance
        if self.pen:
            self.lines.append((self.x, self.y, self.x + dx, self.y + dy))
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

    # offset - move lines by offset
    def save_to_file(self, filename, off_x = 150, off_y = 150):
        vg = vector_graphic(filename)
        vg.start()
        for x1,y1,x2,y2 in self.lines:
            vg.line(x1 + off_x, y1 + off_y, x2 + off_x, y2 + off_y)
        vg.stop()