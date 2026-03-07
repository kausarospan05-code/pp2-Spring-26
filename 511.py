import re


text = input().strip()


uppercase_letters = re.findall(r"[A-Z]", text)


print(len(uppercase_letters))