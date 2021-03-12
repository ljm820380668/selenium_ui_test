import unittest
from AutoTest_project.Website.test_case.model import function,myunit
from AutoTest_project.Website.test_case.page_object.LoginPage import *
from time import sleep

class LoginTest(myunit.StartEnd):
    # @unittest.skipIf(4>3,"skil testlogin1_normal")
    def testlogin1_normal(self):
        '''username and password is normal'''
        print("testlogin1_normal is start test....")
        po=LoginPage(self.driver)
        po.Login_action('ljm_820380668','ljm19880729')
        sleep(2)
        self.assertEqual(po.type_loginPass_hint(),'设置')
        function.insert_img(self.driver,'login_1.png')
        print("testlogin1_normal test end!")

    def testlogin2_PasswdError(self):
        '''username and password is Error'''
        print("testlogin2_PasswdError is start test....")
        po = LoginPage(self.driver)
        po.Login_action('ljm_820380668@163.com', '123456')
        sleep(2)
        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, 'login_2.jpg')
        sleep(2)

    def testlogin3_Error(self):
        '''username and password is Error'''
        print("testlogin3_Error is start test....")
        po = LoginPage(self.driver)
        po.Login_action('l820380668@163.com', '123456')
        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, 'login_3.jpg')
        sleep(2)

if __name__ == '__main__':
    unittest.main()