n = int(input())
c= {}

for _ in range(n): #loop=n times
    num = input().strip()
    c[num] = c.get(num, 0) + 1

res = sum(1 for v in c.values() if v == 3)
print(res)
