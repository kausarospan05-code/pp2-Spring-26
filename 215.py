n = int(input())
arr = [input().strip() for _ in range(n)]
uniq = set(arr)
print(len(uniq))
