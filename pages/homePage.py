import time
from common.baseLog import Log
from common.basePage import BasePage
from pages.loginPage import LoginPage
from appium.webdriver.common.mobileby import MobileBy as By


class HomePage(BasePage):
    purchaseBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/typePurchase')
    homeTitle = (By.ID, 'com.yonghui.cloud.freshstore:id/title_tv')

    def home_page(self):
        Log().info('登录成功后跳转主页')
        self.click_button(self.purchaseBtn, '选择应用模块')

    # @staticmethod
    def get_assertion_ele(self):
        """
        断言元素
        :return:
        """
        assertionEle = (By.ID, self.homeTitle[1])
        return assertionEle
