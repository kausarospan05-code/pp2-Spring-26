class Person:
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
    def string(self):
        return f"Student:  {self.name}, GPA: {self.gpa}"
aty,baga=input().split() #read from one line
baga=float(baga) #GPA ны флоат етып жатр
pers=Person(aty,baga)
print(pers.string())