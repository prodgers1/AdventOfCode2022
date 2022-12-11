import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(11)

monkeys = defaultdict()

def parse():
    i = 0
    while i < len(_input):
        monkey = defaultdict()
        lines = _input[i:i+7]
        monkeyId = int(lines[0].split()[1].replace(':', ''))
        items = lines[1].split(':')[1].strip().split(',')
        monkey["items"] = [int(item) for item in items]
        _, operand, value = lines[2].split('= ')[1].split()
        if operand == '+':
            monkey["operand"] = "+"
        else:
            monkey['operand'] = '*'
        
        if 'old' in value:
            monkey["operationValue"] = "old"
        else:
            monkey["operationValue"] = int(value)
        
        monkey["test"] = int(lines[3].split('by ')[1])
        monkey["testTrue"] = int(lines[4].split('monkey ')[1])
        monkey["testFalse"] = int(lines[5].split('monkey ')[1])
        monkey['inspected'] = 0
        monkeys[monkeyId] = monkey
        i += 7

parse()

lcm = math.lcm(*[monkeys[monkey]['test'] for monkey in monkeys])

for rounds in [20, 10000]:
    tempMonkeys = deepcopy(monkeys)
    for round in range(rounds):
        for monkeyId in tempMonkeys.keys():
            monkey = tempMonkeys[monkeyId]

            for item in monkey['items']:
                monkey['inspected'] += 1
                newWorry = 0
                operationValue = item if monkey['operationValue'] == 'old' else monkey['operationValue']
                if monkey['operand'] == '+':
                    newWorry = item + operationValue         
                elif monkey['operand'] == '*':
                    newWorry = item * operationValue
                
                if rounds == 20:
                    newWorry = newWorry // 3
                else:
                    newWorry = newWorry % lcm

                if newWorry % monkey['test'] == 0:
                    tempMonkeys[monkey['testTrue']]['items'].append(newWorry)
                else:
                    tempMonkeys[monkey['testFalse']]['items'].append(newWorry)
                
                monkey['items'] = []

    mostActiveMonkeys = sorted([tempMonkeys[monkey]['inspected'] for monkey in tempMonkeys], reverse=True)[:2]
    # 3 and 7
    print(mostActiveMonkeys)
    print(mostActiveMonkeys[0] * mostActiveMonkeys[1])