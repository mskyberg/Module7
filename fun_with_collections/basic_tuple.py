"""
Program: basic_tuple.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Demonstrates the use of a basic tuple
"""


def average_scores(*args, **kwargs):
    """
    Description: calculates the average of scores and returns a string

    :param: *args, score arguments
    :param: **kwargs, arguments to include in return string
    :returns: returns a string formatted with kwargs and args
    :raises keyError: raises an exception
    """
    # calculate average of args
    average = 0
    for arg in args:
        average += arg
    average = average / (len(args))

    # format the string to return with keyword args
    return_string = 'Result: '
    for key, value in kwargs.items():
        return_string += "%s = %s " % (key, value)
    return f'{return_string}with current average {average}'


if __name__ == '__main__':
    print(average_scores(85, 90, 92, name='Mike', gpa='3.6', course='Python'))
    print(average_scores(71, 80, 78, 78, 59, team_name='Wild Cats',
                         leading_scorer='Jacob', games_remaining='7'))
    print(average_scores(94, 97, 99, 100, report='Vacation Review',
                         start_date='6/17/20', location='Miami'))
