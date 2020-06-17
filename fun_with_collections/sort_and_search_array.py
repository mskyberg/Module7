"""
Program: sort_and_search_array.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Demonstrates the use of a basic array sorting and searching
"""

import array as arr
LIST_MAX = 3


def get_input():
    """
    Description: Gets user input

    :returns: returns a string of user input
    :raises keyError: raises an exception
    """
    # prompt user for input
    return input('Enter an integer value: ')


def make_array(sort=False, reverse=False):
    """
    Description: gets 3 user inputs and combines them into a list

    :param sort: optional bool whether or not to sort the list
    :param reverse: optional bool sort in reverse order or not
    :returns: returns an array of 3 values
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

    new_array = arr.array('i', new_list)
    if sort:
        return sort_array(new_array, reverse)
    else:
        return new_array


def sort_array(a_arr, rev=False):
    """
    Description: Sort a list in order with optional reverse

    :param a_arr: an array to sort
    :param rev: sort order, true if reverse sort
    :returns: a sorted array
    """
    pass


def search_array(a_arr, element):
    """
    Description: Search for an element at provided index

    :param a_arr: array to search
    :param element: element to find
    :returns: index of element
    :raises ValueError: raises an exception if element does not exist
    """
    pass


if __name__ == '__main__':
    try:
        test_array = make_array(sort=True, reverse=False)
        print(test_array)
        element_index = int(input('Enter element to search:'))
        print(f'Index: {search_array(test_array, element_index)}')
    except ValueError as main_error:
        print(f'failure in main: {main_error}')
