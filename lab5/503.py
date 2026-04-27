import re

s = input().strip()
p = input().strip()
## Find all matches of the pattern in the string
matches = re.findall(p, s)
print(len(matches))