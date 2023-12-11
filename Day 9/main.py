import re

with open('input.txt') as file:
  data = file.readlines()

sequences = [list(map(int, re.findall('-?\d+', i))) for i in data]

def findNextValue(sequence: list) -> int:
  if len(set(sequence)) == 1:
    return sequence[0]
  return sequence[-1] + findNextValue([sequence[n] - sequence[n-1] for n in range(1, len(sequence))])

nextValues = [findNextValue(sequence) for sequence in sequences]
previousValues = [findNextValue(list(reversed(sequence))) for sequence in sequences]

print(sum(nextValues))
print(sum(previousValues))