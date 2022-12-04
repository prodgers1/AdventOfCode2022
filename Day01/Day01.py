import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(1)

maxCalories = []
current = 0

for line in _input:
  if len(line) == 0:
    maxCalories.append(current)
    current = 0
  else:
    current += int(line)
maxCalories.append(current)

print(sorted(maxCalories, reverse=True)[0])
top3 = sum(sorted(maxCalories, reverse=True)[0:3])
print(top3)