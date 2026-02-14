import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return f"({self.x}, {self.y})"

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        return (self.x, self.y)

    def dist(self, other_point):
        return math.dist([self.x, self.y], [other_point.x, other_point.y])


# Input жасау
x, y = map(int, input().split())       # initial point
new_x, new_y = map(int, input().split())  # new coordinates
x1, y1 = map(int, input().split())     # second point жасау

# Create points
p = Point(x, y)
print(p.show())              # show initial

p.move(new_x, new_y)
print(p.show())              # show after move

q = Point(x1, y1)
print(f"{p.dist(q):.2f}")    # distance to second point