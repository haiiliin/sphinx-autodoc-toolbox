

class Parent:
    def parent_method(self):
        """This is a parent method."""
        pass


class Child(Parent):
    """This is an example class"""
    #: This is a public attribute
    attribute = 1
    
    def __init__(self):
        """This is the constructor of the Example class"""
        pass
    
    def public_method(self):
        """This is a public method"""
        pass
    
    def _private_method(self):
        """This is a private method"""
        pass

    def parent_method(self):
        """This is a derived method from the parent class"""
        pass
