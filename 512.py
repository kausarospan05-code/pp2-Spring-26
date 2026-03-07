import re


text = input().strip()


sequences = re.findall(r"\d{2,}", text)


print(" ".join(sequences))