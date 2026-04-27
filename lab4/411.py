import json

def apply_patch(source, patch):#2 dictionaries
    for key, value in patch.items():
        if value is None:
            if key in source:
                del source[key]
        elif isinstance(value, dict) and isinstance(source.get(key), dict):
            source[key] = apply_patch(source[key], value) #recursia
        else:
            source[key] = value#key bar bolsa ozgerted,kok bolsa kosad
    return source

source = json.loads(input().strip()) #orig aqparat
patch = json.loads(input().strip()) #ozgertkimiz keletin
result = apply_patch(source, patch)
print(json.dumps(result, sort_keys=True, separators=(',', ':')))