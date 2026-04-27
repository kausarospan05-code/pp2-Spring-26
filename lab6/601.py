
n = int(input())

numbers = list(map(int, input().split()))

squares = map(lambda x: x * x, numbers)#lambda is used to create small,
# anonymous functions — functions without a name.

result = sum(squares)#is a built-in python function,it adds up all the values in squares

print(result)