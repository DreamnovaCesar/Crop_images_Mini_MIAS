import time
from functools import wraps

class Timer(object):
    """
    A class for timing the execution of a function using the Timer.timer method.

    Examples:
    ---------
    >>> @Timer.timer
    ... def my_func(x, y):
    ...     return np.add(x, y)
    ...
    >>> my_func(np.array([1, 2, 3]), np.array([4, 5, 6]))
    
    ************************************************************
    Function my_func executed in 0.0000
    ************************************************************

    array([5, 7, 9])

    Notes
    -----
    This class decorator uses the `functools.wraps` decorator to preserve the
    metadata of the original function, such as the function name, docstring, and
    parameter information.

    """
    
    @staticmethod  
    def timer(func):
        """
        Decorator function that measures the execution time of a function.

        Parameters:
        -----------
        func : function
            The function to be timed.

        Returns:
        --------
        wrapper : function
            A function that executes the input function and prints the execution time.
        """
        @wraps(func)  
        def wrapper(*args, **kwargs):
            start_time = time.time();
            result = func(*args, **kwargs);
            end_time = time.time();
            print("\n");
            print("*" * 60);
            print('Function {} executed in {:.4f}'.format(func.__name__, end_time - start_time));
            print("*" * 60);
            print("\n");
            return result
        return wrapper