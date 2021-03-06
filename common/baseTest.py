import time
import unittest
from common.baseLog import Log
from common.baseDriver import android_driver
from appium.webdriver.common.mobileby import MobileBy as By
from pages.loginPage import LoginPage


class StartEnd(unittest.TestCase, LoginPage):

    username_inputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/username_et')
    password_inputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/password_et')
    loginBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/loginBtView')
    tipsClk1 = (By.ID, 'com.yonghui.cloud.freshstore:id/cancle_btn')
    tipsClk2 = (By.ID, 'com.yonghui.cloud.freshstore:id/ok_btn')
    roleClk = (By.ID, 'com.yonghui.cloud.freshstore:id/permission_firm_txt')

    def setUp(self) -> None:
        self.base_driver = LoginPage(self.driver)
        self.log = Log()

    def tearDown(self) -> None:
        self.driver.quit()

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = android_driver()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def login_action(self, username='80663333', password='Xx123456'):
        while 1:
            # 判断是否在启动页和需要滑动多少次
            if self.is_element_exist(self.loginBtn[1]) == 'False':
                self.sliding_screen('left', '启动页滑屏操作')
                continue
            # 当noReset=true时，不会弹出两个提示框
            elif self.is_element_exist(self.tipsClk1[1]) == 'False':
                Log().info("输入用户名：{}".format(username))
                self.input_text(username, self.username_inputBox, '用户名')
                Log().info("输入密码：{}".format(password))
                self.input_text(password, self.password_inputBox, '密码')
                self.click_button(self.loginBtn, '登录按钮')
                self.click_button(self.roleClk, '选择角色')
                break
            # 当noReset=false时，会弹出两个提示框
            else:
                Log().info("输入用户名：{}".format(username))
                self.input_text(username, self.username_inputBox, '用户名')
                Log().info("输入密码：{}".format(password))
                self.input_text(password, self.password_inputBox, '密码')
                self.click_button(self.loginBtn, '登录按钮')
                self.click_button(self.tipsClk1, '提示框1')
                self.click_button(self.tipsClk2, '提示框2')
                self.click_button(self.roleClk, '选择角色')
                break


if __name__ == '__main__':
    StartEnd().login_action()