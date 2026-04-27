
import re

s = input().strip()
pattern = r'\S+@\S+\.\S+'
#\S+ Бір немесе бірнеше "бос емес" таңба (кез келген әріп, сан немесе символ, бірақ бос орын емес).
#\S+ -Домен аты "gmail"
#\.    Нүкте белгісі (оны экранға шығару үшін алдына \ қойылады, өйткені . regex-те арнайы мағынаға ие).
#\S  Домен аяқталуы  "com", "kz"
match = re.search(pattern, s)
if match:
    print(match.group())
else:
    print("No email")#match.group() функциясы табылған сәйкестікті толығымен экранға шығарады. else "No email" шығады.
    