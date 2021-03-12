import smtplib, os
from selenium import webdriver
from email.mime.text import MIMEText
from email.header import Header


# 截图保存
def insert_img(driver, filename):
    # 获取文件所在目录
    func_path = os.path.dirname(__file__)
    # print(func_path)

    # 获取上级目录
    base_dir = str(os.path.dirname(func_path))
    base = base_dir.replace('\\', '/').split('/Website')[0]
    # print("项目的根目录是:"+base)

    filepath = base + '/Website/test_report/screenshot/' + filename
    # 捕捉页面截图
    driver.get_screenshot_as_file(filepath)


# 发送邮件
def send_mail(latest_report):
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    smtpserver = 'smtp.163.com'

    user = 'ljm_820380668@163.com'
    password = 'RFQRKKYMLDUTLPNV'  # 根据自己邮箱密码来设置

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

    print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    insert_img(driver, 'baidu.png')
