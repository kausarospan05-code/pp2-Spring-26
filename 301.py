
num = input().strip()

# Checkштп each digit
valid = True
for d in num:
    if int(d) % 2 != 0:   # if digit is odd проверяем
        valid = False
        break

# Output
if valid:
    print("Valid")
else:
    print("Not valid")