import re, math

with open('input.txt') as file:
  data = file.readlines()

races = [(int(i), int(j)) for i, j in zip(re.findall('\d+', data[0]), re.findall('\d+', data[1]))]
part2Race = (int("".join([str(i[0]) for i in races])), int("".join([str(i[1]) for i in races])))

# Finds number of integer solutions to the race
def findSolutionCount(race):
  b, c = race[0], -race[1]
  d = b**2 - -4 * c
  if d <= 0: # Either only 1 solution or error
    return 1
  sol1, sol2 = (-b+math.sqrt(d))/-2, (-b-math.sqrt(d))/-2
  return len(range(math.floor(sol1) + 1, math.ceil(sol2)))

part1SolutionCounts = []
for race in races:
  part1SolutionCounts.append(findSolutionCount(race))

part2SolutionCount = findSolutionCount(part2Race)

print(math.prod(part1SolutionCounts))
print(part2SolutionCount)