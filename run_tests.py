# -*- coding: utf-8 -*-

import sys
import unittest
from vp_check_list.login_test import LoginTest

if __name__ == '__main__':
	suite = unittest.TestSuite((
		unittest.makeSuite(LoginTest),
	))
	result = unittest.TextTestRunner().run(suite)
	sys.exit(not result.wasSuccessful())
