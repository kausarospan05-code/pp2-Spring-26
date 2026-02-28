import json
import re

# Read JSON
J = json.loads(input())
q = int(input())

# Function to resolve one query
def resolve_query(data, query):
    # Split into parts: keys and indices
    parts = re.findall(r'([a-zA-Z0-9_]+|\[\d+\])', query)
    current = data
    for part in parts:
        if part.startswith('['):  # array index
            idx = int(part[1:-1])
            if isinstance(current, list) and 0 <= idx < len(current):
                current = current[idx]
            else:
                return "NOT_FOUND"
        else:  # object key
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return "NOT_FOUND"
    return json.dumps(current, separators=(',',':'))

# Process queries
for _ in range(q):
    query = input().strip()
    print(resolve_query(J, query))