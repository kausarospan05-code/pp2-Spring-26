import re

S = input().strip()
D = input().strip()

parts = re.split(D, S)#Мәтінді D үлгісі кездескен жерден кесіп, бөліктерге бөледі.
print(",".join(parts))
#S = "алма;алмұрт;шие"
#D = ";"
#res="алма,алмұрт,шие"