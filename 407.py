def rev_generator(s):
    for i in range(len(s)-1,-1,-1):
        yield s[i]
s=input()
rev_s="".join(rev_generator(s))
print(rev_s)