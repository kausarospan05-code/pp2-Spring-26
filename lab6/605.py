s = input()                       
vowels = "aeiouAEIOU"             

if any(ch in vowels for ch in s):
    #for ch in s: Енгізілген мәтіндегі әрбір таңбаны (ch) жеке-жеке қарап шығад
    #ch in vowels: Әрбір әріптің vowels тізімінде бар-жоғын тексереді (True/False)
    print("Yes")#esep berilgeni One line: Yes if there is at least one vowel, otherwise No ==any()
else:
    print("No")