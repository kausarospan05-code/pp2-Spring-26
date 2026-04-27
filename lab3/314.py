# Input
n = int(input())                     # number ofelements
arr = list(map(int, input().split()))  # thearray
q = int(input())                     # сандар

#әр операцияны ретпн орындау
for _ in range(q):
    op = input().split()#input
    if op[0] == "add":#кобейту
        x = int(op[1]) #lambda is a way to create a short, anonymous function — a function without a name
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
#сонгы массивты бос орынмен шыгарады