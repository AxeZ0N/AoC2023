import itertools
import pdb
import re
import pprint
import numpy
import math

with open('input.txt') as f:
    grid = [[x for x in y.strip()] for y in f.readlines()]

grid = numpy.array(grid)

grid = numpy.pad(grid, 1, 'constant', constant_values='.')

#for x in grid:
#    for y in x:
#        if re.findall(r'[^A-Za-z0-9]', y):continue
#        else: print(y,end='')
#
#exit()

def squareCoords(center_x,center_y):
    coords = []
    for x in range(-1,2):
        for y in range(-1,2):
            if x==y==0: pass
            else: coords.append((center_x+x,center_y+y))
    return coords

def testSurroundingSquare(grid, coords, reg):
    p_list = squareCoords(*coords)

    for x,y in p_list:
        try: p = grid[x][y]
        except IndexError: continue
        point_pass = re.findall(reg, p)
        if point_pass: return True
    return False

def testSurroundingSquareWithCoords(grid, coords, reg):
    p_list = squareCoords(*coords)

    found_list = []

    for x,y in p_list:
        try: p = grid[x][y]
        except IndexError: continue
        point_pass = re.findall(reg, p)
        if point_pass: found_list.append((x,y))

    if found_list: return found_list
    else: return False

def touchesSpecial(grid, coords, print_coords=False):
        reg = r'[^A-Za-z0-9.]'
        if not coords:
            test = testSurroundingSquare(grid, coords, reg)
        else: 
            test = testSurroundingSquareWithCoords(grid, coords, reg)
        return test

def touchesDigit(grid, coords, print_coords=False):
        reg = r'\d'
        if not coords:
            test = testSurroundingSquare(grid, coords, reg)
        else: 
            test = testSurroundingSquareWithCoords(grid, coords, reg)
        return test

def touchesGear(grid, coords, print_coords=False):
        reg = r'\*'
        if not coords:
            test = testSurroundingSquare(grid, coords, reg)
        else: 
            test = testSurroundingSquareWithCoords(grid, coords, reg)
        return test

def testPoint(point, reg):
    test = re.findall(reg, point)
    if test: return test[0]
    else: return False

def isDigit(point):
    test = testPoint(point, r'\d')
    return test

def isGear(point):
    test = testPoint(point, r'\*')
    return test

def testNumberBordersSpecial(digits, test_list):
    if (any(x for x in test_list[-len(digits):])): return True
    else: return False

def testGrid(grid):
    num_list = []
    test_list = []

    for i,row in enumerate(grid):
        number = ''
        for j,point in enumerate(row):
            is_digit = isDigit(point)
#            print(f'{point} is digit? {is_digit != False}')
            if is_digit:
                number += point
                test_list.append(touchesSpecial(grid, (i,j)))
#                print(f' {point} touches special char? {test_list[-1]}')

            elif len(number) >= 1:
                is_valid_number = testNumberBordersSpecial(number, test_list)
                if is_valid_number: num_list.append(int(number))
#                print(number, test_list[-len(number):])
                number = ''

#    print(num_list)
    return num_list

def isUniqueNumber(grid, num_coords_1, num_coords_2):
    print(num_coords_1)
    print(num_coords_2)

def buildNumber(grid, coord_x, coord_y, coords_only=False):
    number = grid[coord_x][coord_y]
    x_list = set()
    y_list = set()

    coord_y_new = coord_y
    while True:
        coord_y_new = coord_y_new + 1
        test_point = grid[coord_x][coord_y_new]
        if isDigit(test_point):
            number = number + test_point
            x_list.add(coord_x)
            y_list.add(coord_y)
        else: break

    coord_y_new = coord_y
    while True:
        coord_y_new = coord_y_new - 1
        test_point = grid[coord_x][coord_y_new]
        if isDigit(test_point):
            number = test_point + number
            x_list.add(coord_x)
            y_list.add(coord_y)
        else: break

    number_list = [(x,y) for x,y in zip(x_list,y_list)]
    if coords_only: return number_list
    else: return number

num_list = []
def partTwo():
    for i,row in enumerate(grid):
        for j,point in enumerate(row):
            if isGear(point) and touchesDigit(grid, (i,j)):
                touching_coords = touchesDigit(grid, (i,j), print_coords=True)
                
                potential_numbers = set()
                for coord in touching_coords:
                    potential_numbers.add(int(buildNumber(grid, *coord)))
                
                if len(potential_numbers) == 2:
                    ratio = math.prod(potential_numbers)
                    num_list.append(ratio)

    print(sum(num_list))


#num_list = testGrid(grid)
#print(sum(num_list))
#print(num_list)
partTwo()

