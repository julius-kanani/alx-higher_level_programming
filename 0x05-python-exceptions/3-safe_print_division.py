#!/usr/bin/python3


def safe_print_division(a, b):
    """Divides 2 integers and prints the results

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The return value. Value of the division
    """

    result = None
    try:
        result = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(result))
        return (result)


if __name__ == "__main__":
    safe_print_division(a, b)
