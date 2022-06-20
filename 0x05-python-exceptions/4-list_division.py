#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element in 2 lists

    Args:
        my_list_1: The first list.
        my_list_2: The second list.
        list_length: length of list to be returned.

    Returns:
        The return value. A new list(length = list_length) with all divisions
    """

    result = []
    divide = 0

    for i in range(list_length):
        try:
            divide = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            continue
        except TypeError:
            print("wrong type")
            continue
        except IndexError:
            print("out of range")
        finally:
            result.append(divide)
            divide = 0

    return (result)


if __name__ == "__main__":
    list_division(my_list_1, my_list_1, list_length)
