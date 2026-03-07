import re

s = input().strip()
pattern = r'\b\w{3}\b'

matches = re.findall(pattern, s)
print(len(matches))