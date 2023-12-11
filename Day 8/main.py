import re, math

with open('input.txt') as file:
  data = file.readlines()

sequence = data[0].strip()
nodes = {re.findall('[A-Z1-9]+', i)[0]: re.findall('[A-Z1-9]+', i)[1:3] for i in data[2:]}

directionKeys = {'L': 0, 'R': 1}

# Part 1
START_NODE = 'AAA'
DESTINATION_NODE = 'ZZZ'
currentNode = START_NODE
part1Steps = 0
while currentNode != DESTINATION_NODE:
  for i in sequence:
    part1Steps += 1
    currentNode = nodes[currentNode][directionKeys[i]]
    if currentNode == 'ZZZ':
      break

# Part 2
# Goes through every starting node, finds the number of steps for each,
# then finds the lowest common multiple to give the answer
START_NODE_CHARACTER = 'A'
DESTINATION_NODE_CHARACTER = 'Z'
startNodes = [node for node in nodes if node[2] == START_NODE_CHARACTER]
destinationNodes = [node for node in nodes if node[2] == DESTINATION_NODE_CHARACTER]

stepsToDestinations = []
for node in startNodes:
  steps = 0
  while node not in destinationNodes:
    for step in sequence:
      steps += 1
      node = nodes[node][directionKeys[step]]
  stepsToDestinations.append(steps)

part2Steps = math.lcm(*stepsToDestinations)

print(part1Steps)
print(part2Steps)