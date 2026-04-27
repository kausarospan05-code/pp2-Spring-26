n = int(input())                   
numbers = list(map(int, input().split()))  #input="5 10 0", [5, 10, 0] болып сақталад
#Using all(), check whether every number is non-negative == esep berilgeni
if all(x >= 0 for x in numbers):   #Бұл функция "ішіндегі барлық мәндер True ма?" деп сұрайд елси хотяб 1 штук -1 бар болса false
    print("Yes")
else:
    print("No")