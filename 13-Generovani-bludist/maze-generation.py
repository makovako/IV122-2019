import random
from vector_graphic import vector_graphic

def create_full_maze(size):
    maze = []
    for _ in range(size):
        line = []
        for _ in range(size):
            line.append(False)
        maze.append(line)
    return maze

def get_neighbours(vertex, size):
    x,y = vertex
    neighbours = []
    for nx, ny in [(0,-1),(1,0),(0,1),(-1,0)]:
        if 0 <= x + nx < size and 0 <= y + ny < size:
            neighbours.append((x + nx,y + ny))
    random.shuffle(neighbours)
    return neighbours

def dfs(maze,start):
    size = len(maze)
    stack = []
    stack.append((start,None))
    edges = [] # pair of points where the wall should be deleted
    while stack:
        vertex, previous = stack.pop()
        if not maze[vertex[0]][vertex[1]]:
            maze[vertex[0]][vertex[1]] = True
            if previous is not None:
                edges.append((previous,vertex))
            for neighbour in get_neighbours(vertex, size):
                stack.append((neighbour,vertex))
    return edges


def draw_maze(maze,edges):
    size = len(maze)
    out = []
    out.append("".join(["+-" * (size)]+["+"]))
    for i in range(size):
        line = "|"
        for j in range(size):
            line += "."
            if j < size-1:
                # edge = (((j,i),(j+1,i)))
                if ((j,i),(j+1,i)) in edges or ((j+1,i),(j,i)) in edges:
                    line += "."
                else:
                    line += "|"
        line += "|"
        out.append(line)
        line = ""
        for j in range(size):
            line += "+"
            if ((j,i),(j,i+1)) in edges or ((j,i+1),(j,i)) in edges:
                line += "."
            else:
                line += "-"
        line += "+"
        out.append(line)
    return out
            

def print_maze(maze):
    for line in maze:
        print(line)

def save_maze(filename,maze,length,points):
    size = len(maze)
    y_coor = length/2
    vg = vector_graphic(filename,(size+1)/2*length,(size+1)/2*length)
    vg.start()
    for x in range(0,size,2):
        x_coor = length/2
        for y in range(1,size,2):
            char = maze[x][y]
            if char == "-":
                vg.line(x_coor,y_coor,x_coor + length, y_coor)
            x_coor += length
        y_coor += length
    y_coor = length/2
    for y in range(1,size,2):
        x_coor = length/2
        for x in range(0,size,2):
            char = maze[y][x]
            if char == "|":
                vg.line(x_coor,y_coor,x_coor,y_coor + length)
            x_coor += length
        y_coor += length
    for point in points:
        x,y = point
        x *= length
        y *= length
        x += length
        y += length
        vg.circle(x,y,length / 3,fill="black")
    vg.stop()
    
def construct_maze(filename,size,length):
    maze = create_full_maze(size)
    edges = dfs(maze, (0,0))
    drawn_maze = draw_maze(maze,edges)
    save_maze(filename,drawn_maze,length,[(0,0),(size - 1, size - 1)])      

construct_maze("square_maze.svg",10,20)
construct_maze("square_maze-odd.svg",9,20)
