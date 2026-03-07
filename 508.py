import re

S = input().strip()
D = input().strip()

parts = re.split(D, S)
print(",".join(parts))