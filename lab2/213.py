n=int(input())


if n<2:
    print("NO")
else:
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
if prime:
    print("YES")
else:
    print("NO")