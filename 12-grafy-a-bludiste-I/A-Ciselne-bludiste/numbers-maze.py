import json
import queue

def read_file(filename):
    mazes = []
    with open(filename,"r") as f:
        line = f.readline()
        while line:
            if line == "---\n":
                pass
            else:
                size = int(line)
                maze = []
                for _ in range(size):
                    row = f.readline().split()
                    maze.append([int(c) for c in row])
                mazes.append(maze)
            line = f.readline()
    return mazes

def solve_maze(maze):
    # queue stores a pair
    # first element is point to analyze
    # second element is list of points, how we got to current point
    q = queue.Queue()
    size = len(maze)
    goal = (size-1, size-1)
    start = (0,0)
    boundries = range(size)
    q.put((start,[start]))
    result = []
    while True:
        # if queue is empty, we cant go anywhere, we cant find right path
        if q.empty():
            return []
        current, solution = q.get()
        if current == goal: # if we have found solution
            if len(result) == 0: # if we have no result yet, save this one
                result.append(solution)
            else: # check if we have same or worse solution (same length or longer), if worse we have finnished, if same we have found more solutions
                if len(solution) == len(result[0]):
                    result.append(solution)
                else:
                    return result

        x,y = current
        jump = maze[x][y]
        candidates = [(x+jump,y),(x,y+jump),(x-jump,y),(x,y-jump)] # all possible jumps from current
        for cx, cy in candidates:
            if cx in boundries and cy in boundries: # if we are still in maze, queue new point
                next_point = (cx,cy)
                next_solution = solution[:]
                next_solution.append(next_point)
                q.put((next_point,next_solution))

# maze - maze to print
# indexes - if to print indexes (booelan)
def print_maze(maze, indexes):
    if indexes:
        size = len(maze)
        print("x\\y{}".format("".join(["\t{}".format(i) for i in range(size)])))
        for i in range(size):
            print("{}{}".format(i,"".join(["\t{}".format(j) for j in maze[i]])))
    else:
        size = len(maze)
        for i in range(size):
            print("{}".format("".join(["\t{}".format(j) for j in maze[i]])))

# maze - maze to solve and print
def print_solution(maze):
    solution = solve_maze(maze)
    print("Found {} {}.".format(len(solution),"solution" if len(solution) == 1 else "solutions"))
    print_maze(maze,True)
    for i in range(len(solution)): # print solutions
        print("Solution {}: {}".format(i+1,solution[i]))


mazes = read_file("ciselne-bludiste.txt")
print("Careful! first index is horizontal, second index is vertical")
for maze in mazes:
    print_solution(maze)
    print("{}".format("".join(["-"]*30))) # print 30 "-" to seperate mazes

mazes = read_file("custom_maze.txt")
print("Custom maze with 6 solutions")
for maze in mazes:
    print_solution(maze)
    print("{}".format("".join(["-"]*30))) # print 30 "-" to seperate mazes