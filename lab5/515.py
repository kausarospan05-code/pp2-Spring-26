import re
text = input().strip()
result = re.sub(r"\d", lambda m: m.group(0) * 2, text)
#If re.sub finds a digit, it creates a "match object" (which we have named m). m.group(0) represents the actual character that was matched
#"1" * 2 resul="11"
print(result)