import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.applyListPage import ApplyListPage


class PendingPaymentListTest(StartEnd):
    """
    待付款列表页面
    """
    def test_pending_payment_list(self):
        """
        待付款列表页面
        :return:
        """
        Log().info('----------待付款列表页面测试开始----------')
        self.login_action()  # 重新调用一下登录页面
        pending_payment_list_page = ApplyListPage(self.driver)
        pending_payment_list_page.pending_payment_list(1)
        result = self.base_driver.get_element_text(pending_payment_list_page.get_assertion_ele(), '待付款列表页面，获取断言文本')
        expect = ['支付失败', '待付款']
        if result not in expect:
            self.save_screenshot('待付款列表页面断言失败')
        self.assertIn(result, expect, msg='待付款列表页面测试失败，实际值{}不在期望值{}中'.format(result, expect))
        Log().info('----------待付款列表页面测试通过----------')
        Log().info('----------测试完成----------')


if __name__ == '__main__':
    unittest.main()