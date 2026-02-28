def count_generator(N):
    for i in range(N,0):
        yield i
N=int(input())
for c in count_generator(N):
    print c