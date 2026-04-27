n = int(input())
seq = list(map(int, input().split()))

max=seq[0]
for i in range(n):
    if seq[i]>max:
        max=seq[i]
print(max)