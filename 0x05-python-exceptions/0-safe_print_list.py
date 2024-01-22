#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints the first x elements of a given list.

    Args:
        my_list (list): A list containing elements of any type.
        x (int): The number of elements to print.

        Returns:
            The real number of elements successfully printed.
    """
    elem_num = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            elem_num += 1
    except IndexError:
        pass
    print()

    return elem_num
