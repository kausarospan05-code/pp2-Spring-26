import re
text = input().strip()
pattern = re.compile(r"\b\w+\b")
#\b шекарасын қолдану арқылы код сөздерді тыныс белгілерінен (үтір, нүкте) оңай ажырата алады.
#\w+ — бір немесе бірнеше әріптен/цифрдан тұратын сөзді білдіреді.
words = pattern.findall(text)
#Python compile() function takes source code as input and returns a code object that is ready to be executed and which can later be executed by the exec() function.
#hello world ,result=2
print(len(words))
#compile() transforms that string into a "Code Object