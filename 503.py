import re

s = input().strip()
p = input().strip()

matches = re.findall(p, s)
print(len(matches))