import re

S = input().strip()
P = input().strip()
R = input().strip()

result = re.sub(P, R, S)
print(result)