import re


text = input().strip()


pattern = re.compile(r"\b\w+\b")


words = pattern.findall(text)


print(len(words))