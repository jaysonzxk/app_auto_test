import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.paymentPage import PaymentPage


class PaymentTest(StartEnd):
    """
    测试付款页面
    """
    def test_payment(self):
        Log().info('----------付款页面测试开始----------')
        self.login_action()  # 重新调用一下登录页面
        payment_page = PaymentPage(self.driver)
        payment_page.pending_payment_action('123456')
        result = self.base_driver.get_element_text(payment_page.get_assertion_ele(), '付款完成，获取断言文本')
        if result != '支付申请已提交':
            self.save_screenshot('支付断言失败')
        self.assertEqual(result, '支付申请已提交', msg='主页断言失败，实际值{}与期望值{}不符'.format(result, '支付申请已提交'))
        Log().info('----------付款测试通过----------')
        Log().info('----------测试完成----------')

    def test_repayment(self):
        Log().info('----------重新支付页面测试开始----------')
        # self.login_action()  # 重新调用一下登录页面
        repayment_page = PaymentPage(self.driver)
        repayment_page.payment_failed_action('123456')
        result = self.base_driver.get_element_text(repayment_page.get_assertion_ele(), '重新支付完成，获取断言文本')
        if result != '支付申请已提交':
            self.save_screenshot('重新支付断言失败')
        self.assertEqual(result, '支付申请已提交', msg='主页断言失败，实际值{}与期望值{}不符'.format(result, '支付申请已提交'))
        Log().info('----------重新支付测试通过----------')
        Log().info('----------测试完成----------')


if __name__ == '__main__':
    unittest.main()