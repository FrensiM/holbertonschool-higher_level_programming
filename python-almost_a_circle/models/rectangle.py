#!/usr/bin/python3
'''class that inherits'''

from models.base import Base


class Rectangle(Base):
    '''class rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''area of rectangle'''
        return self.__height * self.__width

    def display(self):
        '''print the square with #'''
        for i in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        '''str func'''
        txt = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        txt += " - {}/{}".format(self.__width, self.__height)
        return txt

    def update(self, *args, **kwargs):
        ''' fun that update'''
        list_args = ["id", "width", "height", "x", "y"]

        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        '''represantation of a dictionary'''
        dic = {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
        return dic
