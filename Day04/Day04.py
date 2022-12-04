import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(4)

part1 = 0
part2 = 0

for line in _input:
    firstRange, secondRange = line.split(',')

    first, second = firstRange.split('-')
    third, forth = secondRange.split('-')

    firstList = set([*range(int(first), int(second) + 1, 1)])
    secondList = set([*range(int(third), int(forth) + 1, 1)])
    
    if firstList <= secondList or secondList <= firstList:
        part1 += 1
    
    if len(set(firstList).intersection(set(secondList))) > 0:
        part2 += 1

print(part1)
print(part2)