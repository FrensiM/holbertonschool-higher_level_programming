#!/usr/bin/python3
'''square'''


class Square:
    '''init class'''
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) is not tuple or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        '''size'''
        return self.__size

    @property
    def position(self):
        '''position'''
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''area'''
        return self.__size ** 2

    def my_print(self):
        '''print'''
        if self.__size == 0:
            print()
        else:
            for _ in range(self.size):
                if self.__position[1] > 0:
                    print("#" * self.__size)
                else:
                    print(" " * self.__position[0] + "#" * self.__size)
