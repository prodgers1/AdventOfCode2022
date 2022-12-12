import sys
import math
import heapq
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(12)

#directions,   down right left up
DR = [1, 0, 0, -1,] #change in row
DC = [0, 1, -1, 0] #change in col

def findStart():
    starts = []
    for row in range(len(_input)):
        for col in range(len(_input[0])):
            if ord(_input[row][col]) == ord('S') or ord(_input[row][col]) == ord('a'):
                starts.append((row, col))
    return starts
            

start = findStart()
queue = []
for s in start:
    queue.append((0, s, [], 0))
seen = set()

while queue:
    cost, (row,col), path, steps = heapq.heappop(queue)
    if (row,col) in seen:
        continue
    current = ord(_input[row][col])
    if current == ord('S'):
        current = ord('a')

    path = path + [(row,col)]
    seen.add((row,col))

    if ord(_input[row][col]) == ord('E'):
        print(steps)
        break

    for d in range(4):
        dr = row + DR[d]
        dc = col + DC[d]
        if 0 <= dr < len(_input) and 0 <= dc < len(_input[0]):
            nextOrd = ord(_input[dr][dc])
            if nextOrd == ord('E'):
                nextOrd = ord('z')
            if nextOrd - current <= 1:
                newCost = cost + nextOrd + steps
                heapq.heappush(queue, (newCost, (dr, dc), path, steps + 1))
