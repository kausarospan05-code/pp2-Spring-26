import sys

n=int(sys.stdin.readline())
doc={} #dict
for _ in range(n):
    parts=sys.stdin.readline().split()
    if parts[0]=="set": # dobav ili obnov key
        doc[parts[1]]=parts[2]
    elif parts[0]=="get": #key bar jok
        if parts[1] in doc:
            print(doc[parts[1]])#key bar i to print
        else:
            print("KE: no key "+parts[1]+" found in the document")