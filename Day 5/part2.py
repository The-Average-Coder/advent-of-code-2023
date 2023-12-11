import re

with open('input.txt') as file:
  data = file.read().split('\n\n')

part1Positions = list(map(int, re.findall('\d+', data[0])))

part2Positions = []
for i in range(0, len(part1Positions), 2):
  part2Positions.append(range(part1Positions[i], sum(part1Positions[i:i+2])))

maps = [[list(map(int, i.split())) for i in conversion.split('\n')[1:]] for conversion in data[1:]]
maps.reverse() # Since this method solves the problem backwards

# Takes in a trial location, finds the seed by reversing the mappings
def findSeedFromLocation(location):
  value = location
  for i in maps:
    for j in i:
      if value - j[0] + j[1] in range(j[1], sum(j[1:3])):
        value -= j[0] - j[1]
        break
  return value

testLocation = 0
seedFound = False
while not seedFound:
  testLocation += 1
  testSeed = findSeedFromLocation(testLocation)
  for i in part2Positions:
    if testSeed in i:
      seedFound = True
      break

print(testLocation)