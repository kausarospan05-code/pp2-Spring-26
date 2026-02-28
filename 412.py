import json
import sys

def deep_diff():
    try:
        # Reading input from stdin
        line1 = sys.stdin.readline()
        line2 = sys.stdin.readline()
        
        if not line1 or not line2:
            return

        obj_a = json.loads(line1)
        obj_b = json.loads(line2)
    except (ValueError, EOFError):
        return

    differences = []

    def serialize(val):
        if val == "<missing>":
            return "<missing>"
        return json.dumps(val, separators=(',', ':'))

    def compare(a, b, path):
        # Case 1: Both are dictionaries - recurse
        if isinstance(a, dict) and isinstance(b, dict):
            all_keys = sorted(set(a.keys()) | set(b.keys()))
            for key in all_keys:
                new_path = f"{path}.{key}" if path else key
                val_a = a.get(key, "<missing>")
                val_b = b.get(key, "<missing>")
                compare(val_a, val_b, new_path)
        
        # Case 2: One is missing or they are different values/types
        elif a != b:
            differences.append(f"{path} : {serialize(a)} -> {serialize(b)}")

    compare(obj_a, obj_b, "")

    if not differences:
        print("No differences")
    else:
        # Problem asks for lexicographical sort by path
        differences.sort()
        for diff in differences:
            print(diff)

if __name__ == "__main__":
    deep_diff()