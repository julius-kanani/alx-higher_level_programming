#!/usr/bin/python3
from sys import argv


def infinite_addition():
    infinite_sum = 0
    ac = len(argv)

    for index, args in enumerate(argv):
        if index == 0:
            continue
        infinite_sum += int(args)
    print("{:d}".format(infinite_sum))


if __name__ == "__main__":
    infinite_addition()
