import json

source = json.loads(input().strip())
patch = json.loads(input().strip())

for key, value in patch.items():
    if value is None:
        if key in source:
            del source[key]
    else:
        source[key] = value

print(json.dumps(source, sort_keys=True, separators=(',', ':')))