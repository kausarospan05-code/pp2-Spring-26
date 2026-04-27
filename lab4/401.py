def square_generator(N):
    for i in range(1, N + 1):
        yield i * i #kezek instead of returning
        # everything at once, it produces one square at a time.
N = int(input())
for square in square_generator(N):
    print(square)