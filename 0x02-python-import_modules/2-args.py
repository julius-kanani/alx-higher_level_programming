#!/usr/bin/python3
from sys import argv


def print_sys_arguments():
    """prints the number of and the list of its arguments

    Args:
       No arguments

    Returns:
       The return value. Nothing
    """
    size = len(argv)
    prt = "{:d} {:s}{:s}"

    print(prt.format(
                    size - 1, "argument" if size <= 2 else "arguments",
                    "." if size == 1 else ":"
                    ))

    for index, args in enumerate(argv):
        if index == 0:
            continue
        print("{:d}: {:s}".format(index, args))


if __name__ == "__main__":
    print_sys_arguments()
