import re


text = input().strip()


result = re.sub(r"\d", lambda m: m.group(0) * 2, text)


print(result)