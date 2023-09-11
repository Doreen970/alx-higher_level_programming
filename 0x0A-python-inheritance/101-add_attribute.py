#!/usr/bin/python3
def add_attribute(obj, attr, value):
    """
    adds a new attribute to an object

    Raises:
    TypeError exception: indicates can't add a new attribute
    """
    
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    
    setattr(obj, attr, value)
