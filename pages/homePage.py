import time
from common.baseLog import Log
from common.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class HomePage(BasePage):

    roleBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/permission_firm_txt')
    purchaseBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/typePurchase')

    def home_page(self):
        Log().info('登录成功后跳转主页')
        self.click_button(self.roleBtn, '选择角色')
        time.sleep(2)
        self.click_button(self.purchaseBtn, '选择应用模块')