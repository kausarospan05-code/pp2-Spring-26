
n = int(input())

numbers = list(map(int, input().split()))

squares = map(lambda x: x * x, numbers)

result = sum(squares)

print(result)