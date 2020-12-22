import time
from common.baseLog import Log as log
from common.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class LoginPage(BasePage):
    classIfication = (By.ID, 'com.yonghui.cloud.freshstore:id/bottom_tv_two')

    # @staticmethod
    def get_assertion_ele(self):
        """
        断言元素
        :return:
        """
        assertionEle = (By.ID, self.classIfication[1])
        return assertionEle


