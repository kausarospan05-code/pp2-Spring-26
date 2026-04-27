def pow_generator(n):
    for i in range(n+1):
        yield 2**i
        
n=int(input())
for c in pow_generator(n):
    print(c,end=" ")