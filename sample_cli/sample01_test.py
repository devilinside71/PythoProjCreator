# -*- coding: utf-8 -*-
"""
This module tests for __PROJECTNAMELCASE__.
__PROJECTNAMELCASE__ module:
__DESCRIPTION__
"""
import sys
import unittest
import __PROJECTNAMELCASE__


class testFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_str_01 = 'input text'

    def test_sample_function(self):
        """Test01
        """

        test_class = __PROJECTNAMELCASE__.__PROJECTNAME__()
        test_class.par_input = self.test_str_01
        self.assertEqual(test_class.sample_function(), 'inp text')


if __name__ == '__main__':
    unittest.main()
