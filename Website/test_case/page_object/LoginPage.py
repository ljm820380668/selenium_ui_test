from selenium.webdriver.common.by import By
from AutoTest_project.Website.test_case.page_object.BasePage import Page


class LoginPage(Page):
    url="/"
    username_loc=(By.NAME,'email')
    password_loc=(By.NAME,'password')
    submit_loc=(By.ID,'dologin')

    def type_username(self,username):
        frame = self.find_element(By.TAG_NAME, "iframe")
        self.switch_to_frame(frame)
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()
    #根据登录成功或者失败元素来判断是否失败
    loginPass_loc=(By.ID,'_mail_component_78_78')
    loginFail_loc=(By.ID,'loginbox-title')

    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        return  self.find_element(*self.username_loc).text