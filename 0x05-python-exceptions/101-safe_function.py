#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """Executes a function safely

    Args:
        fct: pointer to a function.
        args: list of arguments.

    Returns:
        The return value. Result of the function.
    """
    result = None

    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)

    return (result)


if __name__ == "__main__":
    safe_function(fct, *args)
