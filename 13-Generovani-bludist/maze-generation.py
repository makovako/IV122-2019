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
        if 0 <= x + nx < size and 0 <= y + ny < size: # if neighbour is in boundries of maze
            neighbours.append((x + nx,y + ny))
    random.shuffle(neighbours) # shuffle the order of neighbours so dfs will go random path
    return neighbours

def dfs(maze,start):
    size = len(maze)
    stack = []
    stack.append((start,None)) # pair of vertex to proces and previous one, so i can create edge
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

# It create lines of string
# "." - vertex or path
# "-", "|" - wall
# "+" - corners
def draw_maze(maze,edges):
    size = len(maze)
    out = []
    out.append("".join(["+-" * (size)]+["+"])) # first line always walls
    for i in range(size):
        line = "|"
        for j in range(size):
            line += "."
            if j < size-1:
                if ((j,i),(j+1,i)) in edges or ((j+1,i),(j,i)) in edges: # if there is edge, put path there
                    line += "."
                else: # otherwise wall
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

# points - list of pairs of indexis where to print circle in maze
# lenght - size of one side of square in maze
# maze - drawn maze (list of string lines)
def save_maze(filename,maze,length,points):
    size = len(maze)
    y = length/2
    vg = vector_graphic(filename,(size+1)/2*length,(size+1)/2*length)
    vg.start()
    # first draw horizontal lines
    for i in range(0,size,2):
        x = length/2
        for j in range(1,size,2):
            char = maze[i][j]
            if char == "-":
                vg.line(x,y,x + length, y)
            x += length
        y += length
    y = length/2
    # then draw vertical lines
    for i in range(1,size,2):
        x = length/2
        for j in range(0,size,2):
            char = maze[i][j]
            if char == "|":
                vg.line(x,y,x,y + length)
            x += length
        y += length
    # print given points as circes
    for point in points:
        x,y = point
        x *= length
        y *= length
        x += length
        y += length
        vg.circle(x,y,length / 3,fill="black")
    vg.stop()

# helper method to easily print some maze
def construct_maze(filename,size,length):
    maze = create_full_maze(size)
    edges = dfs(maze, (0,0))
    drawn_maze = draw_maze(maze,edges)
    save_maze(filename,drawn_maze,length,[(0,0),(size - 1, size - 1)])      

construct_maze("square_maze.svg",10,20)
construct_maze("square_maze-odd.svg",9,20)
