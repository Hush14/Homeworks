import math

class ConvexFigure:
    def Area(self):
        pass

    def Perimeter(self):
        pass

class Circle(ConvexFigure):
    def __init__(self,rad):
        self.rad=rad
    def Area(self):
        return math.pi*(self.rad**2)
    def Perimetr(self):
        return 2*math.pi*self.rad

class Rectangle(ConvexFigure):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def Area(self):
        return self.length*self.width

radius=float(input())
print(Circle(radius).Area())
print(Circle(radius).Perimetr())

length=float(input())
width=float(input())
print(Rectangle(length,width).Area())