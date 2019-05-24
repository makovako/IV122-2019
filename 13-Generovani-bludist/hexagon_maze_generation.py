import random
from math import sqrt
from vector_graphic import vector_graphic

def create_full_maze(size):
    maze = []
    for _ in range(size):
        line = []
        for _ in range(2*size):
            line.append(False)
        maze.append(line)
    return maze

def get_neighbours(vertex, size):
    x,y = vertex
    neighbours = []
    max_x = 2*size
    for nx, ny in [(1,-1),(2,0),(1,1),(-1,1),(-2,0),(-1,-1)]:
        if 0 <= x + nx < max_x and 0 <= y + ny < size:
            neighbours.append((x + nx, y + ny))
    random.shuffle(neighbours)
    return neighbours

def dfs(maze,start):
    size = len(maze)
    stack = []
    stack.append((start,None))
    edges = [] # pair of points where the wall shoulde be deleted
    while stack:
        vertex, previous = stack.pop()
        # print("vertex: {}, previous: {}".format(vertex,previous))
        if not maze[vertex[1]][vertex[0]]:
            maze[vertex[1]][vertex[0]] = True
            if previous is not None:
                edges.append((previous,vertex))
            for neighbour in get_neighbours(vertex, size):
                stack.append((neighbour,vertex))
    return edges

def draw_maze(maze,edges):
    size = len(maze)
    out = []
    out.append("".join(["/\\"] * size))
    for i in range(size):
        line = ""
        if i % 2 == 1:
            line += " "
        for j in range(0,size*2,2):
            if i % 2 == 1:
                j += 1
            if ((j,i),(j-2,i)) in edges or ((j-2,i),(j,i)) in edges:
                line += " " # TODO  ???
            else:
                line += "|"

            if ((j,i),(j+2,i)) in edges or ((j+2,i),(j,i)) in edges:
                line += " " # TODO  ???
            else:
                line += "|"
        # line += "|"
        out.append(line)
        line = ""
        if i % 2 == 1 and i != (size-1):
            line += "/"
        if i == size -1:
            line += " "
        for j in range(0,size*2,2):
            if i % 2 == 1:
                j += 1
            if ((j,i),(j-1,i+1)) in edges or ((j-1,i+1),(j,i)) in edges:
                line += " " # TODO  ???
            else:
                line += "\\"
            if ((j,i),(j+1,i+1)) in edges or ((j+1,i+1),(j,i)) in edges:
                line += " " # TODO  ???
            else:
                line += "/"
        if i % 2 == 0 and i != (size-1):
            line += "\\"
        out.append(line)
        
    return out

def print_maze(maze):
    for line in maze:
        print(line)

def save_maze(filename, maze, edges, length, dots):
    size = len(maze)
    # - x,y - coordinates of the middle of hexagon
    y = length
    # Constants
    S3 = sqrt(3) # square root of 3
    LH = length / 2 # length halfed
    S3L = S3 * length / 2 # height of triangle in hexagon
    vg = vector_graphic(filename,2*size*length,2*size*length)
    vg.start()
    # j,i indexes of heaxgon in maze
    for i in range(size):
        x = length
        if i % 2 == 1:
            x += S3*length/2 # offset every other row of hexagon
        for j in range(0,size*2,2):
            if i % 2 == 1:
                j += 1 # offset every other index
            points = [(x,y - length),
                        (x - S3L,y - LH),
                        (x - S3L,y + LH),
                        (x,y+length),
                        (x + S3L,y + LH),
                        (x + S3L,y - LH),
                        (x,y - length)
                        ] # coordinates of hexagon, first vertex twice
            change = [(-1,-1),(-2,0),(-1,1),(1,1),(2,0),(1,-1)] # change of index in the maze
            for index in range(len(points)-1):
                nx, ny = change[index]
                if not (((j,i),(j+nx,i+ny)) in edges or ((j+nx,i+ny),(j,i)) in edges): # if there is edge (from DFS), dont draw a line
                    vg.line(points[index][0],points[index][1],points[index+1][0],points[index+1][1])
            for dot in dots:
                dx,dy = dot
                if j == dx and i == dy:
                    vg.circle(x,y,length/2,fill="black")
            x += S3 * length
        
        y += 3*length/2
    vg.stop()

def construct_maze(filename,size,length):
    maze = create_full_maze(size)
    edges = dfs(maze,(0,0))
    save_maze(filename,maze,edges,length,[(0,0),(size*2 -1,size-1)])

construct_maze("hexagon_maze.svg",20,20)
construct_maze("hexagon_maze-odd.svg",19,20)
