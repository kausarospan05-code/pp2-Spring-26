
m = int(input())


g = 0   # global
n = 0   # nonlocal


for _ in range(m):
    scope, value = input().split()
    value = int(value)

    if scope == "global":
        g += value
    elif scope == "nonlocal":
        n += value
    elif scope == "local":
        # lpass=ocal changes are ignored
        pass

print(g, n)