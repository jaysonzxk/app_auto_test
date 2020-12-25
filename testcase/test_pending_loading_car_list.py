import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.applyListPage import ApplyListPage


class PendingLoadingListTest(StartEnd):
    """
    待装车列表页面
    """
    @unittest.skip('跳过')
    def test_pending_loading_list(self):
        """
        待装车列表页面
        :return:
        """
        Log().info('----------待装车列表页面测试开始----------')
        self.login_action()  # 重新调用一下登录页面
        pending_loading_list_page = ApplyListPage(self.driver)
        pending_loading_list_page.pending_loading_car_list(2)
        result = self.base_driver.get_element_text(pending_loading_list_page.get_assertion_ele(), '待装车列表页面，获取断言文本')
        expect = ['装车失败', '待装车']
        if result not in expect:
            self.save_screenshot('待装车列表页面断言失败')
        self.assertIn(result, expect, msg='待装车列表页面测试失败，实际值{}不在期望值{}中'.format(result, expect))
        Log().info('----------待装车列表页面测试通过----------')
        Log().info('----------测试完成----------')


if __name__ == '__main__':
    unittest.main()