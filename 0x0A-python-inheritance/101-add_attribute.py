#!/usr/bin/python3

def add_attribute(obj, attr, value):
    """
    adds a new attribute to an object

    Raises:
    TypeError exception: indicates can't add new attribute
    """
    
    raise TypeError("can't add new attribute")

    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
