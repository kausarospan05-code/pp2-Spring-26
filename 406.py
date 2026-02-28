def fibo_generator(n):
    if n<=0:
        return 
    elif n==1:
        yield 0
    elif n==2:
        yield 0
        yield 1
    else:
        a,b=0,1
        yield a
        yield b
    for i in range(2,n):
        next=a+b
        yield next
        a,b=b,next
n=int(input())
print(",".join(str(num) for num in fibo_generator(n)))
    #join works with string
