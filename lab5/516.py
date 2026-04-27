import re

text = input().strip()

match = re.search(r"Name:\s*(.+),\s*Age:\s*(\d+)", text)
#(.+) — бұл 1-ші топ: Name: дегеннен кейінгі кез келген таңбалар жиынын сақтайды.
#(\d+) — бұл 2-ші топ: Age: дегеннен кейінгі цифрларды сақтайды.

if match:#like boolean,Егер сәйкестік табылса,яғни match нөлге тең болмаса
    name = match.group(1)
    age = match.group(2)
    print(name, age)