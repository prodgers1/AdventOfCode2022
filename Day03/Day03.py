import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(3)

def part1(inputCopy):
  score = 0
  for line in inputCopy:
    length =  len(line)
    firstCompartment = line[0:((length//2))]
    secondCompartment = line[(length//2):]

    common = ''.join(set(firstCompartment).intersection(secondCompartment))

    if 'a' <= common <= 'z':
      score += (ord(common) - ord('a') + 1)
    if 'A' <= common <= 'Z':
      score += (ord(common) - ord('A') + 27)

  print(score)

def part2(inputCopy):
  lines = []
  score = 0
  for line in inputCopy:
    if len(lines) == 2:
      lines.append(line)
      common = ''.join(set(lines[0]).intersection(lines[1]).intersection(lines[2]))

      if 'a' <= common <= 'z':
        score += (ord(common) - ord('a') + 1)
      if 'A' <= common <= 'Z':
        score += (ord(common) - ord('A') + 27)
      lines = []
    else:
      lines.append(line)
  print(score)

  

part1(deepcopy(_input))
part2(deepcopy(_input))