n = int(input())                   
numbers = list(map(int, input().split()))  

count_truthy = sum(map(bool, numbers))     
print(count_truthy)                        