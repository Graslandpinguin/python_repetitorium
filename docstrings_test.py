"""Docstring of this python module.

more description
"""

import sys

class MyClass(object):
    """The class's docstring

    more description
    """

    def my_method(self):
        """The method's docstring"""
        

def my_function():
    """The function's docstring

    more description
    """

print(sys.path.__doc__)
print(docstring_test.__doc__)
print(MyClass.__doc__)
print(MyClass.my_method.__doc__)
print(my_function.__doc__)