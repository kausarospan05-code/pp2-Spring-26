import re


text = input().strip()


match = re.search(r"Name:\s*(.+),\s*Age:\s*(\d+)", text)

if match:
    name = match.group(1)
    age = match.group(2)
    print(name, age)