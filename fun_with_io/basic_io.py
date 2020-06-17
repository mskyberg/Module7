"""
Program: basic_io.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Demonstrates io using tuples
"""

import os as os

FILE_NAME = 'student_info.txt'


def write_to_file(info):
    """
    Description:

    :param info: the student info tuple
    :returns: no return
    :raises keyError: raises an exception
    """
    f = open(FILE_NAME, 'a')
    f.write(f'{info[0]} test scores:')
    for score in info[1]:
        f.write(f'{score}\t')
    f.write('\n')
    f.close()


def read_from_file():
    """
    Description: Reads each line in a file and prints to console

    :returns: no return
    :raises
    """
    # Reads a file line by line
    file_dir = os.path.dirname(__file__)
    f = open(os.path.join(file_dir, FILE_NAME), "r")
    line1 = f.read()
    # Prints each line to the console
    print(line1)
    f.close()


def get_student_info(**kwargs):
    """
    Description: Get student test scores

    :param kwargs: this is the student name
    :returns:
    :raises ValueError: raises an exception
    """
    for key, value in kwargs.items():
        print(f'Test Scores for {value}')
    test_scores = []
    # Prompts the user to input as many test scores as they wish
    user_input = input('Enter a test score, Or press enter to continue:')
    while user_input != '':
        try:
            # attempt to cast string to an integer
            user_input = int(user_input)
        except ValueError:
            raise ValueError('Input is not numeric')
        else:
            # if successful, insert into list
            test_scores.append(user_input)
            user_input = input('Enter a test score, Or press enter to continue:')

    # Stores the information (name and scores) in a tuple
    for key, value in kwargs.items():
        student_info = (value, test_scores)
        write_to_file(student_info)


if __name__ == '__main__':
    try:
        get_student_info(name='Mike')
        get_student_info(name='John')
        get_student_info(name='Tony')
        get_student_info(name='Brad')
        read_from_file()
    except ValueError as err:
        print(f'Input Error: {err}')
