from math import pi
class Shape:
    def __init__(self,color):
        self.color = color

    # def area(self):
    #     pass

    # def disply_info(self):
    #     return f"color: {self.color}"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def disply_info(self):
        print(f"color: {self.color}, area: {self.area():.2f}")

class Rectangle(Shape):
    def __init__(self,color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def disply_info(self):
        print(f"color: {self.color}, length: {self.length}, width: {self.width}, area: {self.area()}")


class Triangle(Shape):
    def __init__(self,color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width

    def area(self):
        return (self.height * self.width)/2

    def disply_info(self):
        print(f"color: {self.color}, height: {self.height}, width: {self.width}, area: {self.area()}")





cookie = Circle("blue", 1.5)
# print (cookie.area())

biscuit = Rectangle("yellow", 5, 10)
# print(biscuit.area())

cracker = Triangle("pink",2,4)

# print (cookie.disply_info())
# print (biscuit.disply_info())

cookie.disply_info()
biscuit.disply_info()
cracker.disply_info()

# print(cookie)
# print(biscuit)
