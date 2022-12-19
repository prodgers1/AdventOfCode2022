import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(18)

droplets = set()

for line in _input:
    x, y, z = line.split(',')
    x = int(x)
    y = int(y)
    z = int(z)
    droplets.add((x,y,z))


directions = [(1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,1),(0,0,-1)]

def encapsulated(x,y,z):
    seen = set()
    queue = [(x,y,z)]
    seen.add((x,y,z))
    
    while queue:
        x,y,z = queue.pop(0)

        if min(x, y, z) < -1 or max(x, y, z) > 21:
            return False
        
        for dx, dy, dz in directions:
            xx = x + dx
            yy = y + dy
            zz = z + dz

            if (xx,yy,zz) not in seen and (xx,yy,zz) not in droplets:
                seen.add((xx,yy,zz))
                queue.append((xx,yy,zz))
    return True


def part1():
    area = 0
    for cube in droplets:
        for dx, dy, dz in directions:

            x1, y1, z1 = cube
            x2 = x1 + dx
            y2 = y1 + dy
            z2 = z1 + dz

            if (x2, y2, z2) not in droplets:
                area += 1
                
    print(area)

def part2():

    minX = min([x for (x, y, z) in droplets])
    minY = min([y for (x, y, z) in droplets])
    minZ = min([z for (x, y, z) in droplets])
    maxX = max([x for (x, y, z) in droplets])
    maxY = max([y for (x, y, z) in droplets])
    maxZ = max([z for (x, y, z) in droplets])

    air = set()
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            for z in range(minZ, maxZ):
                if encapsulated(x,y,z):
                    air.add((x,y,z))

    area = 0
    for cube in droplets:
        for dx, dy, dz in directions:
            x1, y1, z1 = cube
            x2 = x1 + dx
            y2 = y1 + dy
            z2 = z1 + dz

            if (x2, y2, z2) not in droplets and (x2,y2,z2) not in air:
                area += 1
    print(area)


part1()
part2()