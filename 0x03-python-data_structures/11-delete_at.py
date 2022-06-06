#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """Deletes the item specified at a specific position in a list

    Args:
        my_list: a given list to delete an item.
        idx: position to delete an item from a given list.

    Returns:
        The return value. A modified list or None if index is
        negative or out of range.
    """

    list_len = len(my_list)

    if (idx >= 0) and (idx < list_len):
        for index, item in enumerate(my_list):
            if index == idx:
                my_list.remove(item)

    return (my_list)


if __name__ == "__main__":
    delete_at(my_list, idx)
