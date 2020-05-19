#!/usr/bin/python3
class Square:
    """Class Square that defines a square"""
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @property
    def position(self):
        return(self.__position)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")


    def area(self):
        return(self.__size**2)

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
