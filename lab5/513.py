import re
text = input().strip()
words = re.findall(r"\w+", text)#\w+ matches one or more letters, digits, or underscores. re.findall uses this to extract all "words" into a list.
print(len(words))
#code=сөздердің санын
#re.findall(r"\w+", "Python 3.12 is cool!")
#['Python', '3', '12', 'is', 'cool']
#result=5