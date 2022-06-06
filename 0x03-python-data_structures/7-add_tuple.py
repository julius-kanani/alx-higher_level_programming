#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples

    Args:
        tuple_a: the first tuple.
        tuple_b: the second tuple.

    Returns:
        The return value. a tuple with 2 integers
            The first element is addition of first element of each argument
            The second element is addition of second element of each argument
    """

    tuple_a_len = len(tuple_a)
    tuple_b_len = len(tuple_b)

    x = (0, 0)
    y = (0, 0)

    if tuple_a_len < 2:
        if tuple_a:
            x = tuple_a[0], 0
    else:
        x = tuple_a[0], tuple_a[1]

    if tuple_b_len < 2:
        if tuple_b:
            y = tuple_b[0], 0
    else:
        y = tuple_b[0], tuple_b[1]

    result = x[0] + y[0], x[1] + y[1]

    return (result)


if __name__ == "__main__":
    add_tuple(tuple_a, tuple_b)
