import unittest
from Website.common.myunit import StartEnd
from Website.businessView.loginView import LoginView
import logging
from time import sleep

class LoginTest(StartEnd):
    csv_file='../data/登录账号测试数据.csv'

    # @unittest.skipIf(4>3,"skil testlogin1_normal")
    def testlogin1_normal(self):
        '''username and password is normal'''
        logging.info("testlogin1_normal is start test....")
        po=LoginView(self.driver)
        data = po.get_csv_data(self.csv_file, 1)
        po.Login_action(data[0], data[1])
        sleep(2)
        self.assertEqual(po.type_loginPass_hint(),'设置')
        po.getScreenShot('login')
        print("testlogin1_normal test end!");
    # @unittest.skip('skip testlogin2_PasswdError')
    def testlogin2_PasswdError(self):
        '''username and password is Error'''
        print("testlogin2_PasswdError is start test....")
        po = LoginView(self.driver)
        data = po.get_csv_data(self.csv_file, 2)
        po.Login_action(data[0], data[1])
        sleep(2)
        self.assertEqual(po.type_loginFail_hint(), '')
        po.getScreenShot('login')
        sleep(2)
    # @unittest.skip('testlogin3_Error')
    def testlogin3_Error(self):
        '''username and password is Error'''
        print("testlogin3_Error is start test....")
        po = LoginView(self.driver)
        data=po.get_csv_data(self.csv_file,3)
        po.Login_action(data[0], data[1])
        self.assertEqual(po.type_loginFail_hint(), '')
        po.getScreenShot('login')
        sleep(2)

if __name__ == '__main__':
    unittest.main()