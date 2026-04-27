n = int(input())                   
numbers = list(map(int, input().split())) 

unique_sorted = sorted(set(numbers))   #listтын setke ainaldyrady    
print(" ".join(map(str, unique_sorted)))   
#5
#3 1 2 3 2
#1 2 3