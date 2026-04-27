import re
import sys

S = sys.stdin.readline().rstrip('\n')
P = sys.stdin.readline().rstrip('\n')

pattern = re.escape#(P)ішіндегі кез келген арнайы таңбаларды (мысалы, ., *, +) "қарапайым мәтін",It prevents errors during the search process."
matches = re.findall(pattern, S)#Бұл функция S мәтінінің ішінен pattern-ге сәйкес келетін барлық фрагменттерді тауып, оларды тізімге (list) салады.

print(len(matches))