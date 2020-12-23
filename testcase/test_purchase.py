import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.purchasePage import PurchasePage


class PurchaseTest(StartEnd):
    """
    测试制单页面
    """
    def test_purchase(self):
        Log().info('----------制单页面测试开始----------')
        self.login_action()  # 重新调用一下登录页面
        pp = PurchasePage(self.driver)
        pp.purchase_action('P001', 'W003', '20027040', '800343', '100', '1')
        result = self.base_driver.get_element_text(pp.get_assertion_ele()[0], '制单完成，获取断言文本')
        if result != '待付款':
            self.save_screenshot('制单断言失败')
        self.assertEqual(result, '待付款', msg='主页断言失败，实际值{}与期望值{}不符'.format(result, '待付款'))
        Log().info('----------制单测试通过----------')
        Log().info('----------测试完成----------')


if __name__ == '__main__':
    unittest.main()