n = int(input())
seq = list(map(int, input().split()))

sum= 0
for i in range(n):
    if seq[i]>0:
        sum=sum+1
print(sum)