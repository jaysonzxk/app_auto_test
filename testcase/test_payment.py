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
        payment_page.payment_action()
        # result = self.base_driver.get_element_text(pp.get_assertion_ele()[0], '付款完成，获取断言文本')
        # if result != '待付款':
        #     self.save_screenshot('制单断言失败')
        # self.assertEqual(result, '待付款', msg='主页断言失败，实际值{}与期望值{}不符'.format(result, '待付款'))
        # Log().info('----------付款测试通过----------')
        # Log().info('----------测试完成----------')


if __name__ == '__main__':
    unittest.main()