class NonIntArgumentException(Exception):
    def __init__(self, message="Non-integer argument provided"):
        super().__init__(message)


def handleNonIntArguments(func):
    def wrapper(*args):
        # Check if all arguments are integers
        try:
            func(*args)
        except TypeError:
            raise NonIntArgumentException("One or more arguments are not integers")
        return func(*args)
    return wrapper
