"""
Program: test_basic_list_exception.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Tests the basic list functionality with raising error
"""

import unittest
import unittest.mock as mock
from unittest.mock import patch
from fun_with_collections import basic_list


class TestList(unittest.TestCase):
    # @patch('fun_with_collections.basic_list.get_input', return_value='ab')
    # def test_make_list_non_numeric(self, input):
    #     with self.assertRaises(ValueError):
    #         basic_list.make_list()
    #
    # @patch('fun_with_collections.basic_list.get_input', return_value='25')
    # def test_make_list_within_range(self, input):
    #     self.assertEqual([25, 25, 25], basic_list.make_list())
    #
    # @patch('fun_with_collections.basic_list.get_input', return_value='0')
    # def test_make_list_below_range(self, input):
    #     with self.assertRaises(ValueError):
    #         basic_list.make_list()

    @patch('fun_with_collections.basic_list.get_input', return_value='51')
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            basic_list.make_list()


if __name__ == '__main__':
    unittest.TestCase()
