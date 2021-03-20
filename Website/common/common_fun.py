import csv
import os
import time
import logging

from selenium.common.exceptions import NoSuchElementException
from Website.common.start_driver import driverStart
from Website.baseView.baseView import BaseView


class Common(BaseView):


    def check_exist_element(self,path):
        '''
        检查元素是否存在
        :param path: 元素id(By.ID,'android/botton')
        :return:
        '''
        logging.info('=======begin check element=======')
        try:
            element=self.driver.find_element(*path)
        except NoSuchElementException:
            logging.info('=======not found element========')
        else:
            element.click()

    def get_csv_data(self, csv_file, line):
        '''
        读取csv文件里面的内容
        :param csv_file:csv文件的路径
        :param line: 第几行
        :return:
        '''
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    logging.info('获取csv文件第%s 行数据为:%s' %(line,row))
                    return row


    def getScreenShot(self, module):
        '''
        捕捉页面截图
        :param module:自定义模块
        :return:
        '''
        time=self.getTime()
        # 获取当前文件所在目录func_path = os.path.dirname(__file__)
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshot/%s_%s.png' %(module,time)
        logging.info('------------开始捕捉%s页面截图---------' %module)
        # 捕捉页面截图
        self.driver.get_screenshot_as_file(image_file)


    def getTime(self):
        '''
        获取格式输出当前系统时间
        :return:
        '''
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now


if __name__ == '__main__':
    driver=driverStart()
    driver.get("http://www.baidu.com")
    csv_file = '../data/登录测试数据.csv'
    data = Common(driver).get_csv_data(csv_file, 1)
    Common(driver).getScreenShot('login')
    driver.quit()
    print(data)
