import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(6)[0]


def findStartOfPacketMarker(line, marker):
  for index in range(marker, len(line), 1):
    sub = line[index - marker:index]
    distinct = set(sub)
    if len(distinct) == len(sub):
      print(index)
      break

findStartOfPacketMarker(_input, 4)
findStartOfPacketMarker(_input, 14)