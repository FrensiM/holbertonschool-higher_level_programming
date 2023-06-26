#!/usr/bin/python3
'''class that inherits'''


from models.base import Base


class Rectangle(Base):
    '''class rectngle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''area of rectangle'''
        return self.__height * self.__width

    def display(self):
        '''print the square wiht #'''
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        txt = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        txt += " - {}/{}".format(self.__width, self.__height)
        return txt
