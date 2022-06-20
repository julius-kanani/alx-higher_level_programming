#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list

    Args:
        my_list: The list.
        x: Number of elements to print.

    Returns:
        The return value. The real number of elements printed.
    """
    count = 0
    error = False

    try:
        if not error:
            for integer in range(x):
                count += 1
                print(my_list[integer], end='')
            print()
    except Exception as Error:
        error = True
        print()
        count -= 1

    return (count)


if __name__ == "__main__":
    safe_print_list(my_list, x)
