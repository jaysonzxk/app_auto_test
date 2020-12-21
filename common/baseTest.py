import time
import unittest
from common.baseLog import Log
from common.baseDriver import android_driver
from pages.loginPage import LoginPage


class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        print('----------测试开始---------')
        self.log = Log()

    def tearDown(self) -> None:
        print('----------测试结束----------')

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = android_driver()

    # def login_page(self):
    #     lp = LoginPage(self.driver)
    #     lp.login_action('80663333', 'Xx123456')
    #     return lp
