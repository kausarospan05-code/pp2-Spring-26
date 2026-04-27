def lim_generator(s,k):
    for i in range(k):
        for j in s:
            yield j

s=input().split()
k=int(input())
 
print(" ".join(lim_generator(s,k)))