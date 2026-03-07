import re

s = input().strip()
digits = re.findall(r'\d', s)
print(" ".join(digits))