import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
from functools import cmp_to_key
_input = GetInput(13)

def compare(int1, int2):
    if int1 < int2:
        return -1
    elif int1 == int2:
        return 0
    else:
        return 1

def parseList(left, right):
    value = True
    if type(left) is list and type(right) is list:
        i = 0
        while i < len(left) and i < len(right):
            value = parseList(left[i], right[i])
            if value == -1:
                return value
            if value == 1:
                return value
            i += 1
        
        if i == len(left) and i < len(right):
            return -1
        elif i == len(right) and i < len(left):
            return 1
        else:
            return 0

    elif type(left) is int and type(right) is int:
        return compare(left, right)        
    
    elif type(left) is list and type(right) is int:
        return parseList(left, [right])
    
    elif type(left) is int and type(right) is list:
        return parseList([left], right)
    


i = 0
ans = []
packetIndex = 0
packets = []
while i < len(_input):
    if len(_input[i]) != 0:
        i += 1
        continue
    packetIndex += 1
    left = eval(_input[i-2])
    right = eval(_input[i-1])
    packets.append(left)
    packets.append(right)

    #print(left, right)

    value = parseList(left, right)

    if value == -1:
       ans.append(packetIndex)
    i += 1

packets.append(eval(_input[i-2]))
packets.append(eval(_input[i-1]))

print(sum(ans))

packets.append([[2]])
packets.append([[6]])

sortedPackets = sorted(packets, key=cmp_to_key(lambda item1, item2: parseList(item1, item2)))
print((sortedPackets.index([[2]]) + 1) * (sortedPackets.index([[6]]) + 1)) #starts at index 1