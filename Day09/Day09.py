import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(9)

def moveHead(direction):
  if direction == "R":
    head["col"] += 1
  elif direction == "L":
    head["col"] -= 1
  elif direction == "U":
    head['row'] += 1
  elif direction == "D":
    head["row"] -= 1
  else:
      assert False


def moveTail2(tailNumber):
  tail = tails[tailNumber]
  previousTail = head
  if j-1 > 0:
    previousTail = tails[tailNumber-1]
  
  moveTail(previousTail, tail, tailNumber=tailNumber)
  
  if tailNumber == 9:
    tailVisited.add((tail['row'], tail['col']))
    #print(tailVisited)

def moveTail(head, tail, tailNumber = 0):
  if abs(head['row'] - tail['row']) <= 1 and abs(tail['col'] - head['col']) <= 1: 
    return

  dr = 0 if head['row'] == tail['row'] else 1
  dc = 0 if head['col'] == tail['col'] else 1

  if dr == 1:
    if head['row'] > tail['row']:
      tail['row'] += 1
    else:
      tail['row'] -= 1
  
  if dc == 1:
    if head['col'] > tail['col']:
      tail['col'] += 1
    else:
      tail['col'] -= 1
  
  if tailNumber == 0 or tailNumber == 9:
    tailVisited.add((tail['row'], tail['col']))

for i in range(2):
  tailVisited = set()
  tailVisited.add((0,0))
  head = {"row": 0, "col": 0}
  tail = {"row": 0, "col": 0}
  tails = {1: {"row": 0, "col": 0}, 2: {"row": 0, "col": 0}, 3: {"row": 0, "col": 0}, 4: {"row": 0, "col": 0}, 5: {"row": 0, "col": 0}, 6: {"row": 0, "col": 0}, 7: {"row": 0, "col": 0}, 8:{"row": 0, "col": 0}, 9: {"row": 0, "col": 0}}

  if i == 0:
    for line in _input:
      direction, units = line.split()
      units = int(units)
      
      for i in range(1, units+1):
        moveHead(direction)  
        moveTail(head, tail)

  else:
    for line in _input:
      direction, units = line.split()
      units = int(units)
      
      for i in range(1, units+1):
        moveHead(direction)  
        for j in range(1, 10):
          moveTail2(j)
  print(len(tailVisited))