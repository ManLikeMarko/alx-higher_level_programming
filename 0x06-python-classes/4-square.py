#!/usr/bin/python3
"""Square Module"""

class Square:
    """Defines square"""

    def __init__(self, size=0):
        """
        Constructor
        Args:
        size: length of one side
        """
        self.size = size

        @property
        def size(self):
            """
            Length of side of square
            Raises:
            ValueError: if size is less than 0
            Typeerror: if size is not int
            """
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be >= 0")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def area(self):
                """
                Area of square
                Returns: Size squared
                """
                return self.__size ** 2
