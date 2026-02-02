n = int(input())
doc = {}
for _ in range(n):
    part = input().split()
    if part[0] == "set":
        doc[part[1]] = part[2]
    else:
        key = part[1]
        if key in doc:
            print(doc[key])
        else:
            print(f"KE: no key {key} found in the document")
