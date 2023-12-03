import re

with open('input.txt') as file:
  data = file.read()

schematic = data.split()
symbols = "@#$%&*-+=/"

part1Total = 0
part2Total = 0

for row in range(len(schematic)):
  for col in range(len(schematic[row])):
    if schematic[row][col] in symbols:
      # Found symbol, now search for surrounding numbers
      neighbouringNumbers = []
      for neighbouringRow in range(row-1, row+2):
        for number in re.finditer('\d+', schematic[neighbouringRow]):
          if -1 <= number.start() - col <= 1 or -1 <= number.end() - 1 - col <= 1:
            neighbouringNumbers.append(int(number.group()))

      part1Total += sum(neighbouringNumbers)

      if len(neighbouringNumbers) == 2:
        part2Total += neighbouringNumbers[0] * neighbouringNumbers[1]

print(part1Total)
print(part2Total)