"""
Program: test_sort_and_search_array.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Tests the basic array searching and sorting functionality
"""

import unittest
import unittest.mock as mock
from unittest.mock import patch
from fun_with_collections import sort_and_search_array as ss


class TestList(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_array.get_input', return_value='18')
    def test_search_list_no_item_found(self, input):
        self.assertEqual(ss.search_array(ss.make_array(), 25), -1)

    @patch('fun_with_collections.sort_and_search_array.get_input', return_value='25')
    def test_search_list_item_found(self, input):
        self.assertEqual(ss.search_array(ss.make_array(), 25), 0)


if __name__ == '__main__':
    unittest.TestCase()
