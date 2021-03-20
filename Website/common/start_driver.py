import logging.config
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from selenium import webdriver

CON_LOG = '../config/log_conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def driverStart():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def send_mail(latest_report):
    '''
    发送邮件
    :param latest_report:最新的报告
    :return:
    '''
    with open(latest_report, 'rb') as file:
        mail_content = file.read()
    smtpserver = 'smtp.163.com'
    user = 'ljm_820380668@163.com'
    password = 'JUNJPRIFOTZFAHAL'  # 根据自己邮箱密码来设置

    sender = 'ljm_820380668@163.com'
    receives = ['820380668@qq.com', '420247258@qq.com']

    subject = 'Web Selenium 自动化测试报告'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receives, msg.as_string())
    logging.info("Send email sucesss!!!!!!!!!!!!!!")
    smtp.quit()


def latest_report(report_dir):
    '''
    获取最新的测试报告
    :return:
    '''
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    logging.info("the latest report is " + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    return file


if __name__ == '__main__':
    driverStart()
