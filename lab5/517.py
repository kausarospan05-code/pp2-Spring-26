import re
import sys

text = sys.stdin.readline().strip()

pattern = r"\d{2}/\d{2}/\d{4}"
matches = re.findall(pattern, text)

print(len(matches))
#күн/ай/жыл) пішіміндегі күндерді іздеп, олардың жалпы санын есептейді
#Input:Today is 17/02/2025 and 18/02/2025
#Output:2