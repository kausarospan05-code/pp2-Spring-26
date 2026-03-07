import re

s = input().strip()
pattern = r'^[A-Za-z].*[0-9]$'

if re.match(pattern, s):
    print("Yes")
else:
    print("No")