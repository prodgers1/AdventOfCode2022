import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(22)

map = []

maxLength = max([len(x) for x in _input[:-2]])
height = len(_input) - 2

def parseDirections(line):
    i = 0
    directions = []
    while i < len(line):
        current = ""
        direction = ""
        for j in range(i, len(line), 1):
            if line[j] == 'R' or line[j] == 'L':
                direction = line[j]
                i = j
                break
            current += line[j]
        directions.append(int(current))
        directions.append(direction)
        i += 1
    return directions[:4001]



for line in _input:
    if len(line) == 0:
        break
    current = []
    for i in range(maxLength):
        if i >= len(line):
            current.append(' ')
        else:
            current.append(line[i])
    map.append(current)

directions = parseDirections(_input[-1])

start = (0,0)
for i in range(maxLength):
    if map[0][i] == '.':
        start = (0, i)
        break


path = [start]

def findStartingColumn(row, currentDirection):
    if currentDirection == 180: #if im going left i need to start at the rhs
        for i in range(maxLength-1, 0, -1):
            if map[row][i] != ' ':
                return i
    else:
        for i in range(maxLength):
            if map[row][i] != ' ':
                return i

def findStartingRow(col, currentDirection):
    if currentDirection == 270: #if i'm going up, i need to start at the end of the map
        for i in range(height-1, 0, -1):
            if map[i][col] != ' ':
                return i
    else:
        for i in range(height):
            if map[i][col] != ' ':
                return i

def move(numberOfSpaces, currentSpace, currentDirection):
    
    if currentDirection == 0:
        for i in range(1, numberOfSpaces+1, 1):
            r, c = currentSpace
            newC = c+1
            if newC == maxLength or map[r][newC] == ' ':
                newC = findStartingColumn(r, currentDirection)
            
            if map[r][newC] == '#':
                break

            path.append((r, newC))
            currentSpace = (r, newC)
    
    elif currentDirection == 180:
        
        for i in range(1, numberOfSpaces+1, 1):
            r, c = currentSpace
            newC = c-1
            if newC < 0 or newC == maxLength or map[r][newC] == ' ':
                newC = findStartingColumn(r, currentDirection)

            if map[r][newC] == '#':
                break
            path.append((r, newC))
            currentSpace = (r, newC)
    
    elif currentDirection == 90:
        for i in range(1, numberOfSpaces+1, 1):
            r, c = currentSpace
            newR = r+1
            if newR < 0 or newR == height or map[newR][c] == ' ':
                newR = findStartingRow(c, currentDirection)

            if map[newR][c] == '#':
                break
            path.append((newR, c))
            currentSpace = (newR, c)

    else: #up
        for i in range(1, numberOfSpaces+1, 1):
            r, c = currentSpace
            newR = r-1
            if newR < 0 or newR == height or map[newR][c] == ' ':
                newR = findStartingRow(c, currentDirection)

            if map[newR][c] == '#':
                break
            path.append((newR, c))
            currentSpace = (newR, c)

    return currentSpace

def turn(currentDirection, newDirection):
    modifier = 1
    if newDirection == 'L' or newDirection == 'U':
        modifier = -1
    return (currentDirection + (90 * modifier))  % 360

def update(printMap, direction, pathToDraw):
    draw = '>'
    if direction == 180:
        draw = '<'
    elif direction == 270:
        draw = '^'
    elif direction == 90:
        draw = 'v'

    for p in pathToDraw:
        printMap[p[0]][p[1]] = draw
    
    f = open("traverse.txt", "a")

    display = ""
    for l in range(maxLength):
        display += "".join(printMap[l])
        display += "\n"
    f.write(display + "\n\n")
    return printMap

def traverse(current):
    #printMap = deepcopy(map)
    # going to be R = 0, L = 180, D = 90, U = 270
    currentDirection = 0
    for direction in directions:
        if isinstance(direction, int):
            #prevPath = deepcopy(path)
            current = move(direction, current, currentDirection)
            #printMap = update(printMap, currentDirection, set(path) - set(prevPath))
            #print(path)
        else:
            #before = currentDirection
            currentDirection = turn(currentDirection, direction)
            #print(f'was: {before}, turned {direction} to: {currentDirection}')
    
    password = (1000 * (current[0]+1)) + (4 * (current[1]+1)) + (currentDirection // 90)
    print(password)

traverse(start)