"""
Program: sort_and_search_list.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Demonstrates the use of a basic list sorting and searching
"""

LIST_MAX = 3


def get_input():
    """
    Description: Gets user input

    :returns: returns a string of user input
    :raises keyError: raises an exception
    """

    # prompt user for input
    return input('Enter an integer value: ')


def make_list(sort=False, reverse=False):
    """
    Description: gets 3 user inputs and combines them into a list

    :param sort: optional bool whether or not to sort the list
    :param reverse: optional bool sort in reverse order or not
    :returns: returns a list of 3 values
    :raises ValueError: raises an exception if input is not numeric
    """

    new_list = []
    # asks for 3 user input in a loop by
    for index in range(LIST_MAX):
        user_input = get_input()
        try:
            # attempt to cast string to an integer
            user_input = int(user_input)
            if not 1 <= user_input <= 50:
                raise ValueError(f'Input is out of range! {user_input}')
        except ValueError:
            raise
        else:
            # if successful, insert into list
            new_list.insert(index, user_input)

    if sort:
        return sort_list(new_list, reverse)
    else:
        return new_list


def sort_list(a_list, rev=False):
    """
    Description: Sort a list in order with optional reverse

    :param a_list: a list to sort
    :param rev: sort order, true if reverse sort
    :returns: a sorted list
    """

    a_list.sort(reverse=rev)
    # I am passing in a list, I am returning a sorted list within the
    # make_list function
    return a_list


def search_list(a_list, element):
    """
    Description: Search for an element at provided index

    :param a_list: list to search
    :param element: element to find
    :returns: index of element
    :raises ValueError: raises an exception if element does not exist
    """
    try:
        index = a_list.index(element)
    except ValueError:
        return -1
    else:
        return index


if __name__ == '__main__':
    try:
        test_list = make_list(sort=True, reverse=False)
        print(test_list)
        element_index = int(input('Enter element to search:'))
        print(f'Index: {search_list(test_list, element_index)}')
    except ValueError as main_error:
        print(f'failure in main: {main_error}')
