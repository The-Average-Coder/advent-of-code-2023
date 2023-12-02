import re

with open('input.txt') as file:
  data = file.readlines()

# Format data into max number of reds, blues and greens
# For a real life situation you would probably be better off extracting the
# number of reds, blues and greens and finding the maximum later so the
# data is more adaptable, but for this problem it saves a few calculations
games = []
for game in data:
  id = int(re.search('Game (\d+)', game).group(1))
  maxReds = max(map(int, re.findall('(\d+) red', game)))
  maxBlues = max(map(int, re.findall('(\d+) blue', game)))
  maxGreens = max(map(int, re.findall('(\d+) green', game)))
  games.append((id, maxReds, maxGreens, maxBlues))

part1Total, part2Total = 0, 0

for i in games:
  if i[1] <= 12 and i[2] <= 13 and i[3] <= 14:
    part1Total += i[0]
  part2Total += i[1] * i[2] * i[3]

print(part1Total)
print(part2Total)