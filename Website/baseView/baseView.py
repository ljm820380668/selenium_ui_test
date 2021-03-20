from time import sleep
import logging
import yaml
import logging

class BaseView(object):
    def __init__(self,driver):
        with open('../config/base_yaml', 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        self.base_url=data['base_url']
        self.driver=driver
        self.timeout = 10

    def _open(self, url):
        url_ = self.base_url + url
        logging.info("open The Test page is %s" % url_)
        self.driver.get(url_)
        self.driver.maximize_window()
        sleep(2)
        assert self.driver.current_url == url_, 'Did not land on %s' % url_

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def get_window_size(self):
        return self.driver.maximize_window()

    def switch_to_frame(self,frame):
        return self.driver.switch_to.frame(frame)