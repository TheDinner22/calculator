# methods for +, -, *, **, /, //, % are all here

import os, sys

# TODO del me
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

# dependencies
from pyLib.float import My_Float
is_float = My_Float.is_float

# decorator to validate inputs
def validator(function):
    def wrapper(*args): # NOTE: remember u can add **kwargs if needed
        # there should only be 2 args
        if len(args) != 2:
            raise TypeError("Expected 2 args, got " + str(len(args)))

        # args should be of type int or My_Float
        for arg in args:
            if type(arg) == int:
                continue
            elif is_float(arg):
                continue
            else:
                raise TypeError("Only accept int and My_Float, was given " + str(type(arg)))
                
        return function(*args)

    return wrapper



class Arithmatic:
    @staticmethod
    @validator
    def add(a, b):
        """add two numbers

        Args:
            a ([int, float]): first number to be added
            b ([int, float]): second number to be added

        Returns:
            [int, float]: just a + b as an int or float 
        """
        # make sure if a or b is a float, it is put first
        if is_float(a):
            return a + b
        elif is_float(b):
            return b + a
        else:
            return a + b

    @staticmethod
    @validator
    def sub(a, b):
        """subtract two numbers

        Args:
            a ([int, float]): first number to be subtracted
            b ([int, float]): second number to be subtracted

        Returns:
            [int, float]: just a - b as an int or float 
        """
        # make sure if a or b is a float, it is put first
        if is_float(a):
            return a - b
        elif is_float(b):
            return b - a
        else:
            return a - b

    @staticmethod
    @validator
    def mult(a, b):

        c = 0
        
        # if either number == 0, return 0
        if a == 0 or b == 0:
            return 0

        a_is_positive = True if a > 0 else False
        b_is_positive = True if b > 0 else False
        a = abs(a)
        b = abs(b)

        for i in range(b):
            c += a

        # decidie if a sign change is needed
        if (a_is_positive and b_is_positive) or ((not a_is_positive) and (not b_is_positive)):
            return c
        else:
            return -c

if __name__ == "__main__":
    print(Arithmatic.add(2, 5))

    print(Arithmatic.sub(2, -12))

    print(Arithmatic.mult(-2, 4))


