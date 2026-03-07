import re


text = input().strip()


if re.search(r"cat|dog", text):
    print("Yes")
else:
    print("No")