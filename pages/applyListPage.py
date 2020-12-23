from common.baseLog import Log
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

    def pending_payment_list(self):
        self.sliding_screen('left', '全部列表页滑动至待付款列表页')

    def pending_loading_car_list(self):
        self.sliding_screen('left', '待付款列表页滑动至待装车列表页')

    def loaded_car_list(self):
        self.sliding_screen('left', '待装车列表页滑动至已装车列表页')

    def warehoused_list(self):
        self.sliding_screen('left', '已装车列表页滑动至已入库列表页')

    def invalid_list(self):
        self.sliding_screen('left', '已入库列表页滑动至已作废列表页')

    def get_assertion_ele(self):
        """
        断言元素
        :return:
        """
        assertionEle = (By.ID, self.assertionText[1])
        return assertionEle