import re

s = input().strip()#strip() әдісі жолдың strip() әдісі жолдың (string) басындағы және соңындағы кездейсоқ артық бос орындарды алып тастайды.басындағы және соңындағы кездейсоқ артық бос орындарды алып тастайды.
p = input().strip()

if re.search(p, s):
    print("Yes")
else:
    print("No")
#егер s = "The cat sat" және p = "cat" болса, код "Yes" деп шығарады.