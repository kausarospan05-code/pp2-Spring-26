n = int(input())
epi={}
for _ in range(n):
    s, k = input().split()
    k = int(k)
    epi[s] = epi.get(s, 0) + k
for name in sorted(epi.keys()):
    print(name, epi[name])
