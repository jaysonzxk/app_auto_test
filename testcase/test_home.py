import unittest
from common.baseTest import StartEnd
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from appium.webdriver.common.mobileby import MobileBy as By


class HomeTest(StartEnd):

    def test_home(self):
        homeTitle = (By.ID, 'com.yonghui.cloud.freshstore:id/title_tv')
        self.log().info('跳转主页测试开始')
        home = LoginPage(self.driver)
        result = home.get_element_text(homeTitle, '主页页面')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()