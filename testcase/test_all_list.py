import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.applyListPage import ApplyListPage


class AllApplyListTest(StartEnd):
    """
    全部申请列表页面
    """
    @unittest.skip('跳过')
    def test_all_list(self):
        """
        全部申请列表页面
        :return:
        """
        Log().info('----------全部申请列表页面测试开始----------')
        self.login_action()  # 重新调用一下登录页面
        all_list_page = ApplyListPage(self.driver)
        all_list_page.all_list()
        result = self.base_driver.get_element_text(all_list_page.get_assertion_ele(), '全部申请列表页面，获取断言文本')
        expect = ['支付失败', '待装车', '已出单', '受理中', '已装车', '待付款', '装车失败', '已作废']
        if result not in expect:
            self.save_screenshot('全部申请列表页面断言失败')
        self.assertIn(result, expect, msg='全部申请列表页面测试失败，实际值{}不在期望值{}中'.format(result, expect))
        Log().info('----------全部申请列表页面测试通过----------')
        Log().info('----------测试完成----------')


if __name__ == '__main__':
    unittest.main()