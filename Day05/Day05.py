import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(5)


#000:'[N]     [C]                 [Q]'
#001:'[W]     [J] [L]             [J] [V]'
#002:'[F]     [N] [D]     [L]     [S] [W]'
#003:'[R] [S] [F] [G]     [R]     [V] [Z]'
#004:'[Z] [G] [Q] [C]     [W] [C] [F] [G]'
#005:'[S] [Q] [V] [P] [S] [F] [D] [R] [S]'
#006:'[M] [P] [R] [Z] [P] [D] [N] [N] [M]'
#007:'[D] [W] [W] [F] [T] [H] [Z] [W] [R]'
#008:' 1   2   3   4   5   6   7   8   9'

#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 

testStacks = [
  ['N', 'Z'],
  ['D', 'C', 'M'],
  ['P']
]

stacks = [
  ['N', 'W', 'F', 'R', 'Z', 'S', 'M' , 'D'],
  ['S', 'G', 'Q', 'P', 'W'],
  ['C', 'J', 'N', 'F', 'Q', 'V', 'R', 'W'],
  ['L', 'D', 'G', 'C', 'P', 'Z', 'F'],
  ['S', 'P', 'T'],
  ['L', 'R', 'W', 'F', 'D', 'H'],
  ['C', 'D', 'N', 'Z'],
  ['Q', 'J', 'S', 'V', 'F', 'R', 'N', 'W'],
  ['V', 'W', 'Z','G','S','M', 'R'],
]

#enable this to run the test input, still need to change the txt file tho
#stacks = testStacks
    

i = 0
while i < len(stacks):
  stacks[i].reverse()
  i += 1

part1 = False

for line in _input:
  _, howMany, _, fromStack, _, toStack = line.split()
  howMany = int(howMany)
  fromStack = int(fromStack) - 1
  toStack = int(toStack) - 1
  i = 0
  
  if part1:
    while i < howMany:
      popped = stacks[fromStack].pop()
      stacks[toStack].append(popped)
      i += 1
  else:
    toAdd = ""
    while i < howMany:
      toAdd += stacks[fromStack].pop()
      i += 1
    
    toAdd = toAdd[::-1]
    for i in range(len(toAdd)):
      stacks[toStack].append(toAdd[i])

ans = ""
for stack in stacks:
  first = stack.pop()
  ans += first

print(ans)