from common.baseLog import Log
from common.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class PaymentPage(BasePage):
    # =====付款=====
    # 点击进入农户采购
    purchaseApp = (By.ID, 'com.yonghui.cloud.freshstore:id/typePurchase')  # 农户采购入口
    # 获取申请单状态
    applyStatus = (By.ID, 'com.yonghui.cloud.freshstore:id/apply_desc_tv')
    # 确认付款按钮
    payConfirmBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/sure_pay_order_tv')
    # 支付密码框
    payInputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/et_password')
    # 支付成功返回列表
    returnBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/return_list')
    # 重置支付
    repaymentBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/paystatus_click_tv')

    # 断言文本元素
    assertionText = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_pay_state')

    def pending_payment_action(self, pay_pwd):
        """
        待付款场景
        """
        # 农户采购入口
        self.click_button(self.purchaseApp, '农户采购入口')
        # 向左滑动到待付款页面
        self.sliding_screen('left', '申请列表-全部列表页向左滑动到待付款列表页')
        while 1:
            text = self.get_element_text(self.applyStatus, '获取申请单状态')
            if text == '待付款':
                self.click_button(self.applyStatus, '点击进入申请单详情页')
                self.click_button(self.payConfirmBtn, '点击确认付款按钮')
                self.input_text(pay_pwd, self.payInputBox, '支付密码输入')
                break
            else:
                self.sliding_screen('up_small', '向上滑动一格')
                continue

    def payment_failed_action(self, pay_pwd):
        """
        付款失败再次支付场景
        :return:
        """
        # 农户采购入口
        self.click_button(self.purchaseApp, '农户采购入口')
        # 向左滑动到待付款页面
        self.sliding_screen('left', '申请列表-全部列表页向左滑动到待付款列表页')
        while 1:
            text = self.get_element_text(self.applyStatus, '获取申请单状态')
            if text == '支付失败':
                self.click_button(self.applyStatus, '点击进入申请单详情页')
                self.sliding_screen('up_big', '向上滑动')
                self.click_button(self.repaymentBtn, '点击重新付款按钮')
                self.input_text(pay_pwd, self.payInputBox, '支付密码输入')
                break
            else:
                self.sliding_screen('up_small', '向上滑动一格')
                continue

    def get_assertion_ele(self):
        """
        1.待付款断言元素
        2.付款失败再次支付断言元素
        :return:
        """
        assertionEle = (By.ID, self.assertionText[1])
        return assertionEle


