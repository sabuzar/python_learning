import math

class Shape:
    def __init__(self, color='black',  name="Default"):
        self.__color = color
        self.__name = name
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Square(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__lenght

    def set_length(self, length):
        self.__lenght = length


    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width



    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)


shape1 = Square(3, 3)
shape1.set_name("square")
print("name of the Shape is",shape1.get_name())
print("Area of square Shape1:", shape1.get_area())
print("Perimeter of square Shape1:", shape1.get_perimeter())
shape1.set_color("white")
print("Color of square Shape1:", shape1.get_color())




class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__lenght

    def set_length(self, length):
        self.__lenght = length


    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width



    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length) + 2 *(self.__width)

shape2 = Rectangle(3, 2)
shape2.set_name("rectangle")
print("name of the Shape is",shape2.get_name())
print("Area of rectangle shape2:", shape2.get_area())
print("Perimeter of rectangle shape2:", shape2.get_perimeter())
shape2.set_color("black")
print("Color of rectangle shape2:", shape2.get_color())




class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius=radius
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.__radius

shape3 = Circle(12)
shape3.set_name("circle")
print("name of the Shape is",shape3.get_name())
print("Area of circle shape3:", round(shape3.get_area()))
print("circumference of circle shape3:",round(shape3.get_circumference()))
shape3.set_color("purpule")
print("Color of circle shape3:", shape3.get_color())

