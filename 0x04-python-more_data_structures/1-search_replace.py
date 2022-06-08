#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a list.

    Args:
        my_list: initial list.
        search: the element to replace.
        replace: the new element.

    Returns:
        The return value. New list.
    """

    if (len(my_list) > 0):
        new_list = my_list[:]
        for index, element in enumerate(new_list):
            if element == search:
                new_list[index] = replace
        return (new_list)

    else:
        return (my_list)


if __name__ == "__main__":
    search_replace(my_list, search, replace)
