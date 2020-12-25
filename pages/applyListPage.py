from common.baseLog import Log
from appium.webdriver.webdriver import WebDriver
from public.decorator import sliptimes
from common.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class ApplyListPage(BasePage):
    # 点击进入农户采购
    purchaseApp = (By.ID, 'com.yonghui.cloud.freshstore:id/typePurchase')
    # 列表页第一条数据（断言文本元素）
    assertionText = (By.ID, 'com.yonghui.cloud.freshstore:id/apply_desc_tv')

    def all_list(self):
        """
        全部列表页
        :return:
        """
        self.click_button(self.purchaseApp, '点击进入农户采购应用')

    def pending_payment_list(self, n):
        """
        待付款
        :return:
        """
        self.click_button(self.purchaseApp, '点击进入农户采购应用')
        while 1:
            if n >= 1:
                for i in range(n):
                    self.sliding_screen('left', '全部列表页滑动至待付款列表页')
                break

    def pending_loading_car_list(self, n):
        """
        袋装车
        :param n: 向左滑动次数
        :return:
        """
        self.click_button(self.purchaseApp, '点击进入农户采购应用')
        while 1:
            if n >= 1:
                for i in range(n):
                    self.sliding_screen('left', '全部列表页滑动至待装车列表页')
                break

    def loaded_car_list(self, n):
        """
        已装车
        :param n: 向左滑动次数
        :return:
        """
        self.click_button(self.purchaseApp, '点击进入农户采购应用')
        while 1:
            if n >= 1:
                for i in range(n):
                    self.sliding_screen('left', '全部列表页滑动至已装车列表页')
                break

    def warehoused_list(self, n):
        """
        已入库
        :param n: 向左滑动次数
        :return:
        """
        self.click_button(self.purchaseApp, '点击进入农户采购应用')
        while 1:
            if n >= 1:
                for i in range(n):
                    self.sliding_screen('left', '全部列表页滑动至已入库列表页')
                break

    def invalid_list(self, n):
        """
        已作废
        :param n: 向左滑动次数
        :return:
        """
        self.click_button(self.purchaseApp, '点击进入农户采购应用')
        while 1:
            if n >= 1:
                for i in range(n):
                    self.sliding_screen('left', '全部列表页滑动至已作废列表页')
                break


    def get_assertion_ele(self):
        """
        断言元素
        :return:
        """
        assertionEle = (By.ID, self.assertionText[1])
        return assertionEle