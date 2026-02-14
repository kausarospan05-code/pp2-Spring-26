class Pair:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def sums(self):
        a_sum=self.a+self.c
        b_sum=self.b+self.d
        return f"Result: {a_sum} {b_sum}"
a,b,c,d=map(int,input().split())
sum=Pair(a,b,c,d)
#methonddy call jasau
print(sum.sums())
