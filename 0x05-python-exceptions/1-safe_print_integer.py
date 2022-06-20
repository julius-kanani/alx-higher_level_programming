#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer

    Args:
        value: The integer value to be printed.

    Returns:
        The return value.   True if value printed correctly.
                            False if value is not an integer.
    """

    try:
        print("{:d}".format(value))

        return (True)
    except Exception:
        return (False)


if __name__ == "__main__":
    safe_print_integer(value)
