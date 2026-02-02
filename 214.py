n = int(input()) 
arr = list(map(int, input().split()))

f = {}
for x in arr:
    f[x] = f.get(x, 0) + 1

maxc = 0
answer = None

for num, count in f.items():
    if count > maxc or (count == maxc and (answer is None or num < answer)):
        maxc = count
        answer = num

print(answer)
