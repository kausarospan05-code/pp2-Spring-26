import re
s = input().strip() 

if re.match(r"Hello", s):#if the pattern matches at the beginning of the string
    print("Yes")
else:
    print("No")