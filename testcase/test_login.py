import unittest
from common.baseTest import StartEnd
from pages.loginPage import LoginPage


class LoginTest(StartEnd):

    def test_login(self):
        self.log.info('登录测试开始')
        self.login_action()
        result = self.base_driver.get_element_text(self.base_driver.get_assertion_ele(), '登录完成，获取断言文本')
        self.assertEqual(result, '分类')


if __name__ == '__main__':
    unittest.main()