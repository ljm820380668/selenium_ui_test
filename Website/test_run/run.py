import unittest
import time
import logging
from Website.common.start_driver import *
from BSTestRunner import BSTestRunner
#
# logging.basicConfig(level=logging.INFO,filename='./log/test.log',
#                     format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s-%(message)s')


report_dir='../test_report'
test_dir='../test_case'


discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_login.py")

now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+'/'+now+'result.html'

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title="Login Test Report" ,description="localhost login test")
    logging.info("start run test case.............")
    runner.run(discover)

latest_report=latest_report(report_dir)

logging.info("begin send email report...........")
send_mail(latest_report)

logging.info("Test end--------------------")