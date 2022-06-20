def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list

    Args:
        my_list: The list.
        x: Number of elements to print.

    Returns:
        The return value. The real number of elements printed.
    """
    count = 0

    try:
        for integer in range(x):
            count += 1
            print(my_list[integer], end='')
        print()
    except Error:
        raise Error

    return (count)


if __name__ == "__main__":
    safe_print_list(my_list, x)
