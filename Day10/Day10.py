import sys
import math
import decimal
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(10)

X = 1
cycle = 1
toComplete = defaultdict()
toComplete[1] = 1
signals = []

for line in _input:
    cycle += 1
    updateAmt = 0
    toComplete[cycle] = X
    if "noop" in line:
        pass
    elif 'addx' in line:
        _, amt = line.split()
        updateAmt = int(amt)
        toComplete[cycle+1] = X + updateAmt
        cycle += 1
    X += updateAmt

ans = 0
for i in [20, 60, 100, 140, 180, 220]:
    #print(i, toComplete[i], i * toComplete[i])
    ans += (i * toComplete[i])

print("Part 1: " + str(ans))
print()

print("Part 2:")
X = 1
picture = [['  ' for i in range(40)] for j in range(6)]
for i in range (0, 240):
    cycle = i + 1
    row = i // 40
    pos = i % 40
    if abs(X - pos) < 2:
        picture[row][pos] = '# '
    X = toComplete[cycle+1]

for line in picture:
    print("".join(line))