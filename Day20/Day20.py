import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(20)

fileLength = len(_input)

def shuffle(mixedFile, inputCopy):
  for i, value in enumerate(inputCopy):
    #print(", ".join([str(x[1]) for i, x in enumerate(mixedFile)]))
    toFind = (i, value)
    currentIndex = mixedFile.index(toFind)
    
    #  First take out the number we are going to be moving, then find the index it needs to go in within that new list which is a length - 1
    temp = mixedFile[:currentIndex] + mixedFile[currentIndex+1:]
    newIndex = (currentIndex + value) % (fileLength - 1)
    temp.insert(newIndex, toFind)

    mixedFile = temp

  return mixedFile


def outputAns(mixedFile):
  zeroIndex = -1
  for i, x in enumerate(mixedFile):
    if x[1] == 0:
      zeroIndex = i
      break

  offset = zeroIndex
  #print(mixedFile[(offset+1000)%fileLength][1], mixedFile[(offset+2000)%fileLength][1], mixedFile[(offset+3000)%fileLength][1])
  print(mixedFile[(offset+1000)%fileLength][1] + mixedFile[(offset+2000)%fileLength][1] + mixedFile[(offset+3000)%fileLength][1])
    
def part1(mixedFile, inputCopy):
  decryptionKey = 1
  inputCopy = [int(x) * decryptionKey for i, x in enumerate(inputCopy)]
  mixedFile = [(i, int(x) * decryptionKey) for i, x in enumerate(mixedFile)]
  mixedFile = shuffle(mixedFile, inputCopy)

  outputAns(mixedFile)

def part2(mixedFile, inputCopy):
  decryptionKey = 811589153
  inputCopy = [int(x) * decryptionKey for i, x in enumerate(inputCopy)]
  mixedFile = [(i, int(x) * decryptionKey) for i, x in enumerate(mixedFile)]
  for _ in range(10):
    mixedFile = shuffle(mixedFile, inputCopy)
  
  outputAns(mixedFile)

inputCopy = deepcopy(_input)
mixedFile1 = deepcopy(_input)
mixedFile2 = deepcopy(_input)
part1(mixedFile1, inputCopy)
part2(mixedFile2, inputCopy)
