from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def browser():
    driver=webdriver.Chrome()

    # driver.get("http://www.baidu.com")

    return driver

if __name__ == '__main__':
    browser()