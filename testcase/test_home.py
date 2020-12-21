import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from appium.webdriver.common.mobileby import MobileBy as By


class HomeTest(StartEnd):

    def test_home(self):

        Log().info('跳转主页测试开始')
        lp = LoginPage(self.driver)
        hp = HomePage(self.driver)
        lp.login_action('80663333', 'Xx123456')
        hp.home_page()
        result = hp.get_element_text(hp.get_assertion_ele(), '跳转到应用主页，断言文本')
        self.assertEqual(result, '我的申请')


if __name__ == '__main__':
    unittest.main()