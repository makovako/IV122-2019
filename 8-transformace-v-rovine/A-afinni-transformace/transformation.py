from vector_graphic import vector_graphic
from math import sin, cos, radians

# Class for transforming lines
class transformation(object):
    # filename - name of file to save the image
    # lines - list of lines, line is a list of points
    # repeat - number of times to repeat operations
    # 0 or more operations to apply on lines, operations should be separate parameters
    def __init__(self, filename, lines, repeat, *operations):
        self.filename = filename
        self.lines = lines
        self.repeat = repeat
        self.operations = operations
        self.process()
    
    # Process the lines and save image
    def process(self):
        if self.operations:
            self.transform()
        self.create_image()

    def create_image(self):
        # fliping the image, finding boundries, and moving lines to positive coordinates
        flipped_lines = []
        flip_matrix = [[1,0,0],[0,-1,0],[0,0,1]]
        for line in self.lines:
            flipped_lines.append(self.transform_line(flip_matrix,line))
        boundries = [0,0,0,0]
        for line in flipped_lines:
            boundries[0] = min(line[0][0],line[1][0],boundries[0]) # min x
            boundries[1] = min(line[0][1],line[1][1],boundries[1]) # min y
            boundries[2] = max(line[0][0],line[1][0],boundries[2]) # max x
            boundries[3] = max(line[0][1],line[1][1],boundries[3]) # max y
        final_lines = []
        move_matrix = translation(-boundries[0] + 1, -boundries[1] + 1) # +1 so there will be 1 pixel margin
        for line in flipped_lines:
            final_lines.append(self.transform_line(move_matrix, line))
        
        v = vector_graphic(self.filename,boundries[2] - boundries[0] + 2,boundries[3] - boundries[1] + 2) # canvas size +2 = +1 pixel margin on each side
        v.start()
        for line in final_lines:
            v.line(line[0][0],line[0][1],line[1][0],line[1][1])
        v.stop()

    def transform(self):
        matrices = []
        for operation in self.operations:
            matrices.append(operation) # list of transformation matrices
        final_matrix = self.merge_transformations(matrices) # create one transformation matrix
        
        processing_lines = self.lines[:] # current lines that are being processed
        all_lines = self.lines[:] # all lines to be drawn at the end
        for _ in range(self.repeat):
            new_lines = [] # lines after transformation, they are new lines in the next round of transformation
            for line in processing_lines:
                transformed_line = self.transform_line(final_matrix,line)
                new_lines.append(transformed_line)
                all_lines.append(transformed_line)
            processing_lines = new_lines[:]
        self.lines = all_lines[:]
    
    # m = transformation matrix
    # l = line [[x1,y1],[x2,y2]]
    def transform_line(self, m, l):
        x = self.transform_point(m, l[0])
        y = self.transform_point(m, l[1])
        return [x,y]

    # m = transformation matrix
    # p = point to be transformed
    def transform_point(self, m, p):
        p.append(1)
        out = [0,0,0]
        for i in range(3):
            loc_out = 0
            for j in range(3):
                loc_out += m[i][j]*p[j]
            out[i] = loc_out
        return out [:2]

    # matrices - list of transformation matrices to be merged into one transformation matrix
    def merge_transformations(self, matrices):
        final_matrix = matrices[0]
        for i in range(1,len(matrices)):
            final_matrix = self.multiply_matrices(matrices[i],final_matrix)
        return final_matrix
    
    def multiply_matrices(self, m1, m2):
        out = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                loc_out = 0
                for k in range(3):
                    loc_out += m1[i][k] * m2[k][j]
                out[i][j] = loc_out
        return out

# following functions just create tranformation matrices

def rotation(angle):
    angle = radians(angle)
    return [[cos(angle),sin(angle),0],[-sin(angle),cos(angle),0],[0,0,1]]

def scaling(sx, sy):
    return [[sx,0,0],[0,sy,0],[0,0,1]]

def translation(dx, dy):
    return [[1,0,dx],[0,1,dy],[0,0,1]]

def shear(cx):
    return [[1,cx,0],[0,1,0],[0,0,1]]