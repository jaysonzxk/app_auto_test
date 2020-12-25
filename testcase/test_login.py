import unittest
from common.baseTest import StartEnd
from pages.loginPage import LoginPage


class LoginTest(StartEnd):

    @unittest.skip('跳过')
    def test_login(self):
        self.log.info('登录测试开始')
        self.login_action()
        result = self.get_element_text(self.get_assertion_ele(), '登录完成，获取断言文本')
        if result != '分类':
            self.save_screenshot('登录成功页面断言失败')
        self.assertEqual(result, '分类', msg='登录完成断言失败，实际值{}与期望值{}不符'.format(result, '分类'))


if __name__ == '__main__':
    unittest.main()