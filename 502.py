import re

s = input().strip()
p = input().strip()

if re.search(p, s):
    print("Yes")
else:
    print("No")