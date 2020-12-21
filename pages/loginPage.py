import time
from common.baseLog import Log
from common.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class LoginPage(BasePage):

    username_inputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/username_et')
    password_inputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/password_et')
    loginBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/loginBtView')
    tipsClk1 = (By.ID, 'com.yonghui.cloud.freshstore:id/cancle_btn')
    tipsClk2 = (By.ID, 'com.yonghui.cloud.freshstore:id/ok_btn')
    roleClk = (By.ID, 'com.yonghui.cloud.freshstore:id/permission_firm_txt')

    def login_action(self, username, password):
        while 1:
            if self.is_element_exist(self.loginBtn[1]) == False:
                self.sliding_screen('left', '启动页滑屏操作')
                continue
            else:
                Log().info('登录开始。。。')
                Log().info("输入用户名：{}".format(username))
                self.input_text(username, self.username_inputBox, '用户名')
                Log().info("输入密码：{}".format(password))
                self.input_text(password, self.password_inputBox, '密码')
                self.click_button(self.loginBtn, '登录按钮')
                self.click_button(self.tipsClk1, '提示框1')
                self.click_button(self.tipsClk2, '提示框2')
                self.click_button(self.roleClk, '选择角色')
                break

    @staticmethod
    def get_classification_ele():
        classification = (By.ID, 'com.yonghui.cloud.freshstore:id/bottom_tv_two')
        return classification


