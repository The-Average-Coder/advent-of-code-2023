import re

with open('input.txt') as file:
  data = file.read().split('\n\n')

part1Positions = list(map(int, re.findall('\d+', data[0])))

def mapSeeds(seeds, map):
  convertedSeeds = [i for i in seeds]

  for i in range(len(seeds)):
    for j in map:
      if seeds[i] in range(j[1], j[1] + j[2]):
        convertedSeeds[i] += j[0] - j[1]
        break
  
  return convertedSeeds

for conversion in data[1:]:
  maps = [list(map(int, i.split())) for i in conversion.split('\n')[1:]]
  part1Positions = mapSeeds(part1Positions, maps)

print(min(part1Positions))