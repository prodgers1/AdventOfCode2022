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
    
    first = int(first)
    second = int(second)
    third = int(third)
    forth = int(forth)

    # this was my first initial approach but had the operators swapped for the first expression -.-
    if (first >= third and second <= forth) or (third >= first and forth <= second):
        part1 += 1

    # second cleaner approach using sets to check subsets
    #if firstList <= secondList or secondList <= firstList:
    #    part1 += 1
    
    if len(set(firstList).intersection(set(secondList))) > 0:
        part2 += 1

print(part1)
print(part2)