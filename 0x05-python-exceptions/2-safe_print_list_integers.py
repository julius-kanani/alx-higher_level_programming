#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers

    Args:
        my_list: The list to be used.
        x: The number of elements to acces in my_list.

    Returns:
        The return value. Real number of integers printed.
    """

    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1

        except TypeError:
            continue
        except ValueError:
            pass
    print()

    return (count)


if __name__ == "__main__":
    safe_print_list_integers(my_list, x)
