n = int(input())              
words = input().split()       

longest = max(words, key=len) #Using max(..., key=len), output the longest word. If several words have the same 
#maximum length, output the first one == esep berilgeni
#әр сөздің ұзындығын (len) салыстырып, ең үлкенін таңдайды
print(longest)                
#Input
#4
#cat tiger dog lion
#Output
#tiger