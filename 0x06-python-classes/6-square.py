#!/usr/bin/python3
"""Square Module"""

class Square:
    """Defines square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor
        ARgs:
        size(int): length of one side
        position(int, int): position of square
        """
        self.size = size
        self.position = position

        @property
        def size(self):
            """
            Get/set current size of square
            Raises:
            ValueError: if size is less than 0
            TypeError: if size is not int
            """
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        @property
        def position(self):
            """
            Get/set current position of square
            """
            return self.__position

        @position.setter
        def position(self, value):
            if (not isinstance(value, tuple) or
                    len(value) != 2 or 
                    not all(isinstance(num, int) for num in value) or 
                    not all(num >= 0 for num in value)):
                raise TypeError("position must be a tuple of two positive integers")
            self.__position = value

        def area(self):
            """
            Area of square
            Returns: Size squared
            """
                return self.__size ** 2


