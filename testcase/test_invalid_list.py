import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.applyListPage import ApplyListPage


class InvalidListTest(StartEnd):
    """
    已作废列表页面
    """
    def test_invalid_list(self):
        """
        已作废列表页面
        :return:
        """
        Log().info('----------已作废列表页面测试开始----------')
        self.login_action()  # 重新调用一下登录页面
        invalid_list_page = ApplyListPage(self.driver)
        # invalid_list_page.all_list()
        invalid_list_page.invalid_list(5)
        result = self.base_driver.get_element_text(invalid_list_page.get_assertion_ele(), '已作废列表页面，获取断言文本')
        expect = ['已作废']
        if result not in expect:
            self.save_screenshot('已作废列表页面断言失败')
        self.assertIn(result, expect, msg='已作废列表页面测试失败，实际值{}不在期望值{}中'.format(result, expect))
        Log().info('----------已作废列表页面测试通过----------')
        Log().info('----------测试完成----------')


if __name__ == '__main__':
    unittest.main()