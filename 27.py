n = int(input())
seq = list(map(int, input().split()))

max=seq[0]
max_i=0

for i in range(n):
    if seq[i]>max:
        max=seq[i]
        max_i=i
        

print(max_i+1)