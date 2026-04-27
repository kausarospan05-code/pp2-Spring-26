import re

text = input().strip()

if re.search(r"cat|dog", text):#|=or
    print("Yes")
else:
    print("No")