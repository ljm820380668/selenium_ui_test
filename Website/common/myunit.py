import unittest

from Website.common.start_driver import driverStart

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver= driverStart()
    def tearDown(self):
        self.driver.quit()