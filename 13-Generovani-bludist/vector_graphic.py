class vector_graphic(object):

    # file = filename
    # width, height - size of the viewport
    def __init__(self, file, width = 0, height = 0):
        self.file = open(file,"w")
        self.width = width
        self.height = height
    
    # Starts the svg file
    def start(self):
        if self.width > 0 and self.height > 0:
            self.file.write('<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">\n'.format(self.width,self.height))
            self.file.write('<rect width="100%" height="100%" fill="white"/>\n')
        else:
            self.file.write('<svg xmlns="http://www.w3.org/2000/svg">\n')
            self.file.write('<rect width="100%" height="100%" fill="white"/>\n')

    
    # Ends the svg file and closes it
    def stop(self):
        self.file.write("</svg>\n")
        self.file.close()

    # Draw line
    def line(self, x1, y1, x2, y2, stroke="black", stroke_width="1"):
        self.file.write('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" stroke-width="{}"/>\n'.format(x1,y1,x2,y2,stroke,stroke_width))
    
    # Draw circle
    def circle(self, cx, cy, r, stroke="black", stroke_width="1",fill="white"):
        self.file.write('<circle cx="{}" cy="{}" r="{}" stroke="{}" stroke-width="{}" fill="{}"/>\n'.format(cx,cy,r,stroke,stroke_width,fill))