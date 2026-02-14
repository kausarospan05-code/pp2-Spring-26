# Input
n = int(input())                     # number ofelements
arr = list(map(int, input().split()))  # thearray
q = int(input())                     # сандар

# Apply each operation in order
for _ in range(q):
    op = input().split()
    if op[0] == "add":
        x = int(op[1])
        arr = list(map(lambda a: a + x, arr))
    elif op[0] == "multiply":
        x = int(op[1])
        arr = list(map(lambda a: a * x, arr))
    elif op[0] == "power":
        x = int(op[1])
        arr = list(map(lambda a: a ** x, arr))
    elif op[0] == "abs":
        arr = list(map(lambda a: abs(a), arr))

# Output
print(" ".join(map(str, arr)))