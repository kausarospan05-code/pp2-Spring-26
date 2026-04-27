n = int(input())                   
keys = input().split()            
values = input().split()           

d = dict(zip(keys, values))#zip арқылы екі тізімді біріктіріп, сөздік жасаймыз
query = input() #We read the query key          

print(d.get(query, "Not found"))   #get() әдісі арқылы іздейміз. Егер жоқ болса "Not found" қайтарамыз
#The .get() function looks for a key in a dictionary and gives a default answer instead of an error if that key is missing