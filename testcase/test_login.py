import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.loginPage import LoginPage
from appium.webdriver.common.mobileby import MobileBy as By


class LoginTest(StartEnd):

    def test_login(self):
        Log().info('登录测试开始')
        lp = LoginPage(self.driver)
        lp.login_action('80663333', 'Xx123456')
        result = lp.get_element_text(lp.get_classification_ele(), '登录完成，获取断言文本')
        self.assertEqual(result, '分类')


if __name__ == '__main__':
    unittest.main()