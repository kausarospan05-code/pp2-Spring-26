class Rectangle:
    def __init__(self,length,width):
        #self=this object itself
        #length,width=values
        self.length=length #length inside the object
        self.width=width #width inside the object
    def area(self):
        return self.length * self.width
l,w=map(int,input(). split())
rectangle=Rectangle(l,w)
print(rectangle.area())

#init=structure ==ts job is to initialize (set up) the object with the values you give it.
