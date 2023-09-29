from typing import Any, Optional


def append(value: Any, the_list: Optional[list] = []):
    """
    Appends a value to a list, and if the list isn't given, return the value on a new list.

    :param value: the value to append to `list`
    :type value: Any

    :param the_list: the list to append to, defaults to an empty list
    :type the_list: list, optional
    """
    the_list.append(value)
    return the_list


def append_fixed(value: Any, the_list: Optional[list] = None):
    """
    Appends a value to a list, and if the list isn't given, return the value on a new list.

    :param value: the value to append to `list`
    :type value: Any

    :param the_list: the list to append to, defaults to an empty list
    :type the_list: list, optional
    """
    if the_list is None:
        the_list = []
    the_list.append(value)
    return the_list
