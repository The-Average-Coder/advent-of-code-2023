# **Advent Of Code 2023**
Simple and easy to understand python solutions of Advent of Code 2023

<h2>Explanations for each day:</h2>
<h3>Day 1</h3>
Part 1 doesn't require much explanation: make a list of all digits in each line, combine the first and last digit in the list into one number and add it to the total.<br />
Part 2 uses some RegEx to find patterns (spelt numbers) in the lines. It is important to note that re.finditer doesn't include overlapping patterns, but in this instance since no numbers from 1-9 have any overlap with themselves I decided to use it in order to keep the code simple and easy to read. If you wanted to apply this to a problem which does include overlapping patterns you can read more about it with the below link, it is fairly easy to do: https://www.geeksforgeeks.org/python-program-to-find-indices-of-overlapping-substrings/.

<h3>Day 2</h3>
First main block of code extracts the required numbers from the data using some simple regex and creates a list of tuples with all the information needed for answering the question. The second block then loops through all games and makes the required calculations / additions to the totals. Fairly simple problem, a good example of where a knowledge of RegEx is really useful to remove lots of splitting and string manipulation.
