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


def make_list():
    """
    Description: gets 3 user inputs and combines them into a list

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

    return new_list


def sort_list():
    """
    Description: Sort a list in order with optional reverse

    :param parameter_1:
    :param parameter_2:
    :returns: will be no return because this function modifies a muteable
    :raises keyError: raises an exception
    """
    pass


def search_list():
    """
    Description: Search for an element at provided index

    :param parameter_1:
    :param parameter_2:
    :returns: this is what is returned
    :raises keyError: raises an exception
    """
    pass


if __name__ == '__main__':
    try:
        print(make_list())
    except ValueError as main_error:
        print(f'failure in main: {main_error}')
