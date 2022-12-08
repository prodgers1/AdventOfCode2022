import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(8)

height = len(_input)
width = len(_input[0])
highestScenicScore = 0
visible = set()

#up, right, down, left
DR = [-1, 0, 1, 0] #change in row
DC = [0, 1, 0, -1] #change in col

def isEdge(row, col):
  return row == 0 or col == 0 or row == height-1 or col == width-1

def checkNeighbors(row, col):
  for i in range(4):
    dx = row + DR[i]
    dy = col + DC[i]

    add = True
    while not isEdge(dx, dy):
      if not int(_input[row][col]) > int(_input[dx][dy]):
        add = False
        break

      dx = dx + DR[i]
      dy = dy + DC[i]
    
    if add and int(_input[row][col]) > int(_input[dx][dy]):
      return (row,col)
      
  return None

def findScenicScore(row, col):
  score = []
  for i in range(4):
    dx = row + DR[i]
    dy = col + DC[i]

    canSee = 1
    while not isEdge(dx, dy):
      if int(_input[row][col]) <= int(_input[dx][dy]):
        break
      canSee += 1

      dx = dx + DR[i]
      dy = dy + DC[i]
    score.append(canSee)
  
  result = 1
  for s in score:
    result *= s
  return result


for row in range(height):
  for col in range(width):
    if isEdge(row, col):
      visible.add((row,col))
      continue
    
    seen = checkNeighbors(row,col)
    if seen != None:
      visible.add(seen)    

    score = findScenicScore(row, col)
    if score > highestScenicScore:
      highestScenicScore = score

print(f"Total visible trees: {len(visible)}")
print(f"Highest Scenic Score: {highestScenicScore}")