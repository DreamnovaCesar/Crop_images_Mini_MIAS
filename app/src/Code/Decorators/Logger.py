from functools import wraps

class Logger(object):
    """
    A class for logging the execution of a function using the Logger.log method.

    Examples:
    ---------
    >>> @Logger.log
    ... def my_func(x, y):
    ...     return np.add(x, y)
    ...
    >>> my_func(np.array([1, 2, 3]), np.array([4, 5, 6]))
    Function my_func called with args (array([1, 2, 3]), array([4, 5, 6])) and kwargs {}.
    Function my_func returned [5 7 9].
    array([5, 7, 9])
    
    Notes
    -----
    This class decorator uses the `functools.wraps` decorator to preserve the
    metadata of the original function, such as the function name, docstring, and
    parameter information.
    
    """
    
    @staticmethod
    def log(func):
        """
        Decorator function that logs the input function's arguments and return value.

        Parameters:
        -----------
        func : function
            The function to be logged.

        Returns:
        --------
        wrapper : function
            A function that logs the input function's arguments and return value.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Function {func.__name__} called with args {args} and kwargs {kwargs}.");
            result = func(*args, **kwargs);
            print(f"Function {func.__name__} returned {result}.");
            return result
        return wrapper