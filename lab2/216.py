n=int(input())
arr=list(map(int,input(). split()))
newa=set()
for i in arr:
    if i not in newa:
        print("YES")
        newa.add(i)
    else:
        print("NO")
    

    
