506.py
import re

s = input().strip()
pattern = r'\S+@\S+\.\S+'

match = re.search(pattern, s)
if match:
    print(match.group())
else:
    print("No email")