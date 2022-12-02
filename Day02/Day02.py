import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(2)

#loss = 0  tie 3 win 6

choices = {
  'A': 1,
  'B': 2,
  'C': 3,
  'X': 1,
  'Y': 2,
  'Z': 3,
  'AX': 3,
  'AY': 6,
  'AZ': 0,
  'BX': 0,
  'BY': 3,
  'BZ': 6,
  'CX': 6,
  'CY': 0,
  'CZ': 3
}

def DetermineScore(choice1, choice2):
  if choice1 == 'A' and choice2 == 'X':
    return 3 + 1
  if choice1 == 'A' and choice2 == 'Y':
    return 6 + 2
  if choice1 == 'A' and choice2 == "Z":
    return 0 + 3
  
  if choice1 == 'B' and choice2 == 'X':
    return 0 + 1
  if choice1 == 'B' and choice2 == 'Y':
    return 3 + 2
  if choice1 == 'B' and choice2 == "Z":
    return 6 + 3

  if choice1 == 'C' and choice2 == 'X':
    return 6 + 1
  if choice1 == 'C' and choice2 == 'Y':
    return 0 + 2
  if choice1 == 'C' and choice2 == "Z":
    return 3 + 3

def DetermineHowToLose(choice1 , choice2):
  if choice1 == 'A' and choice2 == 'X':
    return 0 + 3
  if choice1 == 'A' and choice2 == 'Y':
    return 3 + 1
  if choice1 == 'A' and choice2 == "Z":
    return 6 + 2
  
  if choice1 == 'B' and choice2 == 'X':
    return 0 + 1
  if choice1 == 'B' and choice2 == 'Y':
    return 3 + 2
  if choice1 == 'B' and choice2 == "Z":
    return 6 + 3

  if choice1 == 'C' and choice2 == 'X':
    return 0 + 2
  if choice1 == 'C' and choice2 == 'Y':
    return 3 + 3
  if choice1 == 'C' and choice2 == "Z":
    return 6 + 1


scoreNew = 0
score1 = 0
score2 = 0

for line in _input:
  elfChoice, myChoice = line.split(' ')

  score = choices[elfChoice + myChoice]
  whatDidIPlay = choices[myChoice]
  scoreNew += score + whatDidIPlay

  score1 += DetermineScore(elfChoice, myChoice)
  score2 += DetermineHowToLose(elfChoice, myChoice)

print(scoreNew)
print(score1)
print(score2)