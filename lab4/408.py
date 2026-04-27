def prime_generator(n):
    for num in range(2, n+1):
        is_pri =True
        for i in range(2,int(num**0.5) + 1):
            if num % i ==0:
                is_pri= False
                break
        if is_pri:
            yield str(num)


n = int(input())
for p in prime_generator(n):
    print(p,end=" ")