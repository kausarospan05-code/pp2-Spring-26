import re


text = input().strip()


words = re.findall(r"\w+", text)


print(len(words))