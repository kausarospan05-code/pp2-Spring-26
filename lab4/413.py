import json
import re

J = json.loads(input())
q = int(input())


def resolve_query(data, query):
    # Split into parts: keys and indices
    parts = re.findall(r'([a-zA-Z0-9_]+|\[\d+\])', query)#ser.friends[1] деген сұранысты ['user', 'friends', '[1]'] 
    #деген тізімге айналдырады. Біз әріптерді де, жақша ішіндегі сандарды да танимыз."
    current = data
    for part in parts:#massiv or sozdik
        if part.startswith('['):  # array index
            idx = int(part[1:-1])#[5]->5
            if isinstance(current, list) and 0 <= idx < len(current):
                current = current[idx]#bari norm bols ELEMENTTIN ISHINE KIREDI
            else:
                return "NOT_FOUND"
        else:  # object key
            if isinstance(current, dict) and part in current:
                current = current[part]#tabylsa kilttin manine otedi
            else:
                return "NOT_FOUND"
    return json.dumps(current, separators=(',',':'))#json formatynda 

# Process queries
for _ in range(q):
    query = input().strip()#shetindegi artyk bos orundar
    print(resolve_query(J, query))
#ол рекурсиясыз, қарапайым циклмен жұмыс істейді және
#  үлкен деректер қорын өңдеуге жылдамдығы жетед
