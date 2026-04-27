def square_generator(A,B):
    for c in range(A,B+1):
            yield c*c
A,B=map(int,input().split())
for i in square_generator(A,B):
    print(i,end=" ")