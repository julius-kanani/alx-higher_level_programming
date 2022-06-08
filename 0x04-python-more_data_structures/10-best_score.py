#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value.

    Args:
        a_dictionary: A dictionary with key, value data.

    Returns:
        The return value. Key with the biggest integer value.
                        if no score found return None.
    """

    if (a_dictionary):
        max_int = 0
        best_key = None
        for key, value in a_dictionary.items():
            if value > max_int:
                max_int = value
                best_key = key

        return (best_key)

    return (None)


if __name__ == "__main__":
    best_score(a_dictionary)
