n,p1,p2=map(int,input().split())
arr=list(map(int,input().split()))


left=p1-1
right=p2-1
while left<right:
    var=arr[left]
    arr[left]=arr[right]
    arr[right]=var
    left+=1
    right-=1

for x in arr:
    print(x,end=" ")