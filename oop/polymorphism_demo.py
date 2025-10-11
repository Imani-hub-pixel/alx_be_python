import math
class Shape:
    def area(self):
        raise NotImplementedError("Derived classes need to override this method")
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def __str__(self):
        return f"The area of the Rectangle is: {self.area()} "
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def __str__(self):
        return f"The area of the Circle is: {self.area()} "