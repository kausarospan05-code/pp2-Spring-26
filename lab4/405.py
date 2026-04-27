def count_generator(N):
    for i in range(N,-1,-1):
        yield i

N=int(input())
for c in count_generator(N):
    print(c)