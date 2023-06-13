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
            return
        for height in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for width in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                if j + 1 == self.__size:
                    print('#')
                else:
                    print('#', end="")
