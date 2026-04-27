def even_generator(start,sony, step):
    for i in range(start,sony+1, step):
        yield i

N = int(input())
print(",".join(str(ev) for ev in even_generator(0, N, 2)))
#str(ev)=converts ech number into a string,join works only with strings
#joins all the strings togethrt