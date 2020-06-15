"""
Program: test_basic_list.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Tests the basic list functionality
"""

import unittest
from unittest.mock import patch
from fun_with_collections import basic_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='9')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [9, 9, 9])


if __name__ == '__main__':
    unittest.TestCase()
