n = int(input())                   
numbers = list(map(int, input().split()))  

count_truthy = sum(map(bool, numbers))     
#map,bool =Тізімдегі әрбір санды логикалық мәнге (bool) айналдырады.Егер сан 0 болса False болады.Егер сан нөл емес (оң немесе теріс) болса True болады.
print(count_truthy) #Нөл емес сандардың жалпы санын экранға шығарад