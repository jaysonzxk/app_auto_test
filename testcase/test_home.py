import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from appium.webdriver.common.mobileby import MobileBy as By


class HomeTest(StartEnd):
    """
    测试跳转应用主页
    断言：头部标题
    """
    @unittest.skip('跳过')
    def test_home(self):
        Log().info('----------主页测试开始----------')
        self.login_action()  # 重新调用一下登录页面
        hp = HomePage(self.driver)
        hp.home_page()
        result = self.base_driver.get_element_text(hp.get_assertion_ele(), '跳转到应用主页，获取断言文本')
        if result != '我的申请':
            self.save_screenshot('主页断言失败')
        self.assertEqual(result, '我的申请', msg='主页断言失败，实际值{}与期望值{}不符'.format(result, '我的申请'))
        Log().info('----------主页测试通过----------')
        Log().info('----------测试完成----------')


if __name__ == '__main__':
    unittest.main()