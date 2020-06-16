"""
Program: basic_list.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Demonstrates the use of a basic list
"""


def get_input():
    """
    Description: Gets user input

    :returns: returns a string of user input
    :raises keyError: raises an exception
    """

    # prompt user for input
    # test it manually in your basic_list.py main.

    pass


def make_list():
    """
    Description: gets 3 user inputs and combines them into a list

    :returns: returns a list of 3 values
    :raises ValueError: raises an exception if input is not numeric
    """

    new_list = []
    # asks for 3 user input in a loop by
    for index in range(3):
        user_input = get_input()
        try:
            # attempt to cast string to an integer
            user_input = int(user_input)
        except ValueError:
            print('Input is in bad format!')
            raise ValueError
        else:
            # if successful, insert into list
            new_list.insert(index, user_input)

    return new_list


if __name__ == '__main__':
    pass
