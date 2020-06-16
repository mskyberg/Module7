"""
Program: basic_list_exception.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Demonstrates the use of a basic list exception out of range
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
        except ValueError as e:
            print(f'Input is in bad format! {e}')
            raise ValueError
        else:
            # if successful, insert into list
            new_list.insert(index, user_input)

    return new_list


if __name__ == '__main__':
    try:
        print(make_list())
    except ValueError:
        print('failure in main')
