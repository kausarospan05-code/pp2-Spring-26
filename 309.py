from math import pi

class Circle:
    def __init__ (self,radius):
        self.radius=radius
    def a(self):
        return pi*r*r
r=int(input())
area=Circle(r)
print(f"{area.a():.2f}")

