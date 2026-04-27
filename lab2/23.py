n=int(input())
seq=list(map(int,input().split()))
total=0
for i in range(n):
    total=total+seq[i]
print(total)