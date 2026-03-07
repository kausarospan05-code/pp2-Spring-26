import re
import sys

text = sys.stdin.readline().strip()

pattern = r"\d{2}/\d{2}/\d{4}"
matches = re.findall(pattern, text)

print(len(matches))http://ejudge.kz/new-client?contest_id=702