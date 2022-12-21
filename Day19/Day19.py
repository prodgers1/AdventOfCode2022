import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(19)

class Blueprint:
    def __init__(self, blueprintNum, oreRobotConfig, clayRobotConfig, obsidianRobotConfig, geodeRobotConfig):
        self.blueprintNum = blueprintNum
        self.oreRobotConfig = oreRobotConfig
        self.clayRobotConfig = clayRobotConfig
        self.obsidianRobotConfig = obsidianRobotConfig
        self.geodeRobotConfig = geodeRobotConfig

class RobotConfig:
    oreCost = 0
    clayCost = 0
    obsidianCost = 0
    type = ""

    def __init__(self, type, oreCost = 0, clayCost = 0, obsidianCost = 0):
        self.type = type
        self.oreCost = oreCost
        self.clayCost = clayCost
        self.obsidianCost = obsidianCost

    def HaveMats(self, ore, clay, obsidian):
        return ore >= self.oreCost and clay >= self.clayCost and obsidian >= self.obsidianCost
    
    def Build(self, ore, clay, obsidian):
        ore -= self.oreCost
        clay -= self.clayCost
        obsidian -= self.obsidianCost

        return (ore, clay, obsidian)


blueprints = defaultdict()

for line in _input:
    parsed = line.split()
    blueprintNum = int(parsed[1].rstrip(':'))

    oreRobotCost = int(parsed[6].strip())
    oreRobot = RobotConfig("ore", oreRobotCost)

    clayRobotCost = int(parsed[12].strip())
    clayRobot = RobotConfig("clay", clayRobotCost)

    obsidianRobotOreCost = int(parsed[18].strip())
    obsidianRobotClayCost = int(parsed[21].strip())
    obsidianRobot = RobotConfig("obsidian", obsidianRobotOreCost, obsidianRobotClayCost)

    geodeRobotOreCost = int(parsed[27].strip())
    geodeRobotObsidianCost = int(parsed[30].strip())
    geodeRobot = RobotConfig("geode", geodeRobotOreCost, obsidianCost=geodeRobotObsidianCost)

    b = Blueprint(blueprintNum, oreRobot, clayRobot, obsidianRobot, geodeRobot)
    blueprints[blueprintNum] = b


def collect(ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots):
    ore += (1 * oreRobots)
    clay += (1 * clayRobots)
    obsidian += (1 * obsidianRobots)
    geodes += (1 * geodeRobots)
    return (ore, clay, obsidian, geodes)

def buildRobots(oreRobots, clayRobots, obsidianRobots, geodeRobots, buildOreRobot = False, buildClayRobot = False, buildObsidianRobot = False, buildGeodeRobot = False):
    if buildGeodeRobot:
        geodeRobots += 1
    elif buildObsidianRobot:
        obsidianRobots += 1
    elif buildClayRobot:
        clayRobots += 1
    elif buildOreRobot:
        oreRobots += 1
    
    return (oreRobots, clayRobots, obsidianRobots, geodeRobots)

def quality_heuristic(state): 
    # As the famous saying goes: 
    # 1 geode in the hand is worth 1000 in the bush
    ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, minute = initialState
    return 1000*geodes + 100*obsidian + 10*clay + ore


minutes = 24


ans = []

for index, key in enumerate(blueprints):

    blueprint = blueprints[key]
    #ore, clay, obsidian, geodes,  oreRobots, clayRobots, obsidianRobots, geodeRobots, minutes
    queue = [(0, 0, 0, 0, 1, 0, 0, 0, 1)]
    geodeCount = 0
    geodesMined = set()
    depth = 0

    maxOreCostToBuild = max([blueprint.geodeRobotConfig.oreCost, blueprint.obsidianRobotConfig.oreCost, blueprint.clayRobotConfig.oreCost, blueprint.oreRobotConfig.oreCost])

    while queue:
        state = queue.pop(0)
        initialState = deepcopy(state)
        ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, minute = initialState

        # sort by geodes, obsidian, clay, ore to only deal with things getting us closer to the goal
        if minute > depth:
            queue.sort(key=quality_heuristic, reverse=True)
            queue = queue[:1000]
            depth = minute

        if minute == 19 and ore >= 2 and obsidian == 3 and clay == 17 and geodeRobots == 1:
            x = 5

        geodesMined.add((minute, geodes))

        if minute > minutes:
            break

        if blueprint.geodeRobotConfig.HaveMats(ore, clay, obsidian):
            ore, clay, obsidian = blueprint.geodeRobotConfig.Build(ore, clay, obsidian)
            ore, clay, obsidian, geodes = collect(ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots)
            oreRobots, clayRobots, obsidianRobots, geodeRobots = buildRobots(oreRobots, clayRobots, obsidianRobots, geodeRobots, buildGeodeRobot=True)
            geodesMined.add((minute, geodes))
            queue.append((ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, minute + 1))
            

        elif blueprint.obsidianRobotConfig.HaveMats(ore, clay, obsidian):
            ore, clay, obsidian = blueprint.obsidianRobotConfig.Build(ore, clay, obsidian)
            
            ore, clay, obsidian, geodes = collect(ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots)
            oreRobots, clayRobots, obsidianRobots, geodeRobots = buildRobots(oreRobots, clayRobots, obsidianRobots, geodeRobots, buildObsidianRobot=True)
            geodesMined.add((minute, geodes))
            queue.append((ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, minute + 1))
        
        else:
            if blueprint.clayRobotConfig.HaveMats(ore, clay, obsidian):
                ore, clay, obsidian = blueprint.clayRobotConfig.Build(ore, clay, obsidian)
                
                ore, clay, obsidian, geodes = collect(ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots)
                oreRobots, clayRobots, obsidianRobots, geodeRobots = buildRobots(oreRobots, clayRobots, obsidianRobots, geodeRobots, buildClayRobot=True)
                geodesMined.add((minute, geodes))
                queue.append((ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, minute + 1))
        
            ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, minute = initialState
            if blueprint.oreRobotConfig.HaveMats(ore, clay, obsidian):
                ore, clay, obsidian = blueprint.oreRobotConfig.Build(ore, clay, obsidian)
                
                ore, clay, obsidian, geodes = collect(ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots)
                oreRobots, clayRobots, obsidianRobots, geodeRobots = buildRobots(oreRobots, clayRobots, obsidianRobots, geodeRobots, buildOreRobot=True)
                geodesMined.add((minute, geodes))
                queue.append((ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, minute + 1))
        
        ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, minute = initialState
        ore, clay, obsidian, geodes = collect(ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots)

        #if ore < maxOreCostToBuild:
        geodesMined.add((minute, geodes))
        queue.append((ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, minute + 1))
    
    x = sorted(geodesMined)
    print(key, geodeCount)
    ans.append(key * geodeCount)
    


print(sum(ans))