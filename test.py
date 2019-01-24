# -*- coding: utf-8 -*-
"""
This module creates python basic project files in a folder.
"""

import sys
import unittest
from pythonprojcreator import ProjCreatorProgram as PC


class Test():
    """Main class.

    """

    def __init__(self):
        pass

    def makefolder_test(self):
        """Test01"""
        PC.create_folder('C:\\alma\\korte')

class testFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_str_01 = 'Almás rétes'

    def test_sample_function(self):
        """Test01
        """

        test_class = PC()
        self.assertEqual(test_class.normalized_name(self.test_str_01), 'Almas_retes')

if __name__ == '__main__':
    PROG = Test()
    PROG.makefolder_test()
    unittest.main()
    sys.exit()
