import re

S = input().strip()#Өзгерту керек бастапқы мәтін.
P = input().strip()#Ізделетін үлгі (pattern).
R = input().strip()#Аустырылатын мәтін (replacement).

result = re.sub(P, R, S)
print(result)
#S = "Менің 2 алма және 5 алмұрт бар"
#P = r'\d+'  "бір немесе бірнеше цифр"
#R (ауыстыру) = "#"
#resukt="Менің # алма және # алмұрт бар"