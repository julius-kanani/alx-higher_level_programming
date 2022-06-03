#!/usr/bin/python3
from sys import argv


def print_sys_arguments():
    """prints the number of and the list of its arguments

    Args:
       No arguments

    Returns:
       The return value. Nothing
    """
    ac = len(argv)
    print("{:d} {:s}{:s}{:s}".format(
                    ac - 1,
                    "argument" if ac <= 2 else "arguments",
                    "s" if ac <= 1 else "",
                    "." if ac == 1 else ":"))
    for index, args in enumerate(argv):
        if index == 0:
            continue
        print("{:d}: {:s}".format(index, args))


if __name__ == "__main__":
    print_sys_arguments()
