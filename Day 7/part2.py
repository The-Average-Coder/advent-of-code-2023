import re
from collections import Counter

with open('input.txt') as file:
  data = file.read()

replace_dict = { 'T': 'A', 'J': '1', 'Q': 'C', 'K': 'D', 'A': 'E' }
pattern = re.compile("|".join(map(re.escape, replace_dict.keys())))
hands = [[i.split()[0], int(i.split()[1]), (pattern.sub(lambda match: replace_dict[match.group(0)], i.split()[0]))] for i in data.split('\n')]

frequency_keys = { '5': 'L', '41': 'K', '32': 'J', '311': 'I', '221': 'H', '2111': 'G', '11111': 'F' }
for hand in hands:
  letter_frequencies = dict(Counter(hand[0]))
  if 'J' in letter_frequencies and letter_frequencies['J'] != 5:
    joker_frequency = letter_frequencies.pop('J')
    letter_frequencies[max(letter_frequencies, key=letter_frequencies.get)] += joker_frequency
  letter_frequencies = sorted(letter_frequencies.values(), reverse=True)
  hand[2] = frequency_keys[''.join(map(str, letter_frequencies))] + hand[2]

print(sum([(i + 1) * j[1] for i, j in enumerate(sorted(hands, key=lambda hand: hand[2]))]))