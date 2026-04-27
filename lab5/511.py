import re


text = input().strip()


uppercase_letters = re.findall(r"[A-Z]", text)
#[......]жақшалар ішіндегі таңбалардың кез келгенін іздеуді білдіреді (character set).
#findall fункциясы мәтіндегі барлық осындай әріптерді тауып, оларды тізімге жинайды

print(len(uppercase_letters))#"Python 3.12" res=1