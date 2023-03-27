import time
from functools import wraps

class Retry(object):
    """
    A class for retrying the execution of a function with a delay using the Retry.retry_with_delay method.

    Examples:
    ---------
    >>> @Retry.retry_with_delay(max_retries=5, delay=2)
    ... def my_func(x, y):
    ...     if np.sum(x) == 0:
    ...         raise ValueError("Input array cannot be all zeros.")
    ...     return np.add(x, y)
    ...
    >>> my_func(np.array([1, 2, 3]), np.array([4, 5, 6]))
    array([5, 7, 9])
    
    >>> my_func(np.array([0, 0, 0]), np.array([4, 5, 6]))
    Error occurred: Input array cannot be all zeros. Retrying in 2 seconds...
    Error occurred: Input array cannot be all zeros. Retrying in 2 seconds...
    Error occurred: Input array cannot be all zeros. Retrying in 2 seconds...
    Error occurred: Input array cannot be all zeros. Retrying in 2 seconds...
    Error occurred: Input array cannot be all zeros. Retrying in 2 seconds...
    Traceback (most recent call last):
        ...
    Exception: Function failed after 5 retries..
    
    Notes
    -----
    This class decorator uses the `functools.wraps` decorator to preserve the
    metadata of the original function, such as the function name, docstring, and
    parameter information.
    
    """

    @staticmethod
    def retry_with_delay(max_retries=3, delay=1):
        """
        Decorator function that retries a function a certain number of times with a delay between retries.

        Parameters:
        -----------
        max_retries : int
            The maximum number of retries.
        delay : int
            The delay in seconds between retries.

        Returns:
        --------
        decorator : function
            A decorator function that applies the retry logic to the input function.
        """
        def decorator(func):
            @wraps(func) 
            def wrapper(*args, **kwargs):
                for i in range(max_retries):
                    try:
                        result = func(*args, **kwargs)
                        return result
                    except Exception as e:
                        print(f"Error occurred: {e}. Retrying in {delay} seconds...");
                        time.sleep(delay);
                raise Exception("Function failed after 3 retries.")
            return wrapper
        return decorator