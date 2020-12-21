import unittest
from common.baseTest import StartEnd
from common.baseLog import Log
from pages.homePage import HomePage
from appium.webdriver.common.mobileby import MobileBy as By


class HomeTest(StartEnd):

    def test_home(self):
        homeTitle = (By.ID, 'com.yonghui.cloud.freshstore:id/title_tv')
        Log().info('跳转主页测试开始')
        l = HomePage(self.driver)
        result = l.get_element_text(homeTitle, '主页页面')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()