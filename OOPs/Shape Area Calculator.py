# Same method name area(), different behavior in Circle and Sqaure.

radius = float(input("Enter value of radius: "))
side = float(input("Enter value of side: "))

class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):    
        return 3.14*self.radius*self.radius

class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side*self.side

shapes = [circle(radius), Square(side)]

for shape in shapes:
    print("Area:", shape.area())
