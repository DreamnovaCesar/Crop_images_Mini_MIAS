from functools import wraps

class Singleton(object):
    """A decorator to create singleton instances of a class.
    
    Notes
    -----
    This class decorator uses the `functools.wraps` decorator to preserve the
    metadata of the original function, such as the function name, docstring, and
    parameter information.
    
    """
    
    @staticmethod
    def singleton(cls):
        """
        Decorator function that ensures a class has only one instance.

        Parameters:
        -----------
        cls : class
            The class to be made a singleton.

        Returns:
        --------
        wrapper : function
            A function that ensures only one instance of the input class is created.
        """

        instance = None
        @wraps(cls) 
        def wrapper(*args, **kwargs):
            nonlocal instance;
            if instance is None:
                instance = cls(*args, **kwargs)
            return instance
        return wrapper