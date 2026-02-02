n = int(input())
arr = [input().strip() for _ in range(n)]
first = {}
for i in range(n):
    if arr[i] not in first:
        first[arr[i]] = i + 1
for s in sorted(first.keys()): #ab and cs is key возвращает список
    print(s, first[s])
