
n = int(input())

numbers = list(map(int, input().split()))

evens = filter(lambda x: x % 2 == 0, numbers)#his goes through the numberslist and only keeps the items where the lambda function returns True

result = len(list(evens))

print(result)