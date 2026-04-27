n=int(input())
arr=list(map(int, input(). split()))
min=arr[0]
max=arr[0]
for i in range(n):
    if arr[i]<min:
        min=arr[i]
    if arr[i]>max:
        max=arr[i]

for j in range(n):
    if arr[j]==max:
        arr[j]=min
    print(arr[j],end=" ")
    