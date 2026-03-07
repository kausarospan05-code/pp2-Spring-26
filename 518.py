import re
import sys

S = sys.stdin.readline().rstrip('\n')
P = sys.stdin.readline().rstrip('\n')

pattern = re.escape(P)
matches = re.findall(pattern, S)

print(len(matches))