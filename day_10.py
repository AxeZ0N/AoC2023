'''
Problem 1:
    Write a parser for the input where symbols indicate pipes. 
    Pipes have two connections with 6 variants, empty space, and start
    Start pipe has two connections and is one loop.

    Start by designing a data structure for pipes.
    Input is small enough to hold whole grid in memory
    Input is 2D plane 
    each coord is a 'Tile'
    Each tile has an x,y coord.
    Tiles contain Pipes, Start or Ground.
    ground is impassable in all directions
    Directions are NESW
    0,0 is upper left corner
    North/South moves are -/+y
    East/West moves are +/-x
    Start is unique.
    Pipes have one entrance and one exit (pipes are not directional)

Problem 2:
    Shape of start pipe is unknown
    Have to trace paths until return to start
    Start at start, follow one of two conn in pipes.
'''

from dataclasses import *
import pdb

@dataclass
class Structure:
    coords: tuple[int,int]
    char: str

    def __str__(self):
        return self.char

@dataclass
class Ground(Structure):
    char: str = '.'
    pass

@dataclass
class Pipe(Structure):
    def __post_init__(self):
        self.conn = Pipe.buildPipe(self.char,self.coords)

    @classmethod
    def buildPipe(cls, c, coords):
        pd = {'|':'ns','-':'ew','7':'ws','L':'ne','J':'nw','F':'es'}

        conn = [move(x, coords) for x in pd[c]]

        return conn

@dataclass
class Start(Structure):
    char: str = 'S'

class Grid:
    def move(self, d, coords):
        x,y = move(d,coords)
        rv = self.grid[x][y]
        return rv

    def print(self):
        printGrid(self.grid)

def move(d, coords):
    ''' 
    (row, col)
    (x, y)
    '''
    x,y = coords
    match d:
        case 'n': x -= 1
        case 'e': y += 1
        case 's': x += 1
        case 'w': y -= 1

    coords = (x,y)
    return coords

def readInput(file_no):
    '''
    1 = input
    2 = test input
    3 = custom input
    '''
    file = {1:'input.txt', 2:'input_test.txt',3:'input_test_2.txt'}
    with open(file[file_no]) as f: return f.read()

def printGrid(g):
    for x in g:
        for y in x:
            print(y, end=' ')
        print()

def generateGrid(rows,cols):
    grid = [[Ground(coords=(y,x)) for x in range(rows+2)] for y in range(cols+2)]

    return grid

def buildStructure(c, coords):
    match c:
        case '.': return Ground(coords)
        case 'S': return Start(coords)
        case '|'|'7'|'F'|'L'|'J'|'-': return Pipe(coords, c)
        case _: return None

def populateGrid(grid, str_in):
    lines = str_in.split()
    start = None

    g = Grid()
    g.grid = grid

    for rows in range(0,len(lines)):
        for cols in range(0,len(lines[0])):
            struct = buildStructure(lines[rows][cols], (rows+1,cols+1))
            if type(struct) is Start: start = struct
            g.grid[rows+1][cols+1] = struct
    return g, start

def getNextPipeCoords(p: Pipe, coords):
    if type(p) is Start: return None
    return [x for x in p.conn if x != coords][0]

def followPipe(start_pipe, start_coords):
    if type(start_pipe) is not Start: return 'Not Start'

    directions = [move(x, start_pipe.coords) for x in ['n','s','e','w']]

    list_of_start_pipes = [grid.grid[x[0]][x[1]] for x in directions]

    ret_pipes = []

    for pipe in list_of_start_pipes:
        curr_pipe = pipe
        prev_coords = start_coords
        pipes_list = []
        loop_len = 0

        while True:
            if type(curr_pipe) is Ground: break
            pipes_list.append(curr_pipe)
            loop_len += 1

            for conn in curr_pipe.conn:
                tmp_coords = getNextPipeCoords(curr_pipe, prev_coords)
                if tmp_coords != prev_coords: next_coords = tmp_coords

            next_pipe = grid.grid[next_coords[0]][next_coords[1]]
            if type(next_pipe) is Start: 
                flag=True
                break

            if not isConnected(curr_pipe, next_pipe): break

            prev_coords = curr_pipe.coords
            curr_pipe = next_pipe

        ret_pipes.append(pipes_list)

    return ret_pipes

def buildGrid():
    input_text = readInput(1)
    row_len, col_len = len(input_text.split()), len(input_text.split()[0])
    grid = populateGrid(generateGrid(row_len, col_len), input_text)
    return grid

def isConnected(p1, p2):
    return p1.coords in p2.conn

def printPath(grid, path):
    path = [x.coords for x in path]
    for x in grid:
        for y in x:
            if y == start: print('S', end=' ')
#            elif y == up: print('U',end=' ')
#            elif y == down: print('D',end=' ')
#            elif y == left: print('X',end=' ')
#            elif y == right: print('R',end=' ')
            elif y.coords in path: print(y.char, end=' ')
            else: print('.',end=' ')
        print()

grid,start = buildGrid()

val = followPipe(start, start.coords)
loop_len = len(val)

up = grid.move('n', start.coords)
down = grid.move('s', start.coords)
left = grid.move('w', start.coords)
right = grid.move('e', start.coords)

print(len(val))

print([len(val[x]) for x in range(4)])

print(len(val[0]) / 2)

printPath(grid.grid, val[0])
