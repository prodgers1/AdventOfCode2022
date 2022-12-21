import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(21)

monkeys = {}

for line in _input:
  line = line.split()
  monkeyName = line[0].rstrip(":")
  if line[1].isdigit():
    monkeys[monkeyName] = int(line[1])
  else:
    monkeys[monkeyName] = line[1:]

def operate(lhs, rhs, operator):
  if operator == '+':
    return lhs + rhs
  elif operator == '-':
    return lhs - rhs
  elif operator == '*':
    return lhs * rhs
  elif operator == '/':
    return lhs // rhs

def recurse(monkeyName):
  monkey = monkeys[monkeyName]

  if isinstance(monkey, int):
    return monkey
  else:
    lhs = recurse(monkey[0])
    operator = monkey[1]
    rhs = recurse(monkey[2])
    return operate(lhs, rhs, operator)

print(recurse('root'))